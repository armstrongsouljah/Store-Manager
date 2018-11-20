const form = document.querySelector("form");
const username = document.querySelector("input#username");
const password = document.querySelector("input#password");
const error_msg = document.querySelector("span.errors");
const login_message = document.querySelector("span.status");

const loginEndpoint = "https://soultech-store.herokuapp.com/api/v2/auth/login";

//prevent default un authorised access
localStorage.setItem("admin_loggedin", false)
localStorage.setItem("attendant_loggedin", false)
localStorage.setItem("admin_token", null)
localStorage.setItem("attendant_token", null)


// clear error message when user tries again
username.addEventListener("focus", (e)=>{
    error_msg.innerText =""
})

password.addEventListener("focus", (e)=>{
    error_msg.innerText =""
})

const validateEntries = (username, password) => {
    if (username === "" && password === "") {
        error_msg.innerText = "empty credentials not allowed";
    }
    else if (username === "" || password === "") {
        error_msg.innerText = "username/password cannot be empty!";
    }
};

// custom error in case user enters wrong credentials
const handleErrors = (response)=>{
    if(!response.ok){
        error_msg.innerText = `${response.statusText}, invalid username/password`.toLowerCase
        ();
        login_message.innerText = "";
    }
    return response;
};

let dotheLogin = () => {
    fetch(loginEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'cors',
        body: JSON.stringify({ username: username.value, password: password.value })

    })     
        .then(handleErrors)  
        .then(response => response.json())
        .then(data => {
            if (data["user_role"] === "admin" && typeof data["token"] !== "object") {
                localStorage.setItem("admin_token", data["token"])
                localStorage.setItem("admin_loggedin", true)
                window.location = "./admin/";
            }
            else if (data["user_role"] === "attendant" && data["token"] !== null) {
                localStorage.setItem("attendant_token", data["token"])
                localStorage.setItem("attendant_loggedin", true)
                window.location = "./attendant/";
            }
        })        
        .catch(error => console.log(error))
}

form.addEventListener("submit", (e) => {
    e.preventDefault()
    error_msg.style.color = "red";
    login_message.style.color ="green";
    login_message.style.textAlign ="center";
    login_message.innerText = "Logging in, please wait";

    validateEntries(username.value, password.value);
    dotheLogin()

});