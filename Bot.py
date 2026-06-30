import requests
import smtplib
import time
from email.mime.text import MIMEText

sender_email = "shaybibk969@gmail.com"
app_password = "tprvwpoyqzdzbplg"
receiver_email = "shaybibk969@gmail.com"

def check_and_alert():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
    price = response['bitcoin']['usd']

    if price < 60000:
        signal = "BUY karo! Price kam hai!"
    else:
        signal = "SELL karo! Price zyada hai!"

    msg = MIMEText(f"Bitcoin Price: {price} USD\nSignal: {signal}")
    msg['Subject'] = "Trading Bot Signal"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print(f"[{time.strftime('%H:%M:%S')}] Price: {price} USD | Signal: {signal} | Email sent!")

while True:
    check_and_alert()
    time.sleep(300)
