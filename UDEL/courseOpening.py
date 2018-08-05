from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

courseURLs = ['https://udapps.nss.udel.edu/CoursesSearch/courseInfo?&courseid=006823&offernum=1&term=2188&session=1&section=010',
            'https://udapps.nss.udel.edu/CoursesSearch/courseInfo?&courseid=303194&offernum=1&term=2188&session=1&section=010',
            'https://udapps.nss.udel.edu/CoursesSearch/courseInfo?&courseid=301147&offernum=1&term=2188&session=1&section=010']

def sendEmail(classTitle):
    MY_ADDRESS = 'email to send from'
    PASSWORD = 'your password'
    
    s = smtplib.SMTP(host='smtp.live.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()       # create a message

    msg['From']=MY_ADDRESS
    msg['To']='youremail@email.com'
    msg['Subject']="Open Seats in %s" % (classTitle)

    s.send_message(msg)
    del msg

    s.quit()
    print("Message sent: %s" % (classTitle))

for courseURL in courseURLs:

    page = urlopen(courseURL)
    html = soup(page, 'lxml')

    closed = html.findAll("div", {"id": "closed"})

    if not closed:
        classTitle = html.findAll("h2", {"class": "itwd-title"})[0].text
        sendEmail(classTitle)



