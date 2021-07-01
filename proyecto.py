import imaplib
import re

#datos
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)

count = 0

msgidFile = open("msg-id.txt", "w")
rcv1File = open("primerReceived.txt", "w")
rcv2File = open("penultimoReceived.txt", "w")
utcFile = open("utc.txt", "w")
fromFile = open("from.txt", "w")
correoFile = open("correo.txt", "w")

imap.login('correo', 'contraseña')
imap.select('Inbox')
typ, data = imap.search(None,'FROM', 'cody@codigofacilito.com')

msgidFile.write("Codigo Facilito")
rcv1File.write("Codigo Facilito")
rcv2File.write("Codigo Facilito")
utcFile.write("Codigo Facilito")
fromFile.write("Codigo Facilito")
correoFile.write("Codigo Facilito")

msgidFile.write("\n")
rcv1File.write("\n")
rcv2File.write("\n")
utcFile.write("\n")
fromFile.write("\n")
correoFile.write("\n")

for num in data[0].split():
    if count < 40:
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        msgId= data[0][1].decode()
        msgId=msgId.replace("Message-ID:", "")
        msgId=msgId.replace(">", "")
        msgId=msgId.replace("<", "")
        msgId=msgId.replace("Message-Id:", "")
        msgId=msgId.strip()
        print("MsgID: " + msgId)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
        recv= data[0][1].decode()
        recv= recv.strip()
        recv = recv.split("Received:")
        recv1= recv[1]
        recv2= recv[-2]
        recv1 = recv1.strip()
        recv2 = recv2.strip()
        print("Primer Received: " + recv1)
        print("Penúltimo Received: " + recv2)
        utc = recv1[-11:]
        print("UTC: " + utc)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
        txtfrom = data[0][1].decode()
        txtfrom = txtfrom.replace("From:", "")
        txtfrom = txtfrom.strip()
        correo = txtfrom[txtfrom.find("<"):]
        correo = correo.replace("<", "")
        correo = correo.replace(">", "")
        print("From: " + txtfrom)
        print("Correo: " + correo)
        count += 1
        print(count)
        msgidFile.write(msgId)
        rcv1File.write(recv1)
        rcv2File.write(recv2)
        utcFile.write(utc)
        fromFile.write(txtfrom)
        correoFile.write(correo)
        msgidFile.write("\n")
        rcv1File.write("\n")
        rcv2File.write("\n")
        utcFile.write("\n")
        fromFile.write("\n")
        correoFile.write("\n")

    else:
        break

typ, data = imap.search(None,'FROM', 'contacto@mail.somosmach.com')

msgidFile.write("MACH")
rcv1File.write("MACH")
rcv2File.write("MACH")
utcFile.write("MACH")
fromFile.write("MACH")
correoFile.write("MACH")

msgidFile.write("\n")
rcv1File.write("\n")
rcv2File.write("\n")
utcFile.write("\n")
fromFile.write("\n")
correoFile.write("\n")

for num in data[0].split():
    if count < 80:
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        msgId= data[0][1].decode()
        msgId=msgId.replace("Message-ID:", "")
        msgId=msgId.replace(">", "")
        msgId=msgId.replace("<", "")
        msgId=msgId.replace("Message-Id:", "")
        msgId=msgId.strip()
        print("MsgID: " + msgId)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
        recv= data[0][1].decode()
        recv= recv.strip()
        recv = recv.split("Received:")
        recv1= recv[1]
        recv2= recv[-2]
        recv1 = recv1.strip()
        recv2 = recv2.strip()
        print("Primer Received: " + recv1)
        print("Penúltimo Received: " + recv2)
        utc = recv1[-11:]
        print("UTC: " + utc)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
        txtfrom = data[0][1].decode()
        txtfrom = txtfrom.replace("From:", "")
        txtfrom = txtfrom.strip()
        correo = txtfrom[txtfrom.find("<"):]
        correo = correo.replace("<", "")
        correo = correo.replace(">", "")
        print("From: " + txtfrom)
        print("Correo: " + correo)
        count += 1
        print(count)
        msgidFile.write(msgId)
        rcv1File.write(recv1)
        rcv2File.write(recv2)
        utcFile.write(utc)
        fromFile.write(txtfrom)
        correoFile.write(correo)
        msgidFile.write("\n")
        rcv1File.write("\n")
        rcv2File.write("\n")
        utcFile.write("\n")
        fromFile.write("\n")
        correoFile.write("\n")
    else:
        break

typ, data = imap.search(None,'FROM', 'info@twitter.com')

msgidFile.write("Twitter")
rcv1File.write("Twitter")
rcv2File.write("Twitter")
utcFile.write("Twitter")
fromFile.write("Twitter")
correoFile.write("Twitter")

msgidFile.write("\n")
rcv1File.write("\n")
rcv2File.write("\n")
utcFile.write("\n")
fromFile.write("\n")
correoFile.write("\n")

