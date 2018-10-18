# Store-Manager [![Build Status](https://travis-ci.org/armstrongsouljah/Store-Manager.svg?branch=161211560-admin%2Fattendant-get-products)](https://travis-ci.org/armstrongsouljah/Store-Manager) [![Maintainability](https://api.codeclimate.com/v1/badges/de3d25a8dafaada7833c/maintainability)](https://codeclimate.com/github/armstrongsouljah/Store-Manager/maintainability) [![Coverage Status](https://coveralls.io/repos/github/armstrongsouljah/Store-Manager/badge.svg?branch=161297052-attendant-make-sale-record)](https://coveralls.io/github/armstrongsouljah/Store-Manager?branch=161297052-attendant-make-sale-record)


Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store. [github pages](https://armstrongsouljah.github.io/Store-Manager/ui/)

## Heroku Endpoints
[landing-page](https://soultech-store.herokuapp.com)

[get-products](https://soultech-store.herokuapp.com/api/v1/products)
[add-products](https://soultech-store.herokuapp.com/api/v1/products)



## Features
 `/attendant`
 - search available products
 - make sales
 - view user profile
 - add products to cart

 `/admin`
 - add attendant
 - add new, modify and delete products
 - view sales made by different attendants
 - assign product categories
 - view product details

## login details
  To access the admin dashboard, 
  username `admin`
  password `password`

  To access type in any username and password

## Installation
`$ git clone https://github.com/armstrongsouljah/Store-Manager.git`


### Prerequisites 
`$ cd Store-Manager `

`$ virtualenv venv -p python3`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

### Testing
`$ pytest --cov app/tests -cov-report term-missing`

### Run the app

`$ python3 run.py`
