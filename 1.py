def mass(mass1,mass2):
    while mass1:
         a=mass1.pop(0)
         mass2.append(a)
         print(mass2)

   


mass1=["site1", "site2" , "site3", "site4"]
mass2=[]
mass(mass1,mass2)
gotovo(mass2)
