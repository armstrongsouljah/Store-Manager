salesListEndPoint = "https://soultech-store.herokuapp.com/api/v2/sales"
adminToken = localStorage.getItem("admin_token")
tableBody = document.querySelector("tbody");

loadSales = (() => {

    fetch(salesListEndPoint, {
        headers: {
            'Authorization': `Bearer ${adminToken}`
        }
    })
        .then(response => response.json())
        .then(data => {

            fetch('https://soultech-store.herokuapp.com/api/v2/auth/users', {
                headers: {
                    'Authorization': `Bearer ${adminToken}`
                }
            })
                .then(userResponse => userResponse.json())
                .then(userData => {
                    for (let record of data){
                        fetch(`https://soultech-store.herokuapp.com/api/v2/products/${record["product_sold"]}`)
                        .then(res => res.json())
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