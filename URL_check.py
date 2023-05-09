import requests
import smtplib
import time

# Set up email parameters
sender_email = "sender@email.com"
receiver_email = "receiver@email.com"
password = "sender_password"

# Set up URL to check
url = "https://www.example.com"

interval = 300 #5 minutes

while True:
    try:
        # Make request to URL
        response = requests.get(url)
        
        # Check if page is online
        if response.status_code == 200:
            # If page is online, send email and exit
            message = "Subject: Page is online!\n\nThe page {} is now online.".format(url)
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            break
        else:
            #print(f'webpage returned status code {response.status_code}.')
            time.sleep(interval)
    
    except Exception as e:
        #print(f'Error checking website: {e}')
        time.sleep(interval)
