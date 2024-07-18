```toml
name = 'create Post'
description = '/api/posts'
method = 'POST'
url = 'http://localhost:8000/api/posts/'
sortWeight = 3000000
id = 'a005cb79-280b-4c6a-ac57-d219729bbfc0'

[[body.formData]]
key = 'title'
value = 'new Post'

[[body.formData]]
key = 'content'
value = 'zzzzz'

[[body.formData]]
key = 'created_at'
value = '2024-01-01'
```
