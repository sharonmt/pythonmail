# Python Challenge #3.1 - send email with attachment
# Using gmail smtp
# BONUS: Embed email tracker
# This attempt (3.1) uses HTML; to be able to embed the tracker

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Email (3.1) with attachment"
from_email = "<SENDER EMAIL ADDRESS>"
to_email = "<RECEIVER EMAIL ADDRESS>"
# password = input("Enter password: ")
password = input("Password: ")

# Multipart message and headers
message = MIMEMultipart()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

# Message as HTML
html = """\
<html>
  <body>
    <p>CONTENT OF EMAIL GOES HERE<br>
       CONTENT OF EMAIL GOES HERE<br>
        --sent from My Python Mail
        <p>
       <img src="https://pastepixel.com/image/6aDvY7W5QW4v3WtHT2r4.png?cstm_data=t3.1">
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
message.attach(part2)
# Add attachmen - file in the same directory as script
attachfile = "TextFile.md"

# Open attachment in binary mode
with open(attachfile, "rb") as attachment:
    # Add file as application/octet-stream
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add attachment
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {attachfile}"
)

message.attach(part)
text = message.as_string()

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(from_email, password)
    server.sendmail(from_email, to_email, text)

# HTML Email with attachment works
# Email tracker - Not the best of trackers, but it works!