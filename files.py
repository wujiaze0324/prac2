name = input("Enter your name")
temp_file = open("name.txt","w")
print(name,file=temp_file)
temp_file.close()

temp_file = open("name.txt","r")
temp_file.read()
print("Your name is{}". format(name))
temp_file.close()

temp_file = open("number.txt","w")
print("17",file=temp_file)
print("42",file=temp_file)
temp_file.close()

temp_file = open("number.txt","r")
first_number = int(temp_file.readline())
second_number = int(temp_file.readline())
result = first_number + second_number
print("The result is", result)
temp_file.close()

temp_file = open("number.txt","r")




