import datetime;
import time

print("Memento Mori Clock")

minute = 60
hour = minute * 60
day = 24 * hour
week = 7 * day
month = day * 365.25 / 12
year = month * 12

current_time = datetime.datetime.now().timestamp()
birth_date = input("Format: dd/mm/yyyy\nEnter birthdate: ") 
birth_date = time.mktime(datetime.datetime.strptime(birth_date,"%d/%m/%Y").timetuple())

sleep = 8 * hour
work_day = 8 * hour * 5 / 7
retirement_age = birth_date + 65 * year
#print(datetime.datetime.fromtimestamp(retirement_age))

life_expectancy = 75 * year
retirement_time = life_expectancy - retirement_age

country = input("Enter your country to calculate life expectancy: ")

sex = input("Enter your sex to calculate life expectancy (m/f): ") 
while(sex != 'm' and sex != 'M' and sex != 'f' and sex != 'F'):
    sex = input(f"Unrecognized value {sex}.\nEnter your sex to calculate life expectancy (m/f): ") 


other_time = {}
other_i = input('\nFormat: Sleep, 8*60*60\nEnter name of another activity, and time it takes per day after a comma (q to quit): ')
while other_i != 'q':
    comma = other_i.find(',')
    other_time[f"{other_i[0:comma]}"] = eval(other_i[comma+1::])
    other_i = input('\nFormat: Sleep, 8*60*60\nEnter name of another activity, and time it takes per day after a comma (q to quit): ')

print(other_time)

passed_time = current_time - birth_date
print("Years passed: %.2f" % (passed_time/year))

left_time = 75 * year - passed_time
print("Years left: %.2f" % (left_time/year))

other_time = sum(other_time.values())
other_time = 365.25 * other_time * left_time / year

sleep_time = sleep * left_time / day
work_time = work_day * (retirement_age - passed_time) / day

free_time = left_time - sleep_time - work_time - other_time
print("Free time left: %.2f" % (free_time/year) + " years or %.2f hours per day" % (free_time/hour / (left_time/year * 365.25)) )