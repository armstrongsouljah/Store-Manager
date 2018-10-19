# Store-Manager [![Build Status](https://travis-ci.org/armstrongsouljah/Store-Manager.svg?branch=161211864-admin/attendant-get-specific-salerecord)](https://travis-ci.org/armstrongsouljah/Store-Manager) [![Maintainability](https://api.codeclimate.com/v1/badges/de3d25a8dafaada7833c/maintainability)](https://codeclimate.com/github/armstrongsouljah/Store-Manager/maintainability) [![Coverage Status](https://coveralls.io/repos/github/armstrongsouljah/Store-Manager/badge.svg?branch=161211864-admin/attendant-get-specific-salerecord)](https://coveralls.io/github/armstrongsouljah/Store-Manager?branch=161211864-admin/attendant-get-specific-salerecord)


Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. [github pages](https://armstrongsouljah.github.io/Store-Manager/ui/)

## Heroku Endpoints
|Endpoint|Link|
|:---:|:---|
|Index Route|[index](https://soultech-store.herokuapp.com)|
|`Products`*GET*|[/api/v1/products](https://soultech-store.herokuapp.com/api/v1/products)|
|`Products`*GET* Item|[/api/v1/products/<int:id>](https://soultech-store.herokuapp.com/api/v1/products/1)|
|`Products` *POST*|[add-products](https://soultech-store.herokuapp.com/api/v1/products)|
|`Sales` *GET* Only Admin|[/api/v1/sales](https://soultech-store.herokuapp.com/api/v1/sales)|
|`Sales` *GET* Admin/Attendant|[/api/v1/sales/id](https://soultech-store.herokuapp.com/api/v1/1)|
|`Sales` *POST* Only Attendant|[/api/v1/sales](https://soultech-store.herokuapp.com/api/v1/sales)|


## UI Features
 |`/attendant`| `/admin`|
 |---|---|
 |- search available products| - add attendant|
 |- make sales| - add new, modify and delete products|
 |- view user profile|- view sales made by different attendants|
 |- add products to cart|- assign product categories|
 ||- view product details|
 

## login details
  |Admin Dashboar|Attendant Dashboard| 
  |:---:|:---:|
  |username `admin`|`any`|
  |password `password`|`any`|


## Project Installation
|Action|Command Neeeded|
|---|---|
|*Installation*|`$ git clone https://github.com/armstrongsouljah/Store-Manager.git`|

### Using the project
|Action|Command Needed|
|---|---|
|Project root| `$ cd Store-Manager `|
|Environment creation|`$ virtualenv venv -p python3`|
|Activate Environment `Linux` or `Mac` |`$ source venv/bin/activate`|
|Activate Environment *Windows*|`c:/ .\venv\Scripts\activate venv/bin/activate`|
|Install project Dependencies|`$ pip install -r requirements.txt`|

### Testing the app
`$ pytest --cov app/tests -cov-report term-missing`

### Running the app

`$ python3 run.py`
