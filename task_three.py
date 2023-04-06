# Create a class called TimeUtils that has a static method called time_to_seconds that takes 
# a time string in the format hh:mm:ss and returns the total number of seconds represented by that time. 
# Use functional programing paradigm.


import datetime

class TimeUtils:

    @staticmethod
    def time_to_seconds(time: str) -> float:
        time.split(":")

print(TimeUtils.time_to_seconds(time= 12:22:34))
# x = TimeUtils()
# print(x.get_time())

# print(TimeUtils.time_to_seconds)

# # print(datetime.datetime.now().time())