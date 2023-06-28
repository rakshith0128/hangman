import random
name=(input("enter your name?\n"))
print("let the games begin!! ",name)
box = ['apache']
word = 'tishl'
string = ''*len(word)

while 1:
    user_input= input("guess the word\n")
    index=word.index(user_input)
    
    string = string[:index] + user_input + string[index:]
    print(string)
    if(string==word):
        print("congrats")
        break

    
