#File I/O

#1. File I/O in Python
#Python can be used to perform operations on a file: reading data from it and writing data to it. Data in variables is lost when a program ends; files store it permanently.

#Types of files: 
# Text files: store plain text, like .txt , .log , .csv , .py . 
# Binary files: store data in binary form, like .mp4 , .mov , 
# Note: a Word file ( .docx ) is actually stored as a binary file, even though it contains text.

#2. Open, Read and Close a File
#We have to open a file before reading or writing, and close it when we are done.

##Read file data
# f = open("file.txt", "r")

# data = f.read()

# print(data)

# f.close()
##write data
f = open("file.txt", "w")

data = f.write("passage")

print(data)
f.close()
