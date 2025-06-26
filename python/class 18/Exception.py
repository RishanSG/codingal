try:
    num= int(input("Enter a number: "))

    result=100/num
    
    print(result)

except ZeroDivisonError:
    num=1
    result=100/num
    print(result)
    print("You cant divide a number by 0!")

except ValueError:
    print("You must enter a number!")
except Exception as e:
    print("Something went wrong!")


print("hello Rishan, Good Morning!!")