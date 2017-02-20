import random
x=random.randint(1,100)
z=0

while True:
    b=int(raw_input("guess a no my friend"))
    
    if x==b:
        print "congrats your guess is correct your score "+str(100-z)
        z+=1
        break
    elif x>b:
        c=x-b
        if c>25:
            print "your guess is  <<<<<<< TRY AGAIN >>>>>>>>>>             <<<<<<<<<    [too low]"
            z+=1
        else:
            print "your guess is  <<<<<<< TRY AGAIN >>>>>>>>>>             <<<<<<<<     [low]"
            z+=1
    elif x<b:
        c=b-x
        if c>25:
            print"your guess is to  <<<<<<< TRY AGAIN >>>>>>>>>>           <<<<<<<<     [too high]"
            z+=1
        else:
            print"your guess is   <<<<<<< TRY AGAIN >>>>>>>>>>             <<<<<<<<<    [high]"
            z+=1
        
    
   
        

    
    
    
