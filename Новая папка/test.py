
#w1d4 classwork
#1)print(3*abs(-2))

#2)print(min(5,3))

#3)print(max(5,3))

#4)print(min(3,2,1), max(3,2,1)) 

#5)from math import*
#print(ceil(3.2))

#6)char = 'a'
#print(char.upper())

#7)import math
#print(int(math.sqrt(9)))

#8)from math import*
#print(floor(3.7))

#9)from math import*
#print(round(3.4))

#10)from math import*
#print(pow(2,3))

#11)from math import*
#print(floor(3.7), ceil(3.7), round(3.7))

#12)from math import*
#n = int(input())
#print(sqrt(abs(n)))

#15)from math import*
#n = float(input())
#print((abs(n)) , round(abs(n)))

#17)from math import*
#print(pow(min(2, 3, 1), 2))

#18)from math import*
#a = int(input())
#b = int(input())
#print(max(abs(a), abs(b)))

#19)char = input()
#if char.islower():
  #  print("yeah")
#else:
#    print("nah")

#20)from math import*
#a=int(input())
#b=int(input())
#c=int(input())
#print(max(abs(a), abs(b), abs(c)), min(abs(a), abs(b), abs(c)))


#w2d5 extratasks
#140)temp = float(input())
#if temp >= 37.5:
 #   print("Fever")
#elif 36.0 <= temp <= 37.4:
 #   print("Normal")
#elif 34.0 <= temp <= 35.9:
 #   print("Hypothermia")
#else:  
 #   print("Dangerous")


#141)a = int(input())
#b = int(input())
#n = abs(a) % 10
#m = abs(b) % 10
#if n == m:
 #   print("Same last digit")
#elif n > m:
 #   print("First is greater")
#else:
 #   print("Second is greater")


#142)a = float(input())
#b = float(input())
#c = float(input())

#if (a < b + c) and (b < a + c) and (c < a + b):
    
 #   if a == b == c:
  #      print("Equilateral")
   # elif a == b or b == c or a == c:
    #    print("Isosceles")
    #else:
     #   print("Scalene")
        
#else:
 #   print("Invalid triangle")



#143)s1 = float(input())
#S2 = float(input())

#S1 = s1 * 1000 / 60
#if S1 > S2:
 #   print("First is faster")
#elif S2 > S1:
 #   print("Second is faster")
#else:
 #   print("Equal speed")


#144)ab = int(input())
#if ab % 10 == 0:
 #   print("Invalid reversal")
#else:
 #   a = ab // 10
  #  b = ab % 10
   # ba = (b * 10) + a
    #print(ba)


#145)s = input()
#odd = int(s[0]) + int(s[2]) + int(s[4])
#even = int(s[1]) + int(s[3]) + int(s[5])
#if odd== even:
 #   print("Lucky")
#else:
 #   print("Not lucky")




