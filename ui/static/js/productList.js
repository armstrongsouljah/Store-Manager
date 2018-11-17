if(typeof localStorage.getItem("admin_loggedin")==="object"){
    window.location("../ui/")
}

const productListEndpoint = "https://soultech-store.herokuapp.com/api/v2/products"
let productsTable = document.querySelector("table#products")
let tableBody = document.querySelector("tbody");



let createNode = (element) => {
    return document.createElement(element)
}
const append = (parent, element) => {
    return parent.appendChild(element)
}

link = createNode("a", "href", "./product_detail.html")


//load the products each time a request is made for product
const loadProducts = (() => {
    fetch(productListEndpoint)
        .then(response => response.json())
        .then(data => {
            productList = data["products"];

            
            

            for (let product of productList) {

                

                productRow = createNode("tr")
                productRow.setAttribute("scope", "row")
                productId = createNode("th")
                productId.setAttribute("scope", "column")
                productId.innerText = product["product_id"];

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
                productAddedon.innerText = product["created_at"];

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
        })
        .catch(error => console.log(error))
})()

