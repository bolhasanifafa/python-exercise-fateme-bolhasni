a=int(input("سن خود را وارد کنید: "))
g=input('جنسیت خود را وارد کنید: ')
if g=='m' and a<=40 and a>=0:
    print( 'pesar')
elif g=='m' and 40<=a<=60:
    print('prdar')
elif g=='m' and a>=60:
    print('pedar bozorg')
elif g=='f' and a<=40 and a>=0:
    print('girl')
elif g=='f' and a>=40 and a<=60:
    print('madar')
elif g=='f' and a>=60:
    print('madar bozorg')
    