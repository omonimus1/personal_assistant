# Host device management
def turn_off_device():
    engine.say('Shutting down the device')
    os.system("shutdown /s /t 1")


def reboot_device():
    engine.say('Alright, I am rebooting the system')
    os.system("shutdown /r /t 1")

def get_battery_state():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if plugged is True:
        plugged_state = 'is plugged'
    else:
        plugged_state = 'is not plugged'

    battery_informations = 'The battery is at ' str(percent) + ' and the battery is ' plugged_state
    print(battery_informations)
    engine.say(battery_informations)
