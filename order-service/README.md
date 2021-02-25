Sample Request:

```  
curl --location --request POST 'http://localhost:8080/api/v1/orders/create/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "order_details": {
        "first_name": "Krupal",
        "last_name": "Jadhav",
        "street_1": "Some Street",
        "street_2": "Apt X",
        "city": "Some City",
        "state": "ANy State",
        "zip_code": 123456
    },
    "product": 2
}'  

```

For Postman:

```
{
    "order_details": {
        "first_name": "Krupal",
        "last_name": "Jadhav",
        "street_1": "Some Street",
        "street_2": "Apt X",
        "city": "Some City",
        "state": "Any State",
        "zip_code": 123456
    },
    "product": 2
}

```
