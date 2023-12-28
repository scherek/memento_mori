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

sex = None
country = None
sleep = 8 * hour
work_day = 8 * hour * 5 / 7
retirement_age = birth_date + 65 * year
#print(datetime.datetime.fromtimestamp(retirement_age))

life_expectancy = 75 * year
retirement_time = life_expectancy - retirement_age

passed_time = current_time - birth_date
print("Years passed: " + str(passed_time/year) )

left_time = 75 * year - passed_time
print("Years left: " + str(left_time/year) )

sleep_time = sleep * left_time / day
work_time = work_day * (retirement_age - passed_time) / day

free_time = left_time - sleep_time - work_time
print("Free time left: " + str(free_time/year) + " years" )
