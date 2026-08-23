mojoodi=float(input("mojodi hesab ra vared konid:"))
bardasht=float(input("mablagh bardasht ra vared konid:"))
if bardasht<=0:
    print("mablagh na moatabar ast")
elif bardasht>mojoodi:
    print("mojoodi kafi nist")
else:
     mojoodi_jadid=mojoodi-bardasht
     print("amaliayt movafagh")
     print(mojoodi_jadid)
     