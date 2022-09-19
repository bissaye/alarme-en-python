import os
import time
import datetime
import playsound


__all__ = ['StartAlarm']

def StartAlarm(timeInput, SoundPath):

    TransTime = timeInput.split(":")

    if len(TransTime) != 2 :
        raise "error"

    TransTime[0] = abs(int(TransTime[0]))
    TransTime[1] = abs(int(TransTime[1]))

    if TransTime[0] > 23:
        raise "error"

    if TransTime[0] > 59:
        raise "error"


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Alarm programmed for: {timeInput}\n")
        print(f'current time: {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}')
        if TransTime[0] == datetime.datetime.now().hour and TransTime[1] == datetime.datetime.now().minute :
            print("c'est l'heure")
            playsound.playsound(sound=SoundPath, block=True)
            break
        time.sleep(1)



