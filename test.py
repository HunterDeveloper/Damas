from datetime import  datetime, timedelta
time=str(datetime.now()+timedelta(hours=-5))[:-7]
print(time)