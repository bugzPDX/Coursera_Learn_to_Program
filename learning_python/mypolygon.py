
#from TurtleWorld import *


#world = TurtleWorld()
#bob = Turtle()
#print(bob)
#def square(t,length):
#    for i in range(4):
#        fd(t,length)
#        lt(t)

#    wait_for_user()
#square(bob,125)



#def polygon(t,length,n):
#    for i in range(n):
#        fd(t,length)
#        lt(t,360/n)

#    wait_for_user()
    
#polygon(bob,55,8)


#def circle(t,r):
#    for i in range(n):
#        fd(t,length)
#        lt(t,360/n)

#    wait_for_user()
    
#circle(bob,5,160)



def get_values():
   prompt =  "Input a single digit number:\n"
   prompt2 = "Input a single digit number greater than 2:\n"
   v1 = input(prompt) 
   v2 = input(prompt)
   v3 = input(prompt)
   e1 = input(prompt2)
   return int(v1),int(v2),int(v3),int(e1)


def check_fermat(a,b,c,n):
        if n > 2 and a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")

def get_fermat():
    values = get_values()
    check_fermat(values[0],values[1],values[2],values[3])

def is_triangle(a,b,c):
    if a > (b+c) or b > (a+c) or c > (a+b):
        print("No")
    else:
        print("Yes")
        
is_triangle(3,4,9)

def input_number():
    return input("Enter a number:\n")
    
def set_triangle():
    s1 = input_number()
    s2 = input_number()
    s3 = input_number()
    return int(s1), int(s2), int(s3)
    
def get_triangle():
    values = set_triangle()
    is_triangle(values[0],values[1],values[2])
    
    
def compare(x,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1
        
import math       
def hypotenuse(l1,l2):
    return math.sqrt((l1**2)+(l2**2))
    
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2) 
    
def area(radius):
    return math.pi * radius**2
    
def circle_area(xc,yc,xp,yp):
    return area(distance(xc,yc,xp,yp))
                            
def is_between(x,y,z):
    return x<=y<=z
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m,n-1))
                                                                              
def first(word):
    return word[0]
    
def last(word):
    return word[-1]
    
def middle(word):
    return word[1:-1]
    
def is_palindrome(word):
     if len(word) == 0:
         return True
     if first(word) == last(word):
            is_palindrome(middle(word))

def back_word(word):
    index = len(word)
    while index > 0:
        letter = word[index-1]
        print letter
        index -= 1

def in_order():    
    prefixes = 'JKLMNOPQ'
    suffix1 = 'ack'
    suffix2 = 'uack'
    
    for l in prefixes:
        if l in 'JKLMNP':
            print l + suffix1
        else:
            print l + suffix2    

def find(word,letter,index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1 
    
def count(w,l):
     count = 0
     for char in w:
         if char == l:
             count += 1
     print count               
     
def count_letters(word):
    return word.count('a')
    
def is_a_palindrome(word):
    return word == word[::-1]

def rotate_word(word,num):
    
    for c in word:
        c = ord(c)
        rotated = c + int(num)
        converted = chr(rotated)
        print converted
        
def rotate_word2(word,num):
    for c in word:
        converted = chr(ord(c) + int(num))
        print(converted)

def count_vowels(word):
    count = 0
    vowels = 'aeiou'
    for char in word:
        if char in vowels:
            count += 1
    return count   

    
        
                
def guess_number():
    print "Please think of a number between 1 and 100!"
    high = 100
    low = 0
    
    while True:
        guess = low + (high - low)/2

        print "Is your secret number " + str(guess) + "?"   

        hint = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        
        if hint == 'h':
            high = guess
                        
        elif hint == 'l':
            low = guess
            
        elif hint == 'c':
           print "Game over. Your secret number was " + str(guess) 
            
        else:
            print 'Sorry, I did not understand your input'
s = "Some string containing bobobboboobobob"           
            
num = 0            
for char in s:
    if str('bob') in s:
        num += 1
    
    
         
numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs


curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest

                    
def cc_payment(balance,annualInterestRate,monthlyPaymentRate):
    
    month_int_rate = annualInterestRate/12
    min_month_pymt = 0 # monthlyPaymentRate * balance
    month_unpd_bal = 0 # balance - min_month_pymt
    current_bal    = 0 # month_unpd_bal + (month_int_rate * month_unpd_bal)
    total_pd       = 0
    
    month = 0
    
    
    while month < 12:
        min_month_pymt = monthlyPaymentRate * balance
        month_unpd_bal = balance - min_month_pymt
        current_bal    = month_unpd_bal + (month_int_rate * month_unpd_bal)
        balance = current_bal
        month += 1
        total_pd += min_month_pymt
            
        print "Month: " + str(month)
        print "Minimum monthly payment: " + str(round(min_month_pymt,2))
        print "Remaining balance: " + str(round(balance,2))
        
    print "Total paid: " + str(round(total_pd, 2))
    print "Remaining balance: " + str(round(balance,2))
    
    
def payoff(balance,annualInterestRate):
    
    
    month_int_rate = annualInterestRate/12
    lowest_pymt    = 0
    current_bal    = balance # month_unpd_bal + (month_int_rate * month_unpd_bal)
        
       
    while current_bal > 0:
        current_bal = balance
        lowest_pymt   += 10


        for month in range(12):
        
            month_unpd_bal = current_bal - lowest_pymt
            current_bal    = month_unpd_bal + (month_int_rate * month_unpd_bal)
            
            
    print "Lowest payment: " + str(int(lowest_pymt))
    
def payoff(balance,annualInterestRate):
    
    
    lowest_pymt    = 0
    current_bal    = balance # month_unpd_bal + (month_int_rate * month_unpd_bal)
        
       
    while current_bal > 0:
        lowest_pymt   += 10
        current_bal = get_annual_bal(balance, annualInterestRate, lowest_pymt)

    print "Lowest payment: " + str(int(lowest_pymt))
    
            
    
def get_annual_bal(balance,annualInterestRate,pymt):
    
    month_int_rate = annualInterestRate/12

    
    for month in range(12):
        
            month_unpd_bal = balance - pymt
            balance        = month_unpd_bal + (month_int_rate * month_unpd_bal)
    return balance


    
def bisect_payoff(balance,annualInterestRate):
    
    current_bal    = balance # month_unpd_bal + (month_int_rate * month_unpd_bal)
    mp_lower       = current_bal/12
    mp_upper       = get_annual_bal(balance,annualInterestRate,0)/12
    

       
    while True:
        
        lowest_pymt    = mp_lower + (mp_upper - mp_lower)/2
        current_bal    = get_annual_bal(balance,annualInterestRate,lowest_pymt)
        print "lowest payment: " + str(lowest_pymt) + "current balance: " + str(current_bal)
        print "upper: " + str(mp_upper) + "lower: " + str(mp_lower)
        
        if current_bal > 0 and mp_lower != lowest_pymt:
            mp_lower = lowest_pymt # too low
            
        elif current_bal < 0 and mp_upper != lowest_pymt:
            mp_upper = lowest_pymt # too high
        
        else:        
            print "Lowest payment: " + str(round(lowest_pymt,2))
            break
    
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
    
