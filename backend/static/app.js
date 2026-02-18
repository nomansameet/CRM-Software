function login(){
 fetch("/auth/login",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({username:user.value,password:pass.value})
 }).then(r=>r.json()).then(d=>{
  localStorage.token=d.access_token
  window.location="/dashboard"
 })
}

function signup(){
 fetch("/auth/signup",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({
    username: document.getElementById("newUser").value,
    password: document.getElementById("newPass").value,
    role: document.getElementById("role").value
  })
 })
 .then(r=>r.json())
 .then(d=>{
   alert("User registered successfully");
   window.location="/";
 })
}


function toggleDarkMode(){
 document.body.classList.toggle("dark-mode");
}

function allowDrop(e){ e.preventDefault(); }

function drop(e,status){
 e.preventDefault();
 const id = e.dataTransfer.getData("id");
 updateStatus(id,status);
 showToast("Lead moved to "+status);
}

function updateStatus(id,status){
 fetch("/api/leads/"+id,{
  method:"PUT",
  headers:{
   "Content-Type":"application/json",
   Authorization:`Bearer ${localStorage.token}`
  },
  body:JSON.stringify({status})
 })
}

function showToast(msg){
 const t=document.getElementById("toast");
 t.innerText=msg;
 t.classList.add("show");
 setTimeout(()=>t.classList.remove("show"),3000);
}

fetch("/api/stats",{
 headers:{Authorization:`Bearer ${localStorage.token}`}
}).then(r=>r.json()).then(d=>{
 if(document.getElementById("loader"))
  document.getElementById("loader").style.display="none";

 if(document.getElementById("newCount")){
  newCount.innerText=d.New;
  contactedCount.innerText=d.Contacted;
  wonCount.innerText=d.Won;

  new Chart(chart,{
   type:"bar",
   data:{labels:Object.keys(d),datasets:[{data:Object.values(d)}]}
  })
 }
})
