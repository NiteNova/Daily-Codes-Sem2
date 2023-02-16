AlarmHour = int(input("Enter the hour: "))
AlarmMin = int(input("Enter the minutes: "))

def Alarm(AlarmHour, AlarmMin):
    if AlarmMin >= 40:
        AlarmMin - 40
    elif AlarmMin < 40 and AlarmHour > 0:
        AlarmHour -= 1
        SubTime = 40 - AlarmMin
    elif AlarmHour == 0 and AlarmMin < 40:
        AlarmHour = 23
        SubTime = 40 - AlarmMin
        
    print(AlarmHour, 60-SubTime)
    

if AlarmHour > 23 or AlarmMin > 59:
    print("Invalid number")
else:
    Alarm(AlarmHour, AlarmMin)

    
