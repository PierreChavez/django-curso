```toml
name = 'create Post'
description = '/api/posts'
method = 'POST'
url = 'http://localhost:8000/api/posts/'
sortWeight = 3000000
id = 'a005cb79-280b-4c6a-ac57-d219729bbfc0'

[auth.bearer]
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIxNTM5NzQ3LCJpYXQiOjE3MjE1MzYxNDcsImp0aSI6ImQ2NTQxZjcxZDRhYjRjMmY5NjgzOTMxYzEwNTYyMDYxIiwidXNlcl9pZCI6MX0.OsgzCCiLrWYJ6wPEYd4N3tXP-NUrNQwxHiHCT_tteHM'

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
