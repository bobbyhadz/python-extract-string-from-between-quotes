# Extract strings between quotes in Python

import re

my_str = 'Bobby "Hadz" Com "ABC"'

my_list = re.findall(r'"([^"]*)"', my_str)

print(my_list)  # 👉️ ['Hadz', 'ABC']
print(my_list[0])  # 👉️ Hadz
print(my_list[1])  # 👉️ ABC