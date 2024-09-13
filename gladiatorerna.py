import random, colorama
from colorama import Fore, Style

# Initierar colorama (speciellt viktigt på Windows)
colorama.init()

#print(Fore.RED + "Detta är röd text" + Style.RESET_ALL)
#print(Fore.GREEN + "Detta är grön text" + Style.RESET_ALL)
#print(Fore.YELLOW + "Detta är gul text" + Style.RESET_ALL)

# Hälsopoäng
spelarens_hp = 5
fiendens_hp = 3

# Träffchans
spelarens_träffchans = 5
fiendens_träffchans = 3

# Attacker
skada_järnhård_näve = 2
skada_kvick_spark = 1

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

print (f"Du har just nu {spelarens_hp} hälsopoäng kvar.")
print (f"Din fiende har just nu {fiendens_hp} hälsopoäng kvar.")

# Järnhård näve ger 2 skada och -2 träffchans
# Kvick spark ger 1 skada och +2 träffchans
spelarens_val = input ("Vill du attackera med din järnhårda " + Fore.GREEN + "näve " + Style.RESET_ALL + "eller med din kvicka " + Fore.YELLOW + "spark? " + Style.RESET_ALL).lower()

T10 = random.randint(1, 10)



if (spelarens_val == "näve"):
    print ("Du slår hårt mot din motståndare.") 
    if (T10 <= spelarens_träffchans - 2):           # -2 eftersom järnhård näve minskar träffchansen
        print ("Och träffar!")
        fiendens_hp = fiendens_hp - skada_järnhård_näve
        print (f"Postemius har nu {fiendens_hp} hälsopoäng kvar.")
    else:
        print ("Och missar!")
elif (spelarens_val == "spark"):
    print ("Du skickar iväg en snabb spark.")
    if (T10 <= spelarens_träffchans + 2):           # +2 eftersom kvick spark ökar träffchansen
        print ("Och träffar!")
        fiendens_hp = fiendens_hp - skada_kvick_spark
        print (f"Postemius har nu {fiendens_hp} hälsopoäng kvar.")
    else:
        print ("Och missar!") 




# Avsluta colorama (endast för god praxis)
colorama.deinit()