import time

currenttime = time.time()

secondsinday = 60 * 60 * 24

todaytotalseconds = currenttime%(secondsinday)
dayssinceepoch = currenttime/secondsinday

# Because UTC is 4 hours ahead of Boston time, we subtract by 4
todayhour = todaytotalseconds//(60 * 60) - 4
if todayhour < 0:
    todayhour = 24 + todayhour

todayminute = todaytotalseconds%(60 * 60)//60

todaysecond = todaytotalseconds%(60 * 60)%60

print('The time is currently {:02.0f}:{:02.0f}:{:02.0f}. It has been {:,.0f} days since the epoch.'.format(todayhour, todayminute, todaysecond, dayssinceepoch))