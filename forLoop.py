cars = ["Tata", "BMW", "Kia", "Ferrari", "Ford"]

for i in cars:
    print(i)

#continue skips the situation assigned
#break breaks the loop
str = "hello World"
for i in str:
    if i=="W":
        continue
    elif i=="r":
        break
    print(i)

cars = ["Tata", "BMW", "Kia", "Ferrari", "Ford"]
for i in cars:
    if i==cars[2]:
        continue
    print(i)

#nested for loops
color = ["Blue", "Green", "Red"]
for i in cars:
    for j in color:
        print(j, i)