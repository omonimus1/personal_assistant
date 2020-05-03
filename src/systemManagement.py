import pyttsx3
import psutil  # https://github.com/giampaolo/psutil
import os
# Speech recognitionn with Google Speech Recognition API


engine = pyttsx3.init()

# Host device management
#def turn_off_device():
#    engine.say('Shutting down the device')
#    os.system("systemctl poweroff")


#def reboot_device():
#    engine.say('Alright, I am rebooting the system')
#    os.system("shutdown /r /t 1")


def get_battery_state():
    print('inside battery')
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if plugged is True:
        plugged_state = 'plugged'
    else:
        plugged_state = 'not plugged'

    battery_informations = 'The battery is at ' + str(percent) + ' and it is ' + plugged_state
    print(battery_informations)
    engine.say(battery_informations)
