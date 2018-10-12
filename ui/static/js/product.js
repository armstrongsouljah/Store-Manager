const form = document.querySelector("form");
const product_name = document.querySelector("#product_name");
const category = document.querySelector("#category");
const added_on = document.querySelector("#added_on");
const quantity = document.querySelector("quantity");


form.addEventListener("submit", (e)=>{
    e.preventDefault()
    if(product_name.value!=="" && category.value !=="" && added_on.value !=="" && quantity.value !==""){
        window.location = "./products.html";
    }
    else{
        alert("Product details can't be empty!")
    }
})