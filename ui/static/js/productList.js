const productListEndpoint = "https://soultech-store.herokuapp.com/api/v2/products"
let productsTable = document.querySelector("table#products")
let tableBody = document.querySelector("tbody");



let createNode = (element) => {
    return document.createElement(element)
}
const append = (parent, element) => {
    return parent.appendChild(element)
}




//load the products each time a request is made for product
const loadProducts = (() => {
    fetch(productListEndpoint)
        .then(response => response.json())
        .then(data => {
            productList = data["products"];           
            
            for (let product of productList) {

                productRow = createNode("tr")
                productRow.style.padding ="8px";
                productRow.setAttribute("scope", "row")
                productId = createNode("th")
                productId.setAttribute("scope", "column")
                productId.innerText = product["product_id"];
                link = createNode("a")
                link.setAttribute("href", "./product_detail.html")
                link.innerText = "Details";
                link.className ="details"
                productName = createNode("td")
                productName.innerText = product["product_name"];

                productQuantity = createNode("td")
                productQuantity.innerText = product["quantity"];

                let productCategory = createNode("td")
                fetch(`https://soultech-store.herokuapp.com/api/v2/categories/${product["category"]}`)
                  .then(res => res.json())
                  .then(catData => {
                    productCategory.innerText = catData["category_name"]
                  })
                  .catch(err => console.log(err))
                // productCategory.innerText = product["category"];

                productAddedon = createNode("td")
                productAddedon.append(link)

                productPrice= createNode("td")
                productPrice.innerText = `${product["unit_cost"]} UGX`;                

                productRow.append(productId)
                productRow.append(productName)
                productRow.append(productQuantity)
                productRow.append(productCategory)
                productRow.append(productAddedon)
                productRow.append(productPrice)
                tableBody.append(productRow)
            }
        
            // enable viewing of product details
            detailLinks = document.querySelectorAll("a.details")
            for(let linkItem of detailLinks){
                linkItem.addEventListener("click", (e)=>{
                    e.preventDefault()
                    selectedProduct = e.target.parentNode.parentNode.firstChild.innerText;
                    localStorage.setItem("selectedProduct", selectedProduct)
                    window.location = e.target.getAttribute("href");
                })
            }
        })
        .catch(error => console.log(error))
})()




