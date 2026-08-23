a=int(input('add aval ra vared konid:'))
b=int(input('add dovom ra vared konid:'))
c=input('amalgar ra vared konid(/,*,-,+):') 
if c=="+":
    natije = a + b
    print(natije)
elif c=="-":
    natije = a - b
    print(natije)
elif c=="*":
    natije= a * b
    print(natije)
elif c=="/":
    natije= a / b
    print(natije)
else:
    print("amalgar na moatabar ast")