# Personality Teller
import random

personalities = ['Arrogant and Rude','Funny and Polite','Insane and Crazy'
,'Lover and Cute','Nerd and Boring','Cool and Rude','Cute but arrogant','Intelligent and Geek'
,'Cool and Funny','Idiot and Crazy','Awesome and Crazy','Good and Smart','Cool and Smart',
'Smart and Geek','Cool and Smart']

def teller():
    input('Tell Your Name : ')
    return('According to your name You are ' + random.choice(personalities) + '.')

print(teller())
