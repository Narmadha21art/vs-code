"""SIMPLE CALCULATER -MINI PROJECT BY USING PYTHON PROGRAMMIN LANGUAGE

1.creating functions 2.writing user input 3.printing result

this calculter include 1.Additiion 2.Substraction 3.Multiplication 4.Division 5.Sum 6.Average 7.Mean"""



#function to addition two numbers
def addition(number1,number2):
    return(number1+number2)
#function to substraction two numbers
def substraction(number,number2):
    return(number1-number2)
#function to multiplication two numbers
def multiplication(number,number2):
    return(number1*number2)
#function to division two numbers
def division(number,number2):
    return(number1/number2)
#function to sum two numbers
def sum(number,number2):
    return(number1+number2)
#function to average two numbers
def average(number,number2):
    return((number1+number2)/2)
#function to mean two numbers
def mean(number1,number2):
    return((number1+number2)/2)
def even(number1,number2):
    return((number1/2)==0 and (number2/2)==0)
def odd(number1,number2):
    return((number1/2)==1 and (number2/2)==0)



#step-2 user input
print("please select a operation:\n "\
      "1.Addition\n" \
      "2.Substraction\n" \
      "3.Multiplication\n" \
      "4.Division\n" \
      "5.Sum\n" \
      "6.Average\n")

select =int(input("select a operation from 1,2,3,4,5,6: "))
number1=int(input("enter first number: "))
number2=int(input("enter second number: "))


#step-3 print the result
if select == 1:
    print("addition of two numbers is :",number1,"+",number2,"=",addition( number1,number2))
elif select == 2:
    print("substraction of two numbers is :",number1,"-",number2,"=",substraction( number1,number2))
elif select == 3:
    print("Multiplication of two numbers is :",number1,"*",number2,"=",multiplication( number1,number2))
elif select == 4:
    print("Division of two numbers is :",number1,"/",number2,"=",division( number1,number2))
elif select == 5:
    print("Sum of two numbers is :",number1,"+",number2,"=",sum( number1,number2))
elif select == 6:
     print("Averageon of two numbers is :",(number1, "+",number2),"/" "2" "=",average( number1,number2))
else:
    print("please select a valid  operation number")
