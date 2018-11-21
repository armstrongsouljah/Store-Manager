const productForm = document.querySelector("form");
const product_name = document.querySelector("#product_name");
let category = document.querySelector("#category");
const quantity = document.querySelector("#quantity");
const unitCost = document.querySelector("#unitcost");
let adminToken = localStorage.getItem("admin_token");
let productCreateEndPoint = 'https://soultech-store.herokuapp.com/api/v2/products'
let errorMessage = document.querySelector("span.errorBoard");
let messageBoard = document.querySelector("span.messageBoard");

errorMessage.style.color = "red";
errorMessage.style.background = "#f2f2f2";
messageBoard.color = "#01579b"
messageBoard.style.background ="#fff"

const renderCategories =(()=>{
    fetch('https://soultech-store.herokuapp.com/api/v2/categories')
      .then(response=> response.json())
      .then(data => {
          for (item of data){
             let selectOption = document.createElement("option");
             selectOption.innerText = item["category_name"]
             selectOption.setAttribute("value", item["category_id"])
             category.appendChild(selectOption)
          }
      })
      .catch(error => console.log(error))
})()


productForm.addEventListener("submit", (e)=>{
    e.preventDefault()
    if(product_name.value==="" || category.value ==="" || quantity.value==="" || unitCost.value === ""){
        errorMessage.innerText = "All fields are required.";
    }   

    else if(unitCost.value <= 0 || quantity.value <= 0 ){
        errorMessage.innerText = "Invalid data for quantity/unit_cost";
    }else{
        productData = {
            product_name:product_name.value,
            category: parseInt(category.value, 10),
            quantity: parseInt(quantity.value,10),
            unit_cost: parseInt(unitCost.value, 10)
        }
        messageBoard.innerText = "Saving your product, Please wait."

        fetch(productCreateEndPoint, {
            method:'POST',
            mode:'cors',
            headers:{
                'Content-Type':'application/json',
                'Authorization': `Bearer ${adminToken}`
            },
            body:JSON.stringify(productData)
        })
          .then(res => res.json())
          .then(data => {
              messageBoard.innerText = data["message"];
              // clear form and create space for another product
              productForm.reset()
              setTimeout(()=> {
                  messageBoard.innerText = " "
                },3000)
          })
          .catch(err => console.log(err))
               
        
    }

    
    
})



