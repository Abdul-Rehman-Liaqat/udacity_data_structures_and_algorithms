"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

numbers_sending_texts = set()

for text in texts:
    numbers_sending_texts.add(text[0])
    numbers_sending_texts.add(text[1])

call_from_set = set()
call_to_set = set()

for call in calls:
    call_from_set.add(call[0])
    call_to_set.add(call[1])

possible_telemarketer = set()
for phone_number in call_from_set:
    if phone_number not in call_to_set and phone_number not in numbers_sending_texts:
        possible_telemarketer.add(phone_number)

print(
    "These numbers could be telemarketers:\n{}".format(
        "\n".join(sorted(list(possible_telemarketer)))
    )
)
