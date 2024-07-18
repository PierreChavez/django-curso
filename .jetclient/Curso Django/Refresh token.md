```toml
name = 'Refresh token'
method = 'POST'
url = 'http://localhost:8000/api/auth/token/refresh/'
sortWeight = 6000000
id = '9cbbff05-1bf3-4790-a6aa-7ed44d11ca7a'

[[headers]]
key = 'Content-Type'
value = 'multipart/form-data'

[[body.formData]]
key = 'refresh'
value = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMTM2MjkxOSwiaWF0IjoxNzIxMjc2NTE5LCJqdGkiOiI3OThhYmYyNWQ3MDA0NDQzODA1NmEzNmQzYmE1M2JkMyIsInVzZXJfaWQiOjF9.8zesPFHSGQIkTaHKiy0fflFZ8PXYrQBfAm_7biWCIEY'
```
