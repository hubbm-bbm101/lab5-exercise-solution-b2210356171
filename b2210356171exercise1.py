def odd_sum(num):
    sum=0
    for a in range (1, num+1):
        if a%2==1:
            sum+=a
    return(sum)

def average_even(num):
    sum = 0
    numofevens = 0
    for a in range(1, num + 1):
        if a % 2 == 0:
            sum += a
            numofevens+=1
    if numofevens!=0:
        return(sum/numofevens)

number = int(input("give a number: "))
print("The sum of the odd numbers is", (odd_sum(number)) )
print("The average of the even numbers is", (average_even(number)) )