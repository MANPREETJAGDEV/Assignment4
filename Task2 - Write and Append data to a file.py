# Program to write and append text as input by the user in a output.txt file

input_data1=input("Enter text to write to the file:")
file=open("j:\\PYTHON\\Assignments\\Assignment 4\\output.txt","w+")
writing_data1=file.write(input_data1 + "\n")
print("Data Sucessfully written to output.txt.\n")
input_data2=input("\nEnter additional text to append:")
appending_data=file.write(input_data2 + "\n")
print("Data Sucessfully appended.")

file.close()
final_output=open("j:\\PYTHON\\Assignments\\Assignment 4\\output.txt","r")
print("\nFinal content of output.txt\n")
print(final_output.read())
file.close()
