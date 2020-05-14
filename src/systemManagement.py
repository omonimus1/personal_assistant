import os
import pyttsx3  # Text-to-Speech
import psutil   # Hardware Management


engine = pyttsx3.init()

# Provide battery percent and state: Plugged and Unplugged
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


def turn_off_device():
    shut_down_message = 'Shutting down the device'
    print(shut_down_message) 
    engine.say(shut_down_message)
    os.system("systemctl poweroff")


def reboot_device():
    reboot_message = 'I am rebooting the system'
    print(reboot_message)
    engine.say(reboot_message)
    os.system("shutdown /r /t 1")



