import json
import os
import time

time.sleep(10)
os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

with open('tunnels.json') as data_file:    
    datajson = json.load(data_file)


msg = ""
for i in datajson['tunnels']:
  msg = msg + i['public_url']

os.system("curl -s --user 'api:[your api key here]' https://api.mailgun.net/v3/[your mailgun domain name here]/messages -F from='Ngrok Notifier <ngrok@[your mailgun domain name here]>' -F to=[your email address here] -F subject='Your Ngrok address' -F text='" + msg + "'")
