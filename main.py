#Matthew Rodriguez
#08/06/2023

#gathers input from user 
filename = input("Enter a name for your file:")
firstname = input("Enter your first name:")
address = input("Enter your address:")
phone = input("Enter your phone number:")

#puts first name, address and phone number into a comma delimited string
info = (f"{firstname},{address},{phone}")

#writes the above string to a file
with open(filename, 'w') as file_object:
  file_object.write(info)

#reads and prints the file
with open(filename) as file_object:
  data = file_object.read()
  print(data)
