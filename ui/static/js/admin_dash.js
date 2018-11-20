const form = document.querySelector("form.attendant-form");
const username = document.querySelector("#username");
const firstName = document.querySelector("#first_name");
const lastName = document.querySelector("#last_name");
const password = document.querySelector("#password");
const confirm = document.querySelector("#confirm");

let is_admin = localStorage.getItem("admin_loggedin");
 if (is_admin !== true){
     window.location = "/ui/"
 }