for num in data[0].split():
    if count < 120:
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        msgId= data[0][1].decode()
        msgId=msgId.replace("Message-ID:", "")
        msgId=msgId.replace(">", "")
        msgId=msgId.replace("<", "")
        msgId=msgId.replace("Message-Id:", "")
        msgId=msgId.strip()
        print("MsgID: " + msgId)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
        recv= data[0][1].decode()
        recv= recv.strip()
        recv = recv.split("Received:")
        recv1= recv[1]
        recv2= recv[-2]
        recv1 = recv1.strip()
        recv2 = recv2.strip()
        print("Primer Received: " + recv1)
        print("Penúltimo Received: " + recv2)
        utc = recv1[-11:]
        print("UTC: " + utc)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
        txtfrom = data[0][1].decode()
        txtfrom = txtfrom.replace("From:", "")
        txtfrom = txtfrom.strip()
        correo = txtfrom[txtfrom.find("<"):]
        correo = correo.replace("<", "")
        correo = correo.replace(">", "")
        print("From: " + txtfrom)
        print("Correo: " + correo)
        count += 1
        print(count)
        msgidFile.write(msgId)
        rcv1File.write(recv1)
        rcv2File.write(recv2)
        utcFile.write(utc)
        fromFile.write(txtfrom)
        correoFile.write(correo)
        msgidFile.write("\n")
        rcv1File.write("\n")
        rcv2File.write("\n")
        utcFile.write("\n")
        fromFile.write("\n")
        correoFile.write("\n")
    else:
        break

typ, data = imap.search(None,'FROM', 'uber.chile@uber.com')

msgidFile.write("Uber")
rcv1File.write("Uber")
rcv2File.write("Uber")
utcFile.write("Uber")
fromFile.write("Uber")
correoFile.write("Uber")

msgidFile.write("\n")
rcv1File.write("\n")
rcv2File.write("\n")
utcFile.write("\n")
fromFile.write("\n")
correoFile.write("\n")

for num in data[0].split():
    if count < 160:
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        msgId= data[0][1].decode()
        msgId=msgId.replace("Message-ID:", "")
        msgId=msgId.replace(">", "")
        msgId=msgId.replace("<", "")
        msgId=msgId.replace("Message-Id:", "")
        msgId=msgId.strip()
        print("MsgID: " + msgId)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
        recv= data[0][1].decode()
        recv= recv.strip()
        recv = recv.split("Received:")
        recv1= recv[1]
        recv2= recv[-2]
        recv1 = recv1.strip()
        recv2 = recv2.strip()
        print("Primer Received: " + recv1)
        print("Penúltimo Received: " + recv2)
        utc = recv1[-11:]
        print("UTC: " + utc)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
        txtfrom = data[0][1].decode()
        txtfrom = txtfrom.replace("From:", "")
        txtfrom = txtfrom.strip()
        correo = txtfrom[txtfrom.find("<"):]
        correo = correo.replace("<", "")
        correo = correo.replace(">", "")
        print("From: " + txtfrom)
        print("Correo: " + correo)
        count += 1
        print(count)
        msgidFile.write(msgId)
        rcv1File.write(recv1)
        rcv2File.write(recv2)
        utcFile.write(utc)
        fromFile.write(txtfrom)
        correoFile.write(correo)
        msgidFile.write("\n")
        rcv1File.write("\n")
        rcv2File.write("\n")
        utcFile.write("\n")
        fromFile.write("\n")
        correoFile.write("\n")
    else:
        break

typ, data = imap.search(None,'FROM', 'paratodos@tenpo.cl')

msgidFile.write("Tenpo")
rcv1File.write("Tenpo")
rcv2File.write("Tenpo")
utcFile.write("Tenpo")
fromFile.write("Tenpo")
correoFile.write("Tenpo")

msgidFile.write("\n")
rcv1File.write("\n")
rcv2File.write("\n")
utcFile.write("\n")
fromFile.write("\n")
correoFile.write("\n")

for num in data[0].split():
    if count < 200:
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        msgId= data[0][1].decode()
        msgId=msgId.replace("Message-ID:", "")
        msgId=msgId.replace(">", "")
        msgId=msgId.replace("<", "")
        msgId=msgId.replace("Message-Id:", "")
        msgId=msgId.strip()
        print("MsgID: " + msgId)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
        recv= data[0][1].decode()
        recv= recv.strip()
        recv = recv.split("Received:")
        recv1= recv[1]
        recv2= recv[-2]
        recv1 = recv1.strip()
        recv2 = recv2.strip()
        print("Primer Received: " + recv1)
        print("Penúltimo Received: " + recv2)
        utc = recv1[-11:]
        print("UTC: " + utc)
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
        txtfrom = data[0][1].decode()
        txtfrom = txtfrom.replace("From:", "")
        txtfrom = txtfrom.strip()
        correo = txtfrom[txtfrom.find("<"):]
        correo = correo.replace("<", "")
        correo = correo.replace(">", "")
        print("From: " + txtfrom)
        print("Correo: " + correo)
        count += 1
        print(count)
        msgidFile.write(msgId)
        rcv1File.write(recv1)
        rcv2File.write(recv2)
        utcFile.write(utc)
        fromFile.write(txtfrom)
        correoFile.write(correo)
        msgidFile.write("\n")
        rcv1File.write("\n")
        rcv2File.write("\n")
        utcFile.write("\n")
        fromFile.write("\n")
        correoFile.write("\n")
    else:
        break

msgidFile.close()
rcv1File.close()
rcv2File.close()
utcFile.close()
fromFile.close()
correoFile.close()

imap.close()