from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime
import threading

import os
from dotenv import load_dotenv

load_dotenv()

to_mobile_number = os.getenv('to_mobile_number')

class handler(BaseHTTPRequestHandler):
  
    def checkTime(self):
      # This function runs periodically every 1 second
      threading.Timer(1, self.checkTime).start()
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      print("Current Time =", current_time)
      if(current_time == '07:00:00'):  # check if matches with the desired time
          print('checking tweets')
          FindTweets.get_tweets()
      return

    def do_GET(self):
      s = self.path
      dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
      self.send_response(200)
      self.send_header('Content-type','text/plain')
      self.end_headers()
      
      message = "Ab to PS5 Milna hi chahiye Lol "+to_mobile_number
      print("mobile number ",to_mobile_number)
      self.wfile.write(message.encode())
      self.checkTime()
      return
