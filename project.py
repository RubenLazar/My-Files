import sys
import random
 

def main():
    d = {}
    capitalss = []
    countrys = []
#READ THE FILES FROM THE "CAPITALS.TXT" ,FILE WHICH CONTAINS COUNTRIES AND THEIR CAPITALS
    with open('capitals.txt') as fin:
        for line in fin:
            country, capitals = line.strip().split(",")
            if capitals:
                capitalss.append(capitals)
            if country:
                countrys.append(country)
            d[country] = capitals


        

    maxp = 0   
    points = 0
    print ('Please enter your name:')      
    name = input()
    print ('\nName:{}'.format(name))
         #GENERATE THE QUESTIONS AND MULTIPLE CHOICE ANSWERS
    while True:
        rand = random.choice(countrys)


        print ('\nWhat is the the capital of {:s}?'.format(rand))

        a = random.choice(capitalss)
        b = random.choice(capitalss)
        c = d[rand]
        if a == b or c == a or c == a:
            a = random.choice(capitalss)
        l = [str(a), str(b), str(c)]
        random.shuffle(l)
        x = ('a) {}'.format(l[0]))
        y = ('b) {}'.format(l[1]))
        z = ('c) {}'.format(l[2]))
        print (x)
        print (y)
        print (z)
            #CHECK IF THE ANSWER IS THE RIGHT ONE AND PRINT SOMETHING
        
        answer = input()
        if answer == "a" and str(x[3:]) == d[rand] or answer == "A" and str(x[3:]) == d[rand]:
            print ('\n' + "CONGRATZ {}!YOUR ANSWER IS RIGHT! RESPECT!".format(name))
            points = points + 1
            if points > maxp:
                maxp = points
            print ('Your actuall point(s) is : {:d}'.format(points))
            print ('Your maximum point(s) overall are: {} point(s)'.format(maxp) + '\n')
        elif answer == "b" and str(y[3:]) == d[rand] or answer == "B" and str(y[3:]) == d[rand]:
            print ('\n' + "CONGRATZ {}!YOUR ANSWER IS RIGHT! RESPECT!".format(name))
            points = points + 1
            if points > maxp:
                maxp = points
            print ('Your actuall point(s) is : {:d}'.format(points))
            print ('Your maximum point(s) overall are: {} point(s)'.format(maxp) + '\n')
        elif answer == "c" and str(z[3:]) == d[rand] or answer == "C" and str(z[3:]) == d[rand]:
            print ('\n' + "CONGRATZ {}!YOUR ANSWER IS RIGHT! RESPECT!".format(name))
            points = points + 1
            if points > maxp:
                maxp = points
            print ('Your actuall point(s) is : {:d}'.format(points))
            print ('Your maximum point(s) overall are: {} point(s)'.format(maxp) + '\n')
        elif answer == "exit":
            break
        else:
            #Check if it's other letter than abcABC
            if answer not in ["a", "b", "c","A", "B", "C"]:
                print ("Try another value such as: A or B or C")
                answer = input()
            else:
                print ("Nope..Wrong answer")
                print ("The right answer is {:s}".format(d[rand]))
            if points != 0:
                points -= 1
                print ('Your actuall point(s) is : {:d}'.format(points))
                print ('Your maximum point(s) overall are: {} point(s)'.format(maxp) + '\n')
            else:
                points = 0
                print ('Your actuall point(s) is : {:d}'.format(points))
                print ('Your maximum point(s) overall are: {} point(s)'.format(maxp))
            
            
if __name__ == '__main__':
    main()
