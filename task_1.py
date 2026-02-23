time = '1h 45m,360s,25m,30m 120s,2h 60s'
summ = 0
time_replace = time.replace(' ',',')
time_split = time_replace.split(',')

for i in time_split:
    if 'h' in i:
        time_hours = i.split('h')
        summ += int(time_hours[0]) * 60
    elif 'm' in i:
        time_minutes = i.split('m')
        summ += int(time_minutes[0])
    else:
        time_seconds = i.split('s')
        summ += int(time_seconds[0]) // 60

print(summ)