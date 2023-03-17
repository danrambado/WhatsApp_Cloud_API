import smtplib, ssl

# Set up the SMTP server
smtp_server = 'webmail.alexanderfleming.org'
smtp_port = 587
smtp_username = 'drambado'
smtp_password = 'Ingreso0223'

# Set up the email message
from_addr = 'drambado@alexanderfleming.org'
to_addr = 'danrambado.dev@gmail.com'
subject = 'Test email'
body = 'This is a test email sent from Python.'

# Create the email message
msg = f'To: {to_addr}\nFrom: {from_addr}\nSubject: {subject}\n\n{body}'
print(msg)

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    result = server.sendmail(from_addr, to_addr, msg)
    print(result)

# Check if the email was sent
if not result:
    print(f'Email sent successfully!{result}')
else:
    print(f'Email not sent. Error: {result}')
