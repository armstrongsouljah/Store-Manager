// category form
productEditForm = document.querySelector(".productEditForm");
itemQuantity = document.querySelector("#quantity");
productName = document.querySelector("#productName");
itemUnitCost = document.querySelector("#unitCost");
errors = document.querySelector(".errors");
message = document.querySelector(".message");
itemId = localStorage.getItem("selectedProduct");
adminToken = localStorage.getItem("admin_token");
selectedProduct = `https://soultech-store.herokuapp.com/api/v2/products/${itemId}`;

errors.style.color = "red";

fetch(selectedProduct)
  .then(response => response.json()) 
  .then(data => {
      detail = data["returned_product"]

      productName.value = detail["product_name"];
      productName.disabled = true;

      itemQuantity.value = detail["quantity"];
      itemUnitCost.value = detail["unit_cost"];
    })
  .catch(error => console.log(error))  
  
productEditForm.addEventListener("submit", (event)=>{
    event.preventDefault()
    if(itemQuantity.value <=0 || itemUnitCost.value <=0){
        errors.innerText = "Invalid entry, please try again."
    }else{
        productData = {
            quantity: Number(itemQuantity.value),
            unit_cost: Number(itemUnitCost.value)
        }
        
        message.innerText = "Updating product details."

        fetch(selectedProduct, {
            method:'PUT',
            mode:'cors',
            headers:{
                'Content-Type':'application/json',
                'Authorization': `Bearer ${adminToken}`
            },
            body: JSON.stringify(productData)
        })
        .then(res => res.json())
        .then(data => {
            message.innerText = data["message"];
            setTimeout(()=>{
                message.innerText ="";
            },3000)
        })
        .catch(error => console.log(error))
    }
})
