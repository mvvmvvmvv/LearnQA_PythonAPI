import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
response_array = response.history
redirects_amount = len(response_array)

print("Количество редиректов:", redirects_amount)
print("Конечный URL:", response.url)
