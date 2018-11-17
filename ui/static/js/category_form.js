// category form
const form = document.querySelector(".category");
const category_name = document.querySelector("#category_name");
const added_on = document.querySelector("#added_on");
const instock = document.querySelector("#instock"); 

form.addEventListener("submit", (e)=>{
    e.preventDefault()
    if(category_name.value!=="" && added_on.value!==""){
        window.location = "./categories.html"
    }
    else{
        alert("empty values not accepted!")
    }
    
})

// ensure access by admin logged in

if( typeof localStorage.getItem("admin_loggedin") === "object"){
    window.location = "/ui/"
}

