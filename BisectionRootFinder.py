def function(x):
    return x ** 3 - x ** 2 + 2


def solving(number1, number2, tolerantValue=0.001):
    c = 0.0000
    while True:
        if abs(number1 - number2) >= tolerantValue:
            if function(number1) * function(number2) < 0:
                c = (number1 + number2) / 2
                if function(c) == 0:
                    print("The root is :" + "{0:.4f}".format(c))
                    break
                elif function(number1) * function(c) < 0:
                    number2 = c
                    continue
                else:
                    number1 = c
                    continue

            else:
                print("There is not any root")
                break


number1=eval(input("Enter first number\n"))
number2=eval(input("Enter secend number\n"))
solving(number1, number2)
