import requests
#1. Basic responses 

get_response = requests.get('https://jsonplaceholder.typicode.com/todos')
#print(get_response)
#print(help(get_response))
#print(get_response.status_code)
#print(get_response.json())
#print(get_response.text)

#2. POST with body and headers

body={
    'userId':'1',
    'title':'Test Todo',
    'completed':False
}
headers={
    'Content-Type':'application/json'
}
post_response=requests.post('https://jsonplaceholder.typicode.com/todos',json=body,headers=headers)
#print(post_response)
#print(post_response.json())
#print(post_response.status_code)

#Do we have a successful response?
if post_response.ok:
    print('success!')
else:
    print('failure!')