Num1 = int(input("Num1: \n"))
Num2 = int(input("Num2: \n"))
Num3 = int(input("Num3: \n"))
Num4 = int(input("Num4: \n"))
Set1 = 0
Set2 = 0

if (Num1>Num2):
    Set1 = Num1
else:
    Set1 = Num2
if (Num3>Num4):
    Set2 = Num3
else:
    Set2 = Num4

if (Set1>Set2):
    print("This is greatest is " + str(Set1))
else:
    print("This is greatest is " + str(Set2))
