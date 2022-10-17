from datetime import datetime
name = "fouad mohammed"

new = name.split(" ",1)

print(new[0])

date = datetime.now()
newdate = str(date.year)+"/"+str(date.month)+"/"+str(date.day)

hour = date.hour

print(newdate)