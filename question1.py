salary = int(input("Please Enter Your Mounthly Salary :- "))
serviceTime = int(input("Please Enter time of service given by you till date in years :- "))
if serviceTime > 5:
    print("You are eligible for bonous of Rs 1000. Your net salary this month will be :- " , salary + 1000)
else:
    print("You are not eligible for bonous. Your net salary this month will be :- " , salary)

