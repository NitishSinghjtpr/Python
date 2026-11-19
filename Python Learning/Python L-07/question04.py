#Q4. Write a function to find in which line of the file the word "learning" occurs first. Print 1 if not found.

def check_line(word):
    line_no=1
    with open("practice.txt","r")as f:
        for line in f: #ek time pe ek line read karta hai
            if word in line:
                return line_no
            line_no+=1
    
    return -1   

print(check_line("learning"))
print(check_line("hello")) 