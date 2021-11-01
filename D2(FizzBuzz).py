fizz = int(input("Insert fizz number "))
buzz = int(input("Insert buzz number "))
finish = int(input("Insert Till for "))
count = 0

while count < finish:  #Cicle count from 1 to 'finish' and replace sqrt of 'fizz' and 'buzz'
    count += 1
    if count % fizz == 0 and count % buzz == 0:
        print("FB", end=" ")
    elif count % fizz == 0:
        print("F", end=" ")
    elif count % buzz == 0:
        print("B", end=" ")
    else:
        print(count, end=" ")