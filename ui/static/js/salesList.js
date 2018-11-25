salesListEndPoint = "https://soultech-store.herokuapp.com/api/v2/sales"
adminToken = localStorage.getItem("admin_token")
tableBody = document.querySelector("tbody");

async function fetchAttendants(){
    let response =  await fetch('https://soultech-store.herokuapp.com/api/v2/auth/users', {
        headers: {
            'Authorization': `Bearer ${adminToken}`
        }
    })
    let data = await response.json()
    return data
}

async function retrieveProduct(record){
    let response = await fetch(`https://soultech-store.herokuapp.com/api/v2/products/${record["product_sold"]}`)
    let data = await response.json()
    return data
    
}

loadSales = (() => {

    fetch(salesListEndPoint, {
        headers: {
            'Authorization': `Bearer ${adminToken}`
        }
    })
        .then(response => response.json())
        .then(data => {

            fetchAttendants()
                .then(userData => {
                    for (let record of data){
                        retrieveProduct(record)
                        .then(productData => {
                            for(let user of userData["attendants"]){
                                if( user["user_id"] === record["attendant"]){
                                    record["attendant"] = user["username"]
                                    record["product_sold"] = productData["returned_product"]["product_name"]
                                    
                                    let saleRow = document.createElement("tr")
                                    let saleId = document.createElement("td")
                                    let saleAttendant = document.createElement("td")
                                    let productSold = document.createElement("td")
                                    let saleWorth = document.createElement("td")
                                    let saleDate = document.createElement("td")

                                    saleId.innerText = record["sale_id"]
                                    saleAttendant.innerText = record["attendant"]
                                    productSold.innerText = record["product_sold"]
                                    saleWorth.innerText = record["total_cost"]
                                    saleDate.innerText = record["timestamp"]

                                    saleRow.append(saleId)
                                    saleRow.append(saleAttendant)
                                    saleRow.append(productSold)
                                    saleRow.append(saleWorth)
                                    saleRow.append(saleDate)
                                    tableBody.append(saleRow)

                                }
                            }                            
                            
                        })
                        .catch(err => console.log(err))                       
                    }
                })
                .catch(error => console.log(error))                

        }

        )
        .catch(error => console.log(error))
})()