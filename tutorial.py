import requests
#1. Basic responses
get_response = requests.get('https://jsonplaceholder.typicode.com/posts')
#print(help(get_response))
print(get_response.status_code)
print(get_response.json())
print(get_response.text)