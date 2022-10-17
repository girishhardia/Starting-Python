saly = int(input("Please Enter Your Salary "))
wyr = int(input("Please Enter Your Working Years In Our Company "))

if wyr >= 10 :
    print("Your net bonous will be " , 10*saly/100 )
    print("Your total salary will be " , saly+(10*saly/100))

elif wyr >= 6 :
     print("Your net bonous will be " , 8*saly/100 )
     print("Your total salary will be " , saly+(8*saly/100))

else :
    print("Your net bonous will be " , 5*saly/100 )
    print("Your total salary will be " , saly+(5*saly/100))

  