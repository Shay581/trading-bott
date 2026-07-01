import requests
import time

def check_and_alert():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
    price = response['bitcoin']['usd']

    if price < 60000:
        signal = "BUY karo! Price kam hai!"
    else:
        signal = "SELL karo! Price zyada hai!"

    print(f"[{time.strftime('%H:%M:%S')}] Bitcoin: {price} USD | {signal}")

while True:
    check_and_alert()
    time.sleep(300)
