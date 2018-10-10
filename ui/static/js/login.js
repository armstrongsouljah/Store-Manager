const form = document.querySelector("form");
const username = document.querySelector("#username");
const password = document.querySelector("password")

form.addEventListener("submit", (e)=>{
    e.preventDefault()
    // check entered user and send them to respective dashboard
    if(username.value !== "admin" && password!=="password"){
        window.location = "./user_dash.html";
    }
    else{
        window.location = "./admin_dash.html";

    }
});