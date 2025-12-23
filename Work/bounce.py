# bounce.py
#
# Exercise 1.5
initial_height = 100
height = initial_height
for i in range(1,11):
    height *= (3 / 5)
    print(i, round(height, 4))
