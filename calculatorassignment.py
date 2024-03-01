def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y 
def divide(x,y):
    if y == 0:
        return "Error!"
    return x/y

def calculator():
    history=[]

    while True:
        print("Function:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.View History")
        print("6.Exit")

        choice = input ("Enter choice:1,2,3,4,5,6")

        if choice in ('1','2','3','4'):
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))

            if choice == '1':
                result=add(num1, num2)
                print("Result:", result)
                history.append((num1,'+',num2,'=',result))
            elif choice == '2':
                result=subtract(num1,num2)
                print("\Result:", result)
                history.append((num1,'-',num2,'=',result))
            elif choice == '3':
                result=multiply(num1,num2)
                print("Result:",result) 
                history.append((num1,'*',num2,'=',result))
            elif choice == '4':
                result=divide(num1,num2)
                print("Result:",result)
                history.append((num1,'/',num2,'=',result))
        elif choice == '5':
            if not history:
                print("history is empty.")
            else:
                print("calculation history:")
                for entry in history:
                    print(entry)
        elif choice == '6':
            break

        else: 
            print("Invalid input.")

if __name__ == "__main__":
    calculator()
                


    