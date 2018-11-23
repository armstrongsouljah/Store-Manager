const categoryName = document.querySelector("#category_name");
const categoryAddForm = document.querySelector("form.categoryAdd");
const message = document.querySelector(".message");
const error = document.querySelector(".errors");
const categoriesEndpoint = 'https://soultech-store.herokuapp.com/api/v2/categories';

error.style.color = "red";

categoryAddForm.addEventListener("submit", (event)=>{
    event.preventDefault()
    if(categoryName.value ==="" || categoryName.value === " "){
        error.innerText = "Empty category name is not allowed."
        categoryName.addEventListener("focus",()=>{
            error.innerText = "";
        } )
    }else{
        message.innerText = "Saving Category."
        fetch(categoriesEndpoint, {
            method:'POST',
            mode:"cors",
            headers:{
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem("admin_token")}`
            },
            body: JSON.stringify({category_name: categoryName.value})
        })
        .then(response => response.json())
        .then(data => {
            message.innerText = data["message"];
            setTimeout(()=>{
                message.innerText = ""
                categoryAddForm.reset()
            }, 3000)
        })
    }
})