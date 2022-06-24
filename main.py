import smtplib                                              # Импортируем библиотеку по работе с SMTP
import os                                                   # Функции для работы с операционной системой, не зависящие от используемой операционной системы
import random
# Добавляем необходимые подклассы - MIME-типы
import mimetypes    # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from random import randint
from email import encoders                                  # Импортируем энкодер
from email.mime.base import MIMEBase                        # Общий тип
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.image import MIMEImage                      # Изображения
from email.mime.audio import MIMEAudio                      # Аудио
from email.mime.multipart import MIMEMultipart              # Многокомпонентный объект
import numpy as np
import time
addr_from = "------------------"
addr_to = "------------"
password = "-------"  # пароль от почты addr_from

def send_email(addr_to, msg_subj, msg_text, files,addr_from,password,servers,ports):
    

    msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From']    = addr_from                              # Адресат
    msg['To']      = addr_to                                # Получатель
    msg['Subject'] = msg_subj                               # Тема сообщения

    body = msg_text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст

                        # Добавляем в сообщение текст

    process_attachement(msg, files)

    
    server = smtplib.SMTP_SSL(servers, ports)               # Создаем объект SMTP
    #server.starttls()                                      # Начинаем шифрованный обмен по TLS
    #server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg)                                # Отправляем сообщение
    server.quit()                                           # Выходим
    #==========================================================================================================================
def process_attachement(msg, files):                        # Функция по обработке списка, добавляемых к сообщению файлов
    for f in files:
        if os.path.isfile(f):                               # Если файл существует
            attach_file(msg,f)                              # Добавляем файл к сообщению
        elif os.path.exists(f):                             # Если путь не файл и существует, значит - папка
            dir = os.listdir(f)                             # Получаем список файлов в папке
            for file in dir:                                # Перебираем все файлы и...
                attach_file(msg,f+"/"+file)                 # ...добавляем каждый файл к сообщению

def attach_file(msg, filepath):                             # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)                   # Получаем только имя файла
    ctype, encoding = mimetypes.guess_type(filepath)        # Определяем тип файла на основе его расширения
    if ctype is None or encoding is not None:               # Если тип файла не определяется
        ctype = 'application/octet-stream'                  # Будем использовать общий тип
    maintype, subtype = ctype.split('/', 1)                 # Получаем тип и подтип
    if maintype == 'text':                                  # Если текстовый файл
        with open(filepath) as fp:                          # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)    # Используем тип MIMEText
            fp.close()                                      # После использования файл обязательно нужно закрыть
    elif maintype == 'image':                               # Если изображение
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'audio':                               # Если аудио
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
    else:                                                   # Неизвестный тип файла
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)              # Используем общий MIME-тип
            file.set_payload(fp.read())                     # Добавляем содержимое общего типа (полезную нагрузку)
            fp.close()
            encoders.encode_base64(file)                    # Содержимое должно кодироваться как Base64
    file.add_header('Content-Disposition', 'attachment', filename=filename) # Добавляем заголовки
    msg.attach(file)                                        # Присоединяем файл к сообщению



# Использование функции send_email()
#addr_to   = "vadimovseev87@mail.ru"                                # Получатель
addr_to1   = ["vlad_ostanin1@mail.ru","vadimovseev87@mail.ru"]
files = ["Resume.pdf"]                                       # Если нужно отправить все файлы из заданной папки, нужно указать её
spis=[]

spis=[]
# чтение файла с почтами дял рассылок
with open("school.txt") as file_handler:
    for line in file_handler:
        x=line.replace('В', '')
        x=x.replace('\xa0', '')

        x=x.replace(' ', '')
        x=x.strip()
        x=x.split(";")
        for i in x:
            if "@" in i:
                spis+=[i]





fg=[".",","]
fals=["р","p"]
fals1=["o","о"]


#                    Рассылка с разных почт (анти спам/блок)     		             		     
poshts=["-------",  "----------", "----------",   "----------"] # почты ("test@mail.ru")
#	    |		|	      |		      |
passws=["----------","----------","----------",  '----------'] # пароли от почт ("qwerty")
#	    |           |              |              |
servers=["--------","------------","---------","------------"] #адрес почтового сервера ("smtp.yandex.ru")
#           |           |              |              |
ports= [--------,  ------------,  --------,    ------------]   #Порт(465)
files = ["file.docs"]

                                                        
hjk=0


for i in range(3,len(spis),4):
    poshts = [poshts[-1]] + poshts[:-1]
    passws=  [passws[-1]] + passws[:-1]
    servers= [servers[-1]] + servers[:-1]
    ports=   [ports[-1]] + ports[:-1]
    print(poshts)
    print(passws)
    try:
        x=randint(0, 1)
	c=randint(0, 1)
	d=randint(0, 1)
	e=randint(0, 1)
        time.sleep(randint(10, 50))
        pismo = f"""Уважаемый Ф.И.О.\nМеня зовут Ф.И.О..М{fals1[x]}я компания __ занимается поставкой компьюте{fals[e]}ов и комплектующих и п{fals[c]}ограммного {fals1[x]}беспечения с ______года
		 \nМы п{fals[e]}одаем компьюте{fals[x]}ы известных мировых б{fals[x]}ендов _____________ Сот{fals[d]}удничая с нами, вы получите самое современное и качественное 
		 обо{fals[c]}удование в ко{fals[e]}откие сроки. Поставки осуществляем за один день — для товаров с{fals1[c]} склада и до нескольких дней — для товаров под заказ.
		 \nМы заинтересованы в д{fals1[e]}лг{fals1[d]}срочном взаимовыгодном партнерстве и готовы представить Вашему вниманию низкие цены и высокое качество обслуживания.
	         \nБуду рад сот{fals[d]}удничать, жду Ваш {fals[x]}твет в ближайшее время. \n\n\nРук{fals1[e]}водитель ______________."""
        print(spis[i-3])
        hjk += 1


        print(hjk,"Отправлено",spis[i-3],"кем",poshts[0] )
        send_email(spis[i - 3], "Резюме", pismo, files, poshts[0], passws[0],servers[0],ports[0])


        x = randint(0, 1)
        time.sleep(randint(15, 40))
        hjk += 1

        print(hjk, "Отправлено", spis[i-2], "кем", poshts[1])
        send_email(spis[i - 2], "Резюме", pismo, files, poshts[1], passws[1],servers[1],ports[1])

        x = randint(0, 1)
        time.sleep(randint(15, 50))
        hjk += 1

        print(hjk, "Отправлено", spis[i-1], "кем", poshts[2])
        send_email(spis[i - 1], "Резюме", pismo, files, poshts[2], passws[2],servers[2],ports[2])

        x = randint(0, 1)
        time.sleep(randint(15, 50))
        hjk += 1

        print(hjk, "Отправлено", spis[i], "кем", poshts[3])
        send_email(spis[i], "Резюме", pismo, files, poshts[3], passws[3],servers[3],ports[3])
    except smtplib.SMTPRecipientsRefused as e:
        print(e)
        time.sleep(50)
    except smtplib.SMTPException as e:
        print(e)

    except smtplib.SMTPServerDisconnected as e:
        print(e)

    except KeyboardInterrupt:
        print("Остановка программы")

    except UnicodeEncodeError:
        print("Проверьте email, возможны русские символы")

    except:
        print('-' * 50)
        print("Прочие исключения")
        #67traceback.print_exc(limit=2, file=sys.stdout)
        print('-' * 50)
