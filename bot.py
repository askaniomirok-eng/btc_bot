import requests, time
TOKEN="8467850094:AAHjyFRiCdfXJHQa3cBHyr6rn4nrGNWP6Qw"
CHAT_ID=7691056309
def get_price():
  return requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",timeout=20).json()['bitcoin']['usd']
while True:
  try:
    p=get_price()
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",data={"chat_id":CHAT_ID,"text":f"BTC: ${p:,.0f}"})
  except: pass
  time.sleep(3600)
