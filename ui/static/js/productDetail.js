let selectedProduct = localStorage.getItem("selectedProduct");
let adminToken = localStorage.getItem("admin_token");
let detailRow = document.querySelector("tr.product-detail");
const deleteButton  = document.querySelector("a.deleteBtn");
const editButton =  document.querySelector("a.editButton");

productURI = `https://soultech-store.herokuapp.com/api/v2/products/${selectedProduct}`;

renderSelectedProduct = (()=>{
    fetch(productURI)
      .then(res => res.json())
      .then(data => {
         productData = data["returned_product"];
         let productId = document.createElement("td")
         productId.innerText = selectedProduct;

         let productName = document.createElement("td")
         productName.innerText = productData["product_name"]

         let productQuantity = document.createElement("td");
         productQuantity.innerText = productData["quantity"]

         let productPrice = document.createElement("td");
         productPrice.innerText = ` ${productData["unit_cost"]} UGX`;

         detailRow.appendChild(productId)
         detailRow.appendChild(productName)
         detailRow.appendChild(productQuantity)
         detailRow.appendChild(productPrice)
        
        })
      .catch(error => console.log(error))
})()

// delete selected product
deleteButton.addEventListener("click", (event)=>{
    event.preventDefault()
    if(window.confirm("Are you sure you want to delete?")){
        fetch(productURI, {
            method:'DELETE',
            mode:'cors',
            headers:{
                'Content-Type':'application/json',
                'Authorization': `Bearer ${adminToken}`
            }
        })
          .then(res => res.json())
          .then(data => {
              alert(data["message"])
              window.location = "./products.html"
          })
          .catch(error => console.log(error))
    }else{
        console.log("Request cancelled.")
    }
})

