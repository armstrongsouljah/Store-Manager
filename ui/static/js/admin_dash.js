is_admin = localStorage.getItem("admin_loggedin");
admin_token = localStorage.getItem("admin_token");

if(admin_token === "null" && is_admin === "false"){
    window.location = "../" 
}




