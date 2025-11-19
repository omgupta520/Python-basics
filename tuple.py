

# my_tuple[0]=1000      # tuples are immutable
# print(my_tuple[0])    



# t1=(1,2,35,5) # integer
# print(t1) 
# t2=("apple",10,3.14,True) # mixed form of tuple
# print(t2)
# ordered 
# immutabel ->cant  be changed
fruit=("apple","avacado","papaya","cherry")
# fruit[0]="banana" # mutability is missing in tuple 
# print(fruit)
# print(fruit[0])
# print(fruit[-1])
# print(fruit[0:2]) # slicing    




# a=(11,2,122)
# b=(21,54) 
# print(a +b) # concat in tuple
# #repetetion 
# print(a*5)    
# # membership
# print(122 in a)
# print(10 in a)

# tuple packing and unpacking

# data=('tanshiq',22,'india') #packing
# name,age,country=data #unpacking
    
# print(name)
# print(age)
# print(country)


# #built in function in tuple

# nums=(1,2,3,4,5,6,7)
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(nums.count(2))
# print(nums.index(3)) # it would print the idx of element 3

# # # tuple are immutable 
# t=(1,2,3)
# t[1]=4 #i m trying to update the number 
# print(t)

# a=5
# b=10
# a,b=b,a
# print(a,b) # swapping of numbers


#write a function that takes a tuple of numbers and returns a new tuple with only even numbers?   
# t=(1,2,3,4,5,6,7,8,)
# def get_even(t):
#     return tuple(x for x in t if x%2==0)
# print  (get_even(t))

# tuple=(1,2,3,4,5,7,7,7,7,7)
# print(tuple)



# my_tuple=(10,"hello",11,2,3,4,445)
# print(my_tuple[2])
# print(my_tuple[-2])
# print(my_tuple[1:4])
# print(my_tuple[3:5])
# slicing
#print
# concatination
# # repetetion   



# t=(1,2)
# print(t*3)
# print(2 in t) # membership 
# print(len(t))