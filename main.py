import requests

# Making a GET request
response_get = requests.get('https://api.github.com/events')

# Making a POST request
response_post = requests.post(
    'https://httpbin.org/post', data={'key': 'value'})

# Making a PUT request
response_put = requests.put('https://httpbin.org/put', data={'key': 'value'})

# Making a DELETE request
response_delete = requests.delete('https://httpbin.org/delete')

# Accessing the response data from the GET request
data_get = response_get.json()

print(data_get)

# Similarly, you can access the response data from POST, PUT, and DELETE requests
# data_post = response_post.json()
# data_put = response_put.json()
# data_delete = response_delete.json()
