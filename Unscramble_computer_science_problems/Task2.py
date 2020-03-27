"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_number_duration = dict()

for call in calls:
    telephone_number_duration[call[0]] = int(call[3]) + telephone_number_duration.get(
        call[0], 0
    )
    telephone_number_duration[call[1]] = int(call[3]) + telephone_number_duration.get(
        call[1], 0
    )


phone_number = list(telephone_number_duration.keys())[
    list(telephone_number_duration.values()).index(
        max(list(telephone_number_duration.values()))
    )
]

print(
    "{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.".format(
        telephone_number=phone_number,
        total_time=telephone_number_duration[phone_number],
    )
)
