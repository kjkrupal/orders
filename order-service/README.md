Sample Request:

```  
curl --location --request POST 'http://localhost:8080/api/v1/orders/create/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "order_details": {
        "first_name": "Krupal",
        "last_name": "Jadhav",
        "street_1": "2730 S Veitch Street",
        "street_2": "APT 312",
        "city": "Arlington",
        "state": "VA",
        "zip_code": 22206
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
        "street_1": "2730 S Veitch Street",
        "street_2": "APT 312",
        "city": "Arlington",
        "state": "VA",
        "zip_code": 22206
    },
    "product": 2
}

```
