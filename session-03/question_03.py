majmoo=0 
for i in range(1,11):
    if i % 2==0:
        natije=i+5
        majmoo=majmoo+natije
    else:   
        natije=i*5
        majmoo=majmoo+natije
    print(majmoo)