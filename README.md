# OnlineProducts
 Simple API Server with CRUD using Python Django Framework.
 Example of this repo is hosted on https://django-onlineproduct.herokuapp.com/

# How to use
Go into virtual environment by using this command:
```
cd projectpath
.venv/Scripts/Activate
```
Then runserver:
```
python .\OnlineProducts\manage.py runserver 
```
Then you can open browser and type in:
localhost:8000

And the API Server is already running!

# Endpoints
### localhost:8000/{endpoint}
###	Products/
Localhost:8000/products/ is to return all of the products in the database in JSON format. Using GET method without body.
Response:
```json
{
    "Products": [
        {
            "id": 2,
            "name": "iPhone 14",
            "description": "Handphone",
            "price": 15000000,
            "status": "Available"
        },
        {
            "id": 3,
            "name": "iPhone 15",
            "description": "Handphone",
            "price": 17000000,
            "status": "Available"
        }
    ]
}
```

###	Products/<id>
Localhost:8000/products/<id> is to return products with id number in the database in JSON format. Using GET method without body.
Response:
```json
{
    "id": 3,
    "name": "iPhone 15",
    "description": "Handphone",
    "price": 17000000,
    "status": "Available"
}
```


###	Create/
Localhost:8000/create is to insert a product detail into database. Using POST method and body. It will return the newly created product detail.
Body:
```json
{
    "name": "iPhone 20",
    "description": "Handphone",
    "price": 50000000,
    "status": "Available"
}
```
Response:
```json
{
    "id": 4,
    "name": "iPhone 20",
    "description": "Handphone",
    "price": 50000000,
    "status": "Available"
}
```


###	Update/<id>
Localhost:8000/update is to update a product detail with id into database. Using PUT method and body. It will return the newly updated product detail.

Body:
```json
{
    "name": "iPhone 12",
    "description": "Handphone",
    "price": 7000000,
    "status": "Available"
}
```


Response:
```json
{
    "id": 4,
    "name": "iPhone 12",
    "description": "Handphone",
    "price": 7000000,
    "status": "Available"
}
```




###	Delete/<id>
Localhost:8000/delete/<id> is to delete a product detail with that id from the database. Using DELETE method without body. It will return nothing.
