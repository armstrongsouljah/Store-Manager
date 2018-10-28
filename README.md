# Store-Manager [![Build Status](https://travis-ci.org/armstrongsouljah/Store-Manager.svg?branch=develop)](https://travis-ci.org/armstrongsouljah/Store-Manager) [![Maintainability](https://api.codeclimate.com/v1/badges/de3d25a8dafaada7833c/maintainability)](https://codeclimate.com/github/armstrongsouljah/Store-Manager/maintainability) [![Coverage Status](https://coveralls.io/repos/github/armstrongsouljah/Store-Manager/badge.svg?branch=develop)](https://coveralls.io/github/armstrongsouljah/Store-Manager?branch=develop)


Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. [github pages](https://armstrongsouljah.github.io/Store-Manager/ui/)

## Heroku Endpoints
|Endpoint|Link|
|:---:|:---|
|Index Route|[/](https://soultech-store.herokuapp.com)|
|`Products`*POST*|[/api/v1/login](https://soultech-store.herokuapp.com/api/v1/login)|
|`Products`*GET*|[/api/v1/products](https://soultech-store.herokuapp.com/api/v1/products)|
|`Products`*GET* Item|[/api/v1/products/product_id](https://soultech-store.herokuapp.com/api/v1/products/1)|
|`Products` *POST*|[/api/v1/products](https://soultech-store.herokuapp.com/api/v1/products)|
|`Sales` *GET* Only Admin|[/api/v1/sales](https://soultech-store.herokuapp.com/api/v1/sales)|
|`Sales` *GET* Admin/Attendant|[/api/v1/sales/sale_id](https://soultech-store.herokuapp.com/api/v1/sales/1)|
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
  |Admin Dashboard|Attendant Dashboard| 
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

## Python Version Supported
`Python 3.6 and above`

### Testing the app
`$ pytest --cov app/tests -cov-report term-missing`

### Running the app

`$ python3 run.py`

### Documentation
[view it here](https://documenter.getpostman.com/view/5140285/RWguwbvV)

### CREDITS
- Much appreciation goes to my fellow bootcamp candidates for your tireless efforts in helping me where I got stuck
- Lastly, thank you Andela for  the `Levelup35` program.
## Author
__Armstrong Souljah__

