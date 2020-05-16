#print('hello Peter')
from Hello import Hello

Name=input('What Names do you want to say hello to?')
Names=Name.split(",")
print(Names)

Test=Hello(Names,Greetings='Hi').say_hi()
