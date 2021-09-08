import requests
obj = requests.get('https://api.conceptnet.io/c/en/mask').json()
print(type(obj))
print(obj.keys())
print(len(obj['edges']))
print(obj['edges'][1])