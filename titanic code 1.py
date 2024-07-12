import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('C:/Users/gsoft store/Documents/titanic/train.csv')
data.head(10)
def f():
    data.drop(["PassengerId","Ticket","Fare","Embarked"], axis=1, inplace=True)
    print(data)
    print(data.columns)
    return f
def f2():
    data.Survived.value_counts().plot(kind="barh")
    plt.title("Titanic")
    plt.xlabel("Dead(0) and alive(1)")
    plt.ylabel("No. of Passengers")
    plt.show()
    return f2
def f3():
    data.Sex.value_counts().plot(kind="pie")
    plt.ylabel("")
    plt.show()
    return f3
def f4():
    data.Pclass.value_counts().plot(kind="density")
    plt.ylabel("")
    plt.show()
    return f4
print(f())
c=input("Enter chart category(Survived,Sex,Pclass):")
if c=="Survived":
    print(f2())
elif c=="Sex":
    print(f3())
elif c=="Pclass":
    print(f4())

