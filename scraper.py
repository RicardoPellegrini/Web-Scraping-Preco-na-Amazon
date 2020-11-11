import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Procurando pelo samsung S11 no site da Amazon
URL = 'https://www.amazon.com.br/Smartphone-Samsung-Android-Octa-Core-Traseira/dp/B07NZX5BKH/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=samsung+s11&qid=1605118011&sr=8-1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}

# Função para envio de e-mail
def send_mail():
  smtp_server = "smtp.gmail.com"
  port = 587  # starttls
  sender_email = "ricardo.pellegrini92@gmail.com"
  password = 'senha_ficticia'

  server = smtplib.SMTP(smtp_server, port)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(sender_email, password)
  
  subject = 'O preço do Samsung caiu!'
  body = f'O preço do celular caiu. Visite o link do celular para verificar o novo preço\nhttps://www.amazon.com.br/Smartphone-Samsung-Android-Octa-Core-Traseira/dp/B07NZX5BKH/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=samsung+s11&qid=1605118011&sr=8-1'

  message = f'Subject: {subject}\n\n{body}'

  server.sendmail(
    from_addr=sender_email,
    to_addrs=sender_email,
    msg=message,
    )

  print('E-mail enviado com sucesso!')
  server.quit() 

# Função principal para verificar o preço na Amazon
def check_price():
  page = requests.get(URL, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id='productTitle').text.strip()
  price = soup.find(id='priceblock_ourprice').text.strip()
  converted_price = float(price[2:].replace('.','').replace(',','.'))

  if converted_price > 3199.99:
    send_mail()

# Essa função vai verificar a cada 4 horas
while(True):
  check_price()
  time.sleep(14400)
