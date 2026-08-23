a=input("yek matn vared konid:")
if len(a) % 2==0:
    print(a[:len(a)//2])
else:
    print(a[len(a)//2:])
    