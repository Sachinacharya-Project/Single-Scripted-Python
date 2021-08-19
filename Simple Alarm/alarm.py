import datefinder
import winsound
import datetime

def CallAlarm(name, text):
    alarmDate = datefinder.find_dates(text)
    for match in alarmDate:
        print(match)
    match_string = str(match)
    alarm_time = match_string[11:]
    alarm_hour = int(alarm_time[:-6])
    alarm_minutes = int(alarm_time[3:-3])
    alarm_seconds = int(alarm_time[6:])
    print(alarm_hour,alarm_minutes, alarm_seconds)

    while True:
        if alarm_hour == datetime.datetime.now().hour:
            if alarm_minutes == datetime.datetime.now().minute:
                print(f"Alarm Title: {name}")
                winsound.PlaySound('C:\\Users\\Dell\\Desktop\\Alarm\\alarm.m4a', winsound.SND_LOOP)
            elif alarm_minutes < int(datetime.datetime.now().minute):
                break

CallAlarm(input("Title: "), input("DateString: "))
