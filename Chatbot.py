from selenium import webdriver
import time
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from selenium.webdriver.common.keys import Keys
import sys
import sqlite3

con=sqlite3.connect("Whatsapp.db")
cursor=con.cursor()

def tabloustur():
        cursor.execute("CREATE TABLE IF NOT EXISTS Whatsapp(Numara TEXT,Durum TEXT)")
        con.commit()
def tikla():
    browser=webdriver.Firefox()
    browser.get("https://web.whatsapp.com/")
    ruslar=list()
    kazaklar=list()

    for iter1 in range(int(rusminsayi.text()),int(rusmaxsayi.text())):
        ruslar.append("rus{}".format(iter1))
    for iter2 in range(int(kazakminsayi.text()),int(kazakmaxsayi.text())):
        kazaklar.append("kazak{}".format(iter2))
    ruslar.extend(kazaklar)
    #liste=("Poşet","452172145517")
    time.sleep(5)

    tabloustur()

    for iter in ruslar:

        try:
            time.sleep(5)
            user=browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
            user.send_keys(iter)
            time.sleep(2)
            user.send_keys(Keys.ENTER)
            time.sleep(5)

            mesajkutusu=browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            mesajkutusu.send_keys(mesajbox.text())
            buton3=browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]")
            buton3.click()
            print("{0} adlı kişiye mesaj gönderildi".format(iter))
            Durum='Gönderildi'
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").clear()
            time.sleep(5)
            browser.refresh()
            time.sleep(5)

            logfile=open("log.txt","a",encoding="utf-8")
            logfile.write("{0} Başarıyla Gönderildi".format(iter))
            logfile.close()


        except:
            print("{0} Adlı Kullanıcı Yok".format(iter))
            Durum="Gönderilmedi"
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").clear()
            #listbox.insertItem(iter,Durum)

            logfile=open("log.txt","a",encoding="utf-8")
            logfile.write("{0} Gönderilmedi".format(iter))
            logfile.close()
        cursor.execute("insert into Whatsapp values(?,?)",(iter,Durum))
        con.commit()
    """logfile=open("log.txt","a",encoding="utf-8")
    logfile.write("Başarıyla Tamamlandı")
    zaman=datetime.datetime.now()
    logfile.write(zaman)
    logfile.close()"""
app=QApplication(sys.argv)
pencere=QWidget()

rusmaxsayi=QLineEdit(pencere)
rusmaxsayi.resize(45,25)
rusmaxsayi.move(200,150)

rusminsayi=QLineEdit(pencere)
rusminsayi.resize(45,25)
rusminsayi.move(150,150)

rustext=QLabel(pencere)
rustext.setText("Rus sayısı:")
rustext.move(50,150)
rustext.setFont(QFont('Times font',10))

kazakmaxsayi=QLineEdit(pencere)
kazakmaxsayi.resize(45,25)
kazakmaxsayi.move(200,180)

kazakminsayi=QLineEdit(pencere)
kazakminsayi.resize(45,25)
kazakminsayi.move(150,180)

kazaktext=QLabel(pencere)
kazaktext.setText("Kazak sayısı:")
kazaktext.move(50,180)
kazaktext.setFont(QFont('Times font',10))


yazi=QLabel(pencere)
yazi.setText("Whatsapp Chatbot.")
yazi.setFont(QFont('Times font',20))
yazi.move(150,30)

pencere.setWindowTitle("Whatsapp Chatbot")

resim=QLabel(pencere)
resim.setPixmap(QPixmap("sola.jpg"))

listbox=QListWidget(pencere)
listbox.resize(150,180)
listbox.move(330,300)
pencere.setGeometry(100,100,500,500)

Uibuton=QPushButton(pencere)
Uibuton.setText("Gönder")
Uibuton.move(50,450)

label1=QLabel(pencere)
label1.setFont(QFont('Times font',10))
label1.setText("Gönderilecek Mesaj")
label1.move(50,265)

mesajbox=QLineEdit(pencere)
mesajbox.move(50,300)
mesajbox.resize(250,150)

"""listwidget = QListWidget(pencere)
rus=list()
for iter in range(0,100):
    rus.append("rus"+"{0}".format(iter))
rus.reverse()
"""
zaman=QLabel(pencere)
#now=QDate.currentDate()
gun 	  = datetime.datetime.now().strftime("%d");
ay 	      = datetime.datetime.now().strftime("%m");
yil 	  = datetime.datetime.now().strftime("%Y");
saat 	  = datetime.datetime.now().strftime("%H");
dakika	  = datetime.datetime.now().strftime("%M");
tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
zaman.setText(str(tarihsaat))
zaman.setFont(QFont('ariel',10))
zaman.move(350,25)

"""for iter in rus:
    listwidget.insertItem(1,iter)
listwidget.move(70,350)
"""
pencere.show()

Uibuton.clicked.connect(tikla)



sys.exit(app.exec_())










