import requests, json
from random import *
from datetime import datetime
import time
import threading

class AsyncTask:
  def __init__(self):
        pass

  def termTest(self):
    now = datetime.now()
    pi_id = 2017277432
    T = uniform(34, 48) # float
    V = uniform(11, 14) # float

    date = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    location = "desert"
    print(now.timezone)
    print(now.tzinfo)   

    test = { "id": pi_id, "temperature": T, "voltage": V, "date": date, "location": location }
    test_json = json.dumps(test)
    print(test_json)
    URL = "" # Put your url
    res = requests.post(URL, data=test)

    print("Send at " + date)
    time = threading.Timer(30, self.termTest)
    time.start()

def main():
  at = AsyncTask()
  at.termTest()

if __name__ == '__main__':
  main()
