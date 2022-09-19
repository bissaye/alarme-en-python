import os
import sys
import getopt
import scripts

if __name__ == '__main__':
    TimeInput = ""
    SoundPath = ""
    opts, args = getopt.getopt(
        sys.argv[1:],
        'ht:p:',
        [
            'help',
            'time=',
            'path='
        ]
    )

    for opt , arg in opts:
        if opt in ('-h', '--help'):
            scripts.AllHelp()
        elif opt in ('-t', '--time'):
            TimeInput = arg
        elif opt in ('-p', '--path'):
            SoundPath = arg
        else:
            scripts.AllHelp()

    if (TimeInput != ""):
        if (os.path.exists(SoundPath)):
            scripts.StartAlarm(TimeInput, SoundPath)
        else:
            print("erreur, the sound's path doesn't exists")