# Program to open and print the lines in a sample.txt file

i=1
try:
    file=open("j:\\PYTHON\\Assignments\\Assignment 4\\sample.txt","r")
    print("Reading file content:")
    for line in file:
#strip() removes new line characters and extra spaces
        print("Line", i,":",line.strip()) 
        i=i+1
    file.close()    

except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found.")

