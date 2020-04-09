

DSV = 138350

print("ActionTime:")
AT = int(input())
print("Items Per Action:")
IPA = int(input())
print("Unit Price:")
UP = int(input())
print("Do you use Diamond Spreading: [YES/NO]")
DS = (input())
print("Do you use Lava buckets: [YES/NO]")
LB = (input())
print("Do you use Catalysts: [YES/NO]")
C = (input())
print("Do you use Fly Catchers: [YES/NO]")
FC = (input())



if LB == "YES":
    AT = AT * 0.8
else:
    AT = AT / 1

if C == "YES":
    AT = AT / 3
else:
    AT = AT / 1
if FC == "YES":
    AT = AT * 0.7
else:
    AT = AT / 1





if DS == "YES":
    an = (86400 / AT + IPA * UP + DSV / AT)
else:
    an = (86400 / AT + IPA * UP / AT)
print("How many minion slots:")
MS = int(input())

an = an * MS


print(an)

k=input("press enter to exit") 

