import json
import time
import requests

"""Создание задачи"""
create_task = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
create_task_json = json.loads(create_task.text)

token_value = create_task_json['token']
time_value = create_task_json['seconds']


"""Запрос ДО того, как задача готова"""
payload = {'token': token_value}
send_token_before = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
send_token_before_json = json.loads(send_token_before.text)

status_value = send_token_before_json['status']

assert status_value == "Job is NOT ready", "Unexpected status"
print("Wait for", time_value, "seconds")


"""Запрос ПОСЛЕ того, как задача готова"""
time.sleep(time_value)

payload = {'token': token_value}
send_token_after = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
send_token_after_json = json.loads(send_token_after.text)

status_value = send_token_after_json['status']
result_value = send_token_after_json['result']

assert status_value == "Job is ready", "Unexpected status"
if result_value is not None:
    print("Result =", result_value)


