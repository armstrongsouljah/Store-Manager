const tableBody = document.querySelector("tbody");
let adminToken = localStorage.getItem("admin_token");

async function fetchUsers() {
    let response = await fetch(
        'https://soultech-store.herokuapp.com/api/v2/auth/users',
        {
            headers: {
                'Authorization': `Bearer ${adminToken}`
            }
        }
    )

    let data = await response.json()
    return data
}

const loadUsers = (() => {
    fetchUsers()
        .then(data => {
            users = data["attendants"];
            
            for(let user of users){
                let tableRow = document.createElement("tr")
                let userId = document.createElement("td")
                let username = document.createElement("td")
                let role = document.createElement("td")

                userId.innerText  = user["user_id"];
                username.innerText = user["username"];
                role.innerText = user["role"];

                tableRow.append(userId)
                tableRow.append(username)
                tableRow.append(role)

                tableBody.append(tableRow)
            }
        })
        .catch(error => console.log(error))
})()