import requests
import Config


import os
from dotenv import load_dotenv

load_dotenv()

sms_service_plan_id = os.getenv('sms_service_plan_id')
from_mobile_number = os.getenv('from_mobile_number')
to_mobile_number = os.getenv('to_mobile_number')
sms_code = os.getenv('sms_code')


url = "https://us.sms.api.sinch.com/xms/v1/" + sms_service_plan_id + "/batches"

def send_sms(body):
  payload = {
  "from": from_mobile_number,
  "to": [
    to_mobile_number
  ],
  "body": body
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+sms_code
  }

  response = requests.post(url, json=payload, headers=headers)

  data = response.json()
  print(data)
