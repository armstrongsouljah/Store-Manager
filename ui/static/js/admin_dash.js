const form = document.querySelector("form.attendant-form");
const username = document.querySelector("#username");
const firstName = document.querySelector("#first_name");
const lastName = document.querySelector("#last_name");
const password = document.querySelector("#password");
const confirm = document.querySelector("#confirm");

is_admin = localStorage.getItem("admin_loggedin");

// check if admin is loggedin
if(!is_admin){
    console.log("go away attendant")
}
// console.log(is_admin)




