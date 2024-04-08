from flask import Flask, request
import smtplib

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = "SrinjoyChatterjee2002@outlook.com"
    TO_EMAIL = request.args.get('to_email')
    PASSWORD = "Srinjoy#12345"

    # Extract first name and last name from the request
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    # Construct email message
    subject = "Test Mail"
    message_body = f"""\
    Subject: Customer account creation\n\n
    Create account using the below information:\n
    Link: https://sherlock-002-customer.apigee.io/\n
    First Name: {first_name}\n
    Last Name: {last_name}\n
    Email: {TO_EMAIL}\n
    """

    smtp = smtplib.SMTP(HOST, PORT)
    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, message_body)
    smtp.quit()

    return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)
