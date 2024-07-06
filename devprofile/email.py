import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password_or_app_password')
    print("Connected successfully!")
    server.quit()
except Exception as e:
    print(f"Failed to connect: {e}")
