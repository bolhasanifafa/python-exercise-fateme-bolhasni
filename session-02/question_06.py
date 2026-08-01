2amount=int(input('mablagh kharid ra vared konid:'))
if amount>1000000:
   discount=amount*0.15
elif amount>=500000 and amount<= 1000000:
     discount=amount*0.10
else:
    discount=0
final_amount=amount-discount
print(final_amount)        

    

    
    