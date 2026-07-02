import requests
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "shaybibk969@gmail.com"
app_password = "tprvwpoyqzdzbplg"
receiver_email = "shaybibk969@gmail.com"

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent!")
    except Exception as e:
        print(f"Email error: {e}")

def check_and_alert():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
    price = response['bitcoin']['usd']

    if price < 60000:
        signal = "BUY karo! Price kam hai!"
    else:
        signal = "SELL karo! Price zyada hai!"

    print(f"[{time.strftime('%H:%M:%S')}] Bitcoin: {price} USD | {signal}")
    send_email(f"Trading Signal: {signal}", f"Bitcoin Price: {price} USD\nSignal: {signal}")

while True:
    check_and_alert()
    time.sleep(300)
