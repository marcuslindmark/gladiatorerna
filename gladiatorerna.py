import random, colorama
from colorama import Fore, Style

# Initierar colorama (speciellt viktigt på Windows)
colorama.init()

#print(Fore.RED + "Detta är röd text" + Style.RESET_ALL)
#print(Fore.GREEN + "Detta är grön text" + Style.RESET_ALL)
#print(Fore.YELLOW + "Detta är gul text" + Style.RESET_ALL)

### VARIABLER I SPELET ###

# Övrigt
strid_pågår = True
runda = 1

# Hälsopoäng
spelarens_hp = 10
fiendens_hp = 6

# Träffchans spelaren
spelarens_träffchans = 5

# Träffchans fienden
fiendens_träffchans = 3

### Attacker ###

# Järnhård näve
lägsta_skada_järnhård_näve = 2
högsta_skada_järnhård_näve = 3
modifiering_träffchans_järnhård_näve = -2 

# Kvick spark
lägsta_skada_kvick_spark = 1
högsta_skada_kvick_spark = 2
modifiering_träffchans_kvick_spark = 2 


# Att göra: Programmera ett stridssystem utan vapen
print ("\n\n" + Fore.BLUE + "GLADIATORERNA" + Style.RESET_ALL)
print (Fore.YELLOW + "=============" + Style.RESET_ALL)
print ("Du är gladiatorn " + Fore.GREEN + "Rikke" + Style.RESET_ALL + ", nu ska du slåss mot gladiatorn " + Fore.RED + "Postumius." + Style.RESET_ALL)
print ("Ni befinner er på en romersk arena omgivna av en förväntansfull publik")
print ("Ni har inga vapen eller rustning utan du är klädd enbart i ett par")
print ("korta läderbyxor, ett par pälsstövlar och armband gjorda av läder.")
print ("Din bara bronsfärgade bringa lyses upp av den starka solen.")
print ("Publiken som sitter runt omkring er ser förväntansfulla ut.")
print ("Postemius ser ut att göra sig redo att gå till anfall.")
print ("Striden kan börja.\n")


while (strid_pågår):
    Fore.RED + "Detta är röd text" + Style.RESET_ALL
    
    print (Fore.RED + "Ni spelar runda nummer " + Fore.YELLOW + str(runda) + Style.RESET_ALL + ".")
    runda = runda + 1
    
    print (f"\nDu har just nu {spelarens_hp} hälsopoäng kvar.")
    print (f"Din fiende har just nu {fiendens_hp} hälsopoäng kvar.")

    # Järnhård näve ger 2 och 4 i skada och -2 träffchans
    # Kvick spark ger mellan 1 och 3 i skada och +2 träffchans
    spelarens_val = input ("\nVill du attackera med din järnhårda " + Fore.GREEN + "näve " + Style.RESET_ALL + "eller med din kvicka " + Fore.YELLOW + "spark? " + Style.RESET_ALL).lower()

    
    T10 = random.randint(1, 10)

    if (spelarens_val == "näve"):
        print ("Du slår hårt mot din motståndare.") 
        if (T10 <= spelarens_träffchans + modifiering_träffchans_järnhård_näve):   
            print ("Och träffar!")

            # Beräknar vad skadan och berättar för spelaren vad som händer
            skada_järnhård_näve = random.randint(lägsta_skada_järnhård_näve, högsta_skada_järnhård_näve)
            print (f"Du gör {skada_järnhård_näve} hälsopoäng i skada.")

            fiendens_hp = fiendens_hp - skada_järnhård_näve
            print (f"Din fiende har nu {fiendens_hp} hälsopoäng kvar.")
        else:
            print ("Och missar!")
    elif (spelarens_val == "spark"):
        print ("Du skickar iväg en snabb spark.")
        if (T10 <= spelarens_träffchans + modifiering_träffchans_kvick_spark):
            print ("Och träffar!")

            # Beräknar vad skadan och berättar för spelaren vad som händer
            skada_kvick_spark = random.randint(lägsta_skada_kvick_spark, högsta_skada_kvick_spark)
            print (f"Du gör {skada_kvick_spark} hälsopoäng i skada.")

            fiendens_hp = fiendens_hp - skada_kvick_spark
            print (f"Din fiende har nu {fiendens_hp} hälsopoäng kvar.")
        else:
            print ("Och missar!")        

    ### FIENDEN ATTACKERAR! ###

    # Bestäm vilken attack som fienden väljer
    fiendens_attacker = ["slag", "spark"]
    fiendens_val = random.choice(fiendens_attacker)
        
    T10 = random.randint(1, 10)
    
    # Kontrollerar att fienden inte redan är besegrad
    if (fiendens_hp > 0):
        # Om fienden lever körs striden
        print ("\nNu attackerar din motståndare dig!")
        if (fiendens_val == "slag"):
            print ("Din fiende slår hårt mot dig.") 
            if (T10 <= fiendens_träffchans + modifiering_träffchans_järnhård_näve):   
                print ("Och träffar!")

                # Beräknar vad skadan och berättar för spelaren vad som händer
                skada_järnhård_näve = random.randint(lägsta_skada_järnhård_näve, högsta_skada_järnhård_näve)
                print (f"Din fiende gör {skada_järnhård_näve} hälsopoäng i skada.")

                spelarens_hp = spelarens_hp - skada_järnhård_näve
                print (f"Du har nu {spelarens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
        elif (fiendens_val == "spark"):
            print ("Din fiende skickar iväg en snabb spark mot dig.")
            if (T10 <= fiendens_träffchans + modifiering_träffchans_kvick_spark):
                print ("Och träffar!")

                # Beräknar vad skadan och berättar för spelaren vad som händer
                skada_kvick_spark = random.randint(lägsta_skada_kvick_spark, högsta_skada_kvick_spark)
                print (f"Din fiende gör {skada_kvick_spark} hälsopoäng i skada.")

                spelarens_hp = spelarens_hp - skada_kvick_spark
                print (f"Du har nu {spelarens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")


    print ("\n")    # Extra radbrytning.
    
    # Kontrollerar om det är dags att avsluta striden
    if (spelarens_hp <= 0 or fiendens_hp <= 0):
        strid_pågår = False

# Slut meddelande
if (spelarens_hp <= 0):
    print ("Du förlorade striden. Bättre lycka nästa gång.")
elif (fiendens_hp <= 0):
    print ("Din fiende förlorade striden. Grattis du vann.")


# Avsluta colorama (endast för god praxis)
colorama.deinit()