const username = document.querySelector("#username");
const role = document.querySelector("#role")
const password = document.querySelector("#password")
const confirmPassword = document.querySelector("#confirm")
let adminToken = localStorage.getItem("admin_token");
let error_message = document.querySelector("#error");
let message = document.querySelector("#message");
const registerForm = document.querySelector(".adduser");
let user = new Object()

validateEntries = (username, role, password, confirmPassword)=>{
  if(username.value === "" || role.value ==="" ||password.value ==="" || confirmPassword.value ===""){
      error_message.innerText ="All fields are required is required."
  }  
 else if(username.value.length <6){
    error_message.innerText = "Username must be above 6 letters"
 }
  else if(password.value !== confirmPassword.value){
      error_message.innerText = "Password do not match"
  }else{
      user.username  = username.value
      user.role =  role.value
      user.password = password.value
      
  }
  return user
}

registerForm.addEventListener("submit", (event)=>{
    event.preventDefault()
    validateEntries(username, role, password, confirmPassword)
    message.innerText = "Saving user details, please wait."
    fetch('https://soultech-store.herokuapp.com/api/v2/auth/signup', {
        method:'POST',
        mode:'cors',
        headers:{
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${adminToken}`
        },
        body:JSON.stringify(user)
    })
      .then(response => response.json())
      .then(data => {
          message.innerText = data["message"];
          
          setTimeout(()=>{
              registerForm.reset()
              message.innerText = "";
          }, 3000)
        })
      .catch(error => console.log(error))
})

