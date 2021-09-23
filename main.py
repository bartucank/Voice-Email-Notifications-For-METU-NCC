from itertools import chain
import email
import imaplib
from gtts import gTTS
import random
import playsound
import time

#imap server login details
imap_ssl_host = 'imap.metu.edu.tr' #I did this project because I was waiting for an email from my university about the transfer.
imap_ssl_port = 993               # However, you can adapt it to your project by changing the IMAP server.
password = 'your_pass.'
user = 'your_username'
#imap server login details

#for voice
def talk(textt):
    tts = gTTS(text = textt, lang= "en")
    file = str(random.randint(0,1000000000000000000000)) + ".mp3"
    tts.save(file)
    playsound.playsound(file)
#for voice

check_mail = 0
def search_mail(check_mail):
    c =  [('UID', '%d:*' % (check_mail + 1))]
    return '(%s)' % ' '.join(chain(*c))

def receive_mail(msg):
    mail_content = msg.get_content_mainmail_content()

    if mail_content == 'multipart':
        return part.get_payload()
    elif mail_content == 'text':
        return msg.get_payload()

server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
server.login(user, password)
server.select('INBOX')
result, data = server.uid('search', None, search_mail(check_mail))
ch = [int(s) for s in data[0].split()]

if ch:
    check_mail = max(ch)
server.logout()

while 1:
    server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
    server.login(user, password)
    server.select('INBOX')
    result, data = server.uid('search', None, search_mail(check_mail ))
    ch = [int(s) for s in data[0].split()]
    for c in ch:
        if c > check_mail:
            talk("A new email has arrived to the METU email account!")
            check_mail = c
    server.logout()
    time.sleep(1)








