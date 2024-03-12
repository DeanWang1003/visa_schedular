import sched
import time
from datetime import datetime
import csv

scheduler = sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)

class A():
    def __init__(self):
        self.x = 1
        
    def func(self):
        def b():
            self.x +=1
            if self.x == 3:
                return
            print(self.x+1)
            print("Task executed at", time.strftime("%H:%M:%S"))
        return b



def task(callable):
    scheduler.enter(5, 1, task, (callable,))
    callable()

now = datetime.now()
str= datetime.strftime(now,'%d %m %Y')
print(f"{str}")
user_data = []
# Open the CSV file for reading
with open("/root/autodl-tmp/visa_schedular/src/visa_users.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader, None)
    for row in csv_reader:
        user_data.append(row)
for data in user_data:
        email, password, user_expect_date_str = data[0], data[1], data[2]
        user_expect_date = datetime.strptime(user_expect_date_str, '%Y-%m-%d')
print(user_expect_date)              
print(user_expect_date_str) 