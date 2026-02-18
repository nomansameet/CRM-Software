from flask import Blueprint, request, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Customer, Lead
from functools import wraps
import csv, smtplib
from config import Config

api_bp = Blueprint("api", __name__)

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = User.query.get(get_jwt_identity())
        if user.role != "admin":
            return jsonify(error="Admin access required"), 403
        return fn(*args, **kwargs)
    return wrapper

def send_email(msg):
    try:
        with smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT) as s:
            s.starttls()
            s.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            s.sendmail(Config.MAIL_USERNAME, Config.MAIL_USERNAME, msg)
    except:
        pass

@api_bp.route("/stats")
@jwt_required()
def stats():
    return jsonify({
        "New": Lead.query.filter_by(status="New").count(),
        "Contacted": Lead.query.filter_by(status="Contacted").count(),
        "Won": Lead.query.filter_by(status="Won").count()
    })

@api_bp.route("/leads/<int:id>", methods=["PUT"])
@jwt_required()
def update_lead(id):
    lead = Lead.query.get(id)
    lead.status = request.json["status"]
    db.session.commit()
    send_email("Lead status updated")
    return jsonify(message="Updated")

@api_bp.route("/export")
@jwt_required()
@admin_required
def export_csv():
    def generate():
        yield "id,customer_id,status\n"
        for l in Lead.query.all():
            yield f"{l.id},{l.customer_id},{l.status}\n"
    return Response(generate(), mimetype="text/csv")

