import sys 
import random
number = raw_input("Enter the upper limit for the FizzBuzz Game: ")
if len(number) < 1:
  number = random.randrange(1,300)
  print "You didn't supply a number, so we picked one for you! -- We picked ", number
number = int(number)
startnum = 1
li = []
while startnum <= number:
  
  current_num = startnum
  replace = ""
  if current_num%3 == 0:
    replace = "Fizz"
  if current_num%5 == 0:
    replace = "Buzz"
  if current_num%5  == 0 and current_num %3 == 0:
    replace = "FizzBuzz"
    
  if replace == "":
    li.append(str(current_num))
  if replace != "":
    li.append(replace)
  startnum = startnum + 1
  
print "Fizz Buzz counting up to ", number

for n in range(0,number):
  print li[n]
