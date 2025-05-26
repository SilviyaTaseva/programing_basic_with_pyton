import requests

city_name = input()
print(city_name)

print(f'Display Weather report for :{city_name}')
url = f'http://wttr.in/{city_name}'
res = requests.get(url)
print(res.text)
