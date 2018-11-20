logoutLink = document.querySelector("a.logoutLink");
is_admin = localStorage.getItem("admin_loggedin");
is_attendant = localStorage.getItem("attendant_loggedin");
adminToken = localStorage.getItem("admin_token");
attendantToken = localStorage.getItem("attendant_token");

logoutLink.addEventListener("click", (e)=>{
    e.preventDefault()
    if (is_admin){
        localStorage.setItem("admin_token", null)
        localStorage.setItem("admin_loggedin", false)
        window.location = "../"
    }
    if(is_attendant){
        localStorage.setItem("attendant_token", null)
        localStorage.setItem("attendant_loggedin", false)
        window.location = "../"
    }
})
