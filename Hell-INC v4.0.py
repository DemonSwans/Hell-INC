import os
import numpy as np
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


path= os.getcwd() + "\Data"
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
server.login("swansytest","Testpass!2")
ex = np.array(np.loadtxt(os.getcwd()+"\Bases\ext.npy", dtype=str))
ma = np.array(np.loadtxt(os.getcwd()+"\Bases\mail.npy", dtype=str))
nma = 0
for kj in ex:
    roz = np.array([])
    exclude = set(['Bases'])
    for r, dirs, f in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in f:
            if kj in file:
                roz=np.append(roz,os.path.join(r, file))

    for f in roz:
        print(f)
        
    msg = MIMEMultipart()
    msg['From'] = "swansytest@gmail.com"
    msg['To'] = ma[nma]
    msg['Subject'] = "Pliki" + kj
    body = " "
    msg.attach(MIMEText(body, 'plain'))
    pakiet = 0
    nup = 0
    i=0
    al = 0
    usu = np.array([])
    for f in roz:
        i=i+1
        al = al +1
        file_path = f
        pakiet = pakiet + 1
        nazwap = str(i) + kj
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename= nazwap)
        msg.attach(attachment)
        usu = np.append(usu,f)
        if pakiet == 4:
            text = msg.as_string()
            server.sendmail("swansytest@gmail.com", ma[nma], text)
            print("Wysłano " + str(nup+1))
            del msg['From']
            del msg['To']
            del msg['Subject']
            del msg
            del text
            msg = MIMEMultipart()
            msg['From'] = "swansytest@gmail.com"
            msg['To'] = ma[nma]
            msg['Subject'] = "Pliki" + kj
            body = " "
            msg.attach(MIMEText(body, 'plain'))
            pakiet = 0
            nup = nup+1
            al = 0
            for j in usu:
                os.remove(j)
            del usu
            usu = np.array([])
            
    if al<4 and al != 0:
        text = msg.as_string()
        server.sendmail("swansytest@gmail.com", ma[nma], text)
        print("Wysłano Reszte")
        for j in usu:
                os.remove(j)
        del usu
        usu = np.array([])
    del msg['From']
    del msg['To']
    del msg['Subject']
    del msg
    text = 0
    del text
    if i > 0:
        print("Pliki" + kj + " zostały wysłane")
    else:
        print("Nie było nic do wysłania z Plików" + kj)
    if i > 0:
        print("Pliki" + kj + " zostały usunięte")
    else:
        print("Nie było nic do usuwania z Plików" + kj)
    nma= nma + 1
    del usu
del roz
server.quit()