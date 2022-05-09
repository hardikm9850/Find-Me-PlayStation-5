from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime
import threading

class handler(BaseHTTPRequestHandler):


  def checkTime():
    # This function runs periodically every 1 second
    threading.Timer(1, checkTime).start()

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

    if "name" in dic:
      message = "Hello, " + dic["name"] + "!"
    else:
      message = "Hello, stranger!"

    self.wfile.write(message.encode())
    checkTime()
    return
