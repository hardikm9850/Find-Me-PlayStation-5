import requests
import Config


url = "https://us.sms.api.sinch.com/xms/v1/" + Config.sms_service_plan_id + "/batches"

def send_sms(body):
  payload = {
  "from": Config.from_mobile_number,
  "to": [
    Config.to_mobile_number
  ],
  "body": body
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer fdd83a949e9f4e6aaac59f79f04c46bd"
  }

  response = requests.post(url, json=payload, headers=headers)

  data = response.json()
  print(data)
