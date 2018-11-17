const form = document.querySelector("form.attendant-form");
const username = document.querySelector("#username");
const firstName = document.querySelector("#first_name");
const lastName = document.querySelector("#last_name");
const password = document.querySelector("#password");
const confirm = document.querySelector("#confirm");

// ensure access by admin logged in

if( typeof localStorage.getItem("admin_loggedin") === "object"){
    window.location = "/ui/"
}



