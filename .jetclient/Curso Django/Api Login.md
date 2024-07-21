```toml
name = 'Api Login'
method = 'POST'
url = 'http://localhost:8000/api/auth/login/'
sortWeight = 5000000
id = '89d9af55-23fe-4ecc-af58-c735682e2873'

[[headers]]
key = 'Content-Type'
value = 'multipart/form-data'

[[body.formData]]
key = 'email'
value = 'pierre_chavez@outlook.com'

[[body.formData]]
key = 'password'
value = '12345'
```
