hour=int(input("عددی بین 0تا23 به عنوان ساعت وارد کنید:"))
if hour<0 or hour>23:
    print("عدد وارد شده خارج از بازه مجاز است")
else:
    if hour>=6 and hour<=16:
        print("صبح")
    elif hour>=12 and hour <=16:
        print("ظهر")
    elif hour>=17 and hour<=20:
        print("عصر")
    elif hour>=21 or hour<=5:
        print("شب")
