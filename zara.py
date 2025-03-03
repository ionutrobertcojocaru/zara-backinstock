import requests
import json
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
email_user = "youremail_1@gmail.com"
email_password = "pass"
email_to = "youremail_2@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# List of URLs to check
urls = [
     "https://www.zara.com/itxrest/1/catalog/store/10704/product/id/312313470/availability"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://www.zara.com/"
}

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, email_to, text)
        server.quit()
        print(f"Email sent successfully to {email_to}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_availability(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for sku_info in data.get('skusAvailability', []):
            sku = sku_info.get('sku')
            availability = sku_info.get('availability')
            if availability == "in_stock" or availability == "low_on_stock":
                print(f"SKU {sku} is in stock.")
                subject = f"Product SKU {sku} is in stock"
                body = f"The product with SKU {sku} is now in stock. Check it out here: {url}"
                send_email(subject, body)
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

while(True):
    for url in urls:
        check_availability(url)
    time.sleep(1800)

