Ports:  
| Name            | Ports         |
| -------------   | ------------- |
| PostGres        | localhost:5434|
| Catalog Server  | localhost:8002|
| Reverse Proxy   | localhost:8081|  

Access Admin Panel:  
```  
http://localhost:8081/admin/    

Username : admin   
Password : admin  
```  

API Request:  
```
GET
http://localhost:8002/api/v1/catalog/products/?query=merlot&country=US&points=90

```

