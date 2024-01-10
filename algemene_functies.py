def mijn_functie_1(lijst_met_cijfers):
    for i in lijst_met_cijfers:
        print(pow(i,2))
    return i
    

lijst_met_cijfers=[2,4,10,12]

mijn_functie_1(lijst_met_cijfers)




def mijn_functie_2(a,b):
     
     result = []

     
     result.append(a+b)
     result.append(a-b)
     result.append(a*b)
     result.append(round(a/b))

     return result

mijn_functie_2(12,3)
mijn_functie_2(12,2)
mijn_functie_2(10,5)
mijn_functie_2(100,20)