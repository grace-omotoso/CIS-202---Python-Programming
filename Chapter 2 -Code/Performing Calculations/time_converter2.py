number_of_secs = int(input('Enter the number of seconds: '))
hr = number_of_secs//3600 # 3600 sec makes an hr
hr_rem = number_of_secs%3600
mins = hr_rem//60 # 60 sec make a minute
secs = hr_rem%60
print(number_of_secs,'seconds is equal to', hr,'hours,',mins,'minutes',secs,'seconds')
