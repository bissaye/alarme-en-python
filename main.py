#coding:utf-8
import os
import datetime
from playsound import playsound
import time

os.system("cls")
error =1
while error != 0:
    os.system("cls")
    error1 =0
    error2 =0
    alarmH = abs(int(input("heure de reveil ")))
    alarmM = abs(int(input("minute")))
    if  alarmH > 23:
        error1 = 1
        print("heure incorrecte")
        time.sleep(1)
    if alarmM > 59:
        error2 = 1
        print("minutes incorrecte")
        time.sleep(1)
    error = error1 + error2
os.system("cls")
print("declenchement de l'alarm a" , alarmH,":",alarmM)
while 1 == 1:
    os.system("cls")
    print(datetime.datetime.now().hour,":",datetime.datetime.now().minute,":",datetime.datetime.now().second)
    if (alarmH == datetime.datetime.now().hour  and  alarmM == datetime.datetime.now().minute):
        print("c'est l,heure")
        os.system("start panda.mp3")
        break
    time.sleep(1)