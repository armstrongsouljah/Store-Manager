const form = document.querySelector("form.attendant-form");
const username = document.querySelector("#username");
const firstName = document.querySelector("#first_name");
const lastName = document.querySelector("#last_name");
const password = document.querySelector("#password");
const confirm = document.querySelector("#confirm");

form.addEventListener("submit", (e)=>{
    e.preventDefault()
    
    // check for entered values
    window.location = "./admin_dash.html"

})