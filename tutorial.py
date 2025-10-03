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
#if post_response.ok:
#    print('success!')
#else:
#    print('failure!')

#3. URL Params

params={
    'userId':'1'
}
filter_response=requests.get('https://jsonplaceholder.typicode.com/todos',params=params)
#print(filter_response)
#print(filter_response.json())

#4. Basic Auth

auth=('testuser','password')
basic_auth_response=requests.get('https://httpbin.org/basic-auth/testuser/password',auth=auth)
#print(basic_auth_response)

#5. Bearer Auth
headers={
    'Authorization': 'Bearer 1234567'
}
bearer_auth_response=requests.get('https://httpbin.org/bearer')
print(bearer_auth_response)