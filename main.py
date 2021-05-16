# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
print(add_time("6:30 PM", "205:12"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("3:00 PM", "3:10"))
print(add_time("11:43 PM", "24:20", "TueSday"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("3:30 PM", "2:12", "MoNday"))
print(add_time("2:59 AM", "24:00", "saturDay"))

# Run unit tests automatically
main(module='test_module', exit=False)