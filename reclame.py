from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs - (prijs * korting)
    
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {korting}0 euro.")

aanbieding_1("aardbei", 4, 0.1)




def inkomsten_totaal1(inkomsten, btw):
    totaal = 0
    for i in inkomsten:
        totaal += i
        bedrag = btw * totaal
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]

print(inkomsten_totaal1(inkomsten, 0.09))



def laag_en_hoog(mijn_lijst):
    result = []
    result.append(max(mijn_lijst))
    result.append(min(mijn_lijst))
    
    return result



print(laag_en_hoog(inkomsten))



def gemiddelde(mijn_lijst):
    totaal = 0
    for i in mijn_lijst:
        totaal += i
   
  
    return totaal / len(mijn_lijst)

print (f"De gemiddelde inkomsten deze week zijn {gemiddelde(inkomsten)} euro.")




def meervoudig(invoer_lijst):
    result = laag_en_hoog(invoer_lijst)
    return result

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
    
print(meervoudig(invoer_lijst))




def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])

    return uitvoer



    


print(combinatie(invoer_lijst))