import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
messages_array = json.loads(json_text)
message2 = messages_array['messages'][1]

print(message2['message'])