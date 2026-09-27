while True:
    first_num = int(input("Enter a number: "))
    operator = input("Choose one operator (+, -, *, /): ") 
    second_num = int(input("Enter another number: "))

    if operator == "+":
        total = first_num + second_num
        print("Answer:" , total)
        
    elif operator == "-":
        total = first_num - second_num
        print("Answer:" , total)
        
    elif operator == "*":
        total = first_num * second_num
        print("Answer:" , total)
        
    elif operator == "/":
        if second_num == 0:
            print("You cannot divide by Zero!")
        else:
            total = first_num / second_num
            print("Answer:" , total)
        
    else:
        print("Invalid Operator")
        
    again = input("Do you want to calculate again? (Yes/No): ")
    
    if again.lower() == "no":
        break
print("Have a nice day!")