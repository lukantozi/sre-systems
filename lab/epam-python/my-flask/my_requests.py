import requests

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 400:
    print('Not found!')

if response:
    print('Success!')
    print(response.content)
else:
    print('An error has occured')
