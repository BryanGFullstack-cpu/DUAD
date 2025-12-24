#Exercise 2  b week 6
the_change = 100

def change_value():
  global the_change
  the_change = 200
  print("inside", the_change)


change_value() 


print("outside", the_change)
print("got it :)")