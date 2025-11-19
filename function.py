# def func(parameters):
#     #code block
#     return value 



# # simpl function
 
# def say_helo():
#     print("hello everyone") # will give the output as -> say hello 
# say_helo()  #calling of  function

# #function with parameter

# def greet(name):
#     print("hello",name)
# greet("garv") # calling my function

# #function with return value

# def add(a,b):
#    return a + b
# result=add(4,5)
# print(result) #calling our function 
# print(add(10,30))

# checking wheter num is odd or even 

# a=int(input("enter your number"))
# def num(a):
#     if a%2==0:
#         print("even")
#     else :
#         print("odd")
# num(a)  #calling of function

# #default parameters

def greet(name="1"):
 print("hello",name) # body
greet() #calling default
greet("global") #calling with some value of parameter  
        
# #arbitary arguments

# def total(*num):
#   print(sum(num))  #body 
# total(1,2,3,4,5) # calling with parameter

# # #multiple keywords argument

# def total(**info):
#     print(info)
# total(name="global",age=20,course="cyber",festival="Diwali")  

# # write a function to print odd and even in that or to check odd or even?


# def check(num):
#    return "even " if num%2==0 else "odd"
# print(check(10))

# # maximum of two number using function?

# # def max(a,b):
# #     return a if a>b else b  # logic
# # # print(max(12,8))

# # list=[10,20,30,40,50]
# # def input_list():
    
# #    print(min(list))
# # input_list() #caliing
    
# #     user_input=input("enter element that u want to add")
    
# #     # user_list=user_input.split()
# #     # return user_list

# # result=input_list()
# # print("your list is ",result)

# # def print_list(my_list):
# #      print("the list u passed is",my_list)
# # number=[10,20,30,40]
# # print_list(number)

# # def multiply(a,b,c):  # declaration of function
# #     return a*b*c     # return ning condition in fucntion
# # print(multiply(2,3,4)) #caliing of  function 


# def fun():
#   for i in range(0,10):
#      print (i)
# fun()   
# n=int(input("enter the year"))
# def fun_n():
#  if n%4==0:
#   print ("leap year")   
#  else:
#   print("not a leap year")
# fun_n()


# def set_fun():
#   s1={1,2,3,4,5,6,6,778,8,8,8}
#   print(s1)
# set_fun()