# import random
# import string
# def main():
#     while True:
#         try:
#             user = int(input("Give us the length of the password: "))
#             print(pass_gen(user))
#             break
#         except:
#             pass

# def pass_gen(length):
#     all_chars = string.ascii_letters + string.digits + string.punctuation
#     password = "".join(random.choices(all_chars, k=length))
#     return password

# if __name__=="__main__":
#     main()
#===================================================================
# import itertools

# counter = itertools.count(start = 1, step = 3)
# number_list = [next(counter) for _ in range(5)]

# sequence = ["A","B","C","D"]
# cycle_sequence = itertools.cycle(sequence)
# cycle_list = [next(cycle_sequence) for _ in range(10)]
# combination = list(itertools.combinations_with_replacement(sequence,2))
# combination2 = list(itertools.combinations(sequence,2))

# print(combination)
# print(combination2)
#===================================================================
# import itertools

# data1 = ["A","B","C"]
# data2 = [1, 2, 3]

# combination = list(itertools.product(data1, data2))
# permit = list(itertools.permutations(data1))
# print(combination)
# print(permit)
#===================================================================
# import datetime

# def main():
#     event_date = [datetime.date.today()+datetime.timedelta(days=i) for i in range(5)]
#     time_slots = ["9:00 AM - 12:00 PM", "1:00 PM - 4:00 PM", "5:00 PM - 8:00 PM"]
#     for ev_date in event_date:
#         print(f"Event Date {ev_date.strftime('%d-%m-%Y')}")
#         for time in time_slots:
#             valantiors = input("Give us the names: ")
#             if valantiors:
#                 print(f"Volunteers for this slot: {valantiors}")

# main()
#===================================================================
# import datetime
# import pytz

# def main():
#     event_name = input("Enter event name: ")
#     start_date = input("Enter event start date (YYYY-MM-DD): ")
#     start_time = input("Enter event start time (HH:MM): ")
#     event_timezone = input("Enter event timezone (e.g., 'America/New_York'): ")

#     event_time = datetime.datetime.strptime(start_date + " " + start_time, "%Y-%m-%d %H:%M")

#     event_time_local = convert_to_local_time(event_time, event_timezone)

#     print(event_time_local)

# def convert_to_local_time(event_time, timezone):
#     event_time_utc = event_time.astimezone(pytz.utc)
#     local_time_zone = pytz.timezone(timezone)
#     return event_time_utc.astimezone(local_time_zone)

# main()
#===================================================================

# import datetime


# def main():
#     project_name = input("Enter the project name: ")
#     tasks = []
#     while True:
#         task_name = input("Enter the Task (or 'stop' to finish): ")

#         if task_name.lower() =="stop":
#             break
#         deadline = int(input("Enter the deadline: "))
#         tasks.append(schedule_task(task_name,deadline))
#     print(tasks)
#     for task in tasks:
#         track_task_progress(task[0], task[1].toordinal() - datetime.date.today().toordinal())


# def schedule_task(task_name, days_until_deadline):
#     today = datetime.date.today()
#     deadline = today + datetime.timedelta(days=days_until_deadline)
#     return task_name, deadline

# def track_task_progress(task_name, days_until_deadline):
#     total_days = days_until_deadline
#     remaining_days = total_days

#     while remaining_days >= 0:
#         progress = 100 - (remaining_days / total_days * 100)
#         print(f"Task: {task_name}, Progress: {progress:.2f}%")
#         remaining_days -= 1
# main()
