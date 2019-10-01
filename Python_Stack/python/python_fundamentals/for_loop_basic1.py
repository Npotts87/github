#1 Basic - Print all integers from 0 to 150.
def printints0to150():
    for i in range (0, 151):
        print(i)
printints0to150 ()

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000.
def multiplesof5 ():
    for i in range (5, 1001, 5):
        print(i)
multiplesof5 ()

#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def countingthedojoway ():
    for i in range (1, 101):
        if i % 5 == 0:
            print("Coding")
        if i % 10 == 0:
            print("Coding Dojo")
countingthedojoway ()

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def woah ():
    sum = 0
    for i in range (1,500000,2):
        sum += i
    print(sum)
woah ()

#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def countdownbyfours ():
    for i in range(2018, 0, -4):
        print(i)
countdownbyfours ()

#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexiblecounter ():
    lowNum = 1
    highNum = 10
    mult = 2
    for i in range (lowNum, highNum):
        if i%mult == 1:
            print (i)
flexiblecounter ()