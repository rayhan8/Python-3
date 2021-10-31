# syntax : [start : stop : step]

my_string = "abcdefghijk"

print(my_string[::])
# print from beginning to end

print(my_string[::2])
# here step size is 2
# print beginning to end by jumping 2 steps

print(my_string[::3])
# here step size is 3
# print beginning to end by jumping 3 steps

print(my_string[2:9:2])
# 2 is starting point
# 9 is stop point
# 2 is step size
# print index position 2 up to index position 9(not included index 9) by jumping 2 steps

print(my_string[::-1])
# here step size is -1
# print end to beginning because step size is -1
# Trick : String Reverse Technique
