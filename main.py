import random

my_list = []

for _ in range(random.randint(3, 10)):
    my_list.append(random.randint(0, 5))
print(my_list)

new_other_list = [my_list[0], my_list[2], my_list[-2]]
print(new_other_list)