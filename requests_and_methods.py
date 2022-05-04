import requests

"""Запрос любого типа без параметра method"""
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Запрос любого типа без параметра method:", response, response.text)


"""Запрос не из списка"""
payload = {"method": "HEAD"}
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print("Запрос не из списка:", response, response.text)


"""Запрос с правильным значением method"""
payload = {"method": "POST"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
print("Запрос с правильным значением method:", response, response.text)

print()


print("Проверяет все возможные сочетания реальных типов запроса и значений параметра method:")

"""GET"""
for method in "GET", "POST", "PUT", "DELETE":
    payload = {"method": method}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    print("GET метод:", method, response, response.text)
print()

"""POST"""
for method in "GET", "POST", "PUT", "DELETE":
    payload = {"method": method}
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print("POST метод:", method, response, response.text)
print()

"""PUT"""
for method in "GET", "POST", "PUT", "DELETE":
    payload = {"method": method}
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print("PUT метод:", method, response, response.text)
print()

"""DELETE"""
for method in "GET", "POST", "PUT", "DELETE":
    payload = {"method": method}
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print("DELETE метод:", method, response, response.text)
print()
