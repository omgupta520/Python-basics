# #dictionery ->>>> is a collection of key value pair 



student ={
    "name":"global", # key ->value
    "age":"21",
    "course":"ai"
}

# # #accesing value

# print(student["name"])
# print(student["age"])
# print(student["course"])

# #using get method

# print(student.get("age"))
# print(student.get("course"))  
# print(student.get("age"))

# # #adding and updating the value 

# student["city"]="Delhi" # add
# # print(student)
# student["id"]="local" #add
# # print(student)
# student["age"]=30    #update
# print(student)

 
# #removing item
 
# student.pop("course") # remove 
# student.popitem()     # removes the last inserted key 
# # del student["name"]   # other way to delete the item 
# # student.clear()       # removes everything 

# for key in student:
#     print(key)
    

# for value in student.values():
#     print(value)

for key,value in student.items():
    print(f"{key}->{value}")
    
    
print(student.keys())
print(student.values())
print(student.items())



# # student.pop("course") # remove whatever you want to 
# # print(student)





# #adding and updating
# # student["address"]="gurgaon" # additio of new key value pair 
# # student["age"]=23 # updating of age
# # print(student)

# for key,value in student.items():
#     print(f"{key}->{value}")

# # fstring concept
# # a=3
# # print(f"hello my age is {a}")

# #question  
  
marks = {
    "Math": 90,
    "Physics": 85,
    "Chemistry": 92
}

# # Total and average marks
total = sum(marks.values())
print(total)
average = total / len(marks)
print(average)



# if "branch" in result:
#     print("key branch exist")
# else:
#     print("key branch doesnt exist")    
