a1 = "name" , "class"
a2 = "roll no" , 15
print(a2)
print(a1)
#list(can have different data type) and array(only have same data type) difference
#how to use
#in

quote = " A quick brown fox jumps over the lazy dog"

if "quick" in quote:
    print("no")
else:
    print("yes")

if "quick" not in quote:
    print("no")
else:
    print("yes")


#string slicing

print(quote[4:20])
print(quote[:20])
print(quote[4:])
#use - to strat from last
print(quote[-20])
print(quote[-30:-20])
#whtever is before the colen is included but after the colen is excluded

#upper & lower
print(quote.upper())
print(quote.lower())

#strip (remove spaces before and after the string)
print(quote)
print(quote.strip())

#replace
print(quote.replace("fox" , "bear"))
#(search python string methods on google)

#concatenation 
a = "Hello"
b = " World"
c = a + b
print(c)

#string format
age = 26
ageString = "I am {} year old"
print(ageString.format(age))

#string format multiple
a = 1
b = 2
c = 3
str = "a={}, b={}, c={}"
print(str.format(a,b,c))

#string format change sequence
str = "a={2}, b={0}, c={1}"
print(str.format(b,c,a))
