let tableBody = document.querySelector("tbody");
let lastRow = document.querySelector("#last");
categoriesEndpoint =  'https://soultech-store.herokuapp.com/api/v2/categories';

const loadCategories = (()=>{
    fetch(categoriesEndpoint)
    .then(response => response.json())
    .then(data => {
        
        for(let category of data){
            let row = document.createElement("tr");
            let categoryID  =  document.createElement("td");
            let categoryName = document.createElement("td");
            let dateAdded = document.createElement("td");

            categoryID.innerText = category["category_id"];
            categoryName.innerText = category["category_name"];
            dateAdded.innerText = category["date_added"];

            row.appendChild(categoryID)
            row.appendChild(categoryName)
            row.appendChild(dateAdded)

            tableBody.prepend(row)

        }
        
    })
    .catch(error => console.log(error))
})()