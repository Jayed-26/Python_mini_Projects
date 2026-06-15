# This code will generate pin from your entered name. using skip value.

name = (input("Enter your name :"))

autopin = name[1:5:2]
print("Your pin is =", autopin)

print("Did not like it?")
pin = (input("Enter your own pin :"))


if pin == "":  
   print ("Your pin is Auto Generated :", autopin)

else :  
    print("Your pin is :", pin)
