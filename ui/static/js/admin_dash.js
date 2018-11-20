const form = document.querySelector("form.attendant-form");
const username = document.querySelector("#username");
const firstName = document.querySelector("#first_name");
const lastName = document.querySelector("#last_name");
const password = document.querySelector("#password");
const confirm = document.querySelector("#confirm");

is_admin = localStorage.getItem("admin_loggedin");
admin_token = localStorage.getItem("admin_token");

if(admin_token === "null" && is_admin === "false"){
    window.location = "/ui/"
}




