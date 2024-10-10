import random, colorama, msvcrt
from colorama import Fore, Style

# Initierar colorama (speciellt viktigt på Windows)
colorama.init()

### VARIABLER I SPELET ###

# Vapen variabeln håller reda på om spelaren bär på något vapen. 
vapen = "Du har inget vapen."

# Hälsopoäng (dessa är variabler eftersom de förändras under spelet. 
# Behöver därför skickas in i mina funktioner innan de går att modifera där.)
spelarens_hp = 10
fiendens_hp = 6

# Träffchans (dessa är konstanter eftersom de har fasta värden. 
# Konstanter är automatiskt globala och behöver därför inte skickas in i funktioner som argument.)
SPELARENS_TRÄFFCHANS = 5
FIENDENS_TRÄFFCHANS = 5


### Attacker ###

# Järnhård näve
LÄGSTA_SKADA_JÄRNHÅRD_NÄVE = 2
HÖGSTA_SKADA_JÄRNHÅRD_NÄVE = 3
MODIFIERING_TRÄFFCHANS_JÄRNHÅRD_NÄVE = -2 

# Kvick spark
LÄGSTA_SKADA_KVICK_SPARK = 1
HÖGSTA_SKADA_KVICK_SPARK = 2
MODIFIERING_TRÄFFCHANS_KVICK_SPARK = 2

# Kortsvärd
MODIFIERING_SKADA_KORTSVÄRD = 1

# Övrigt
ogiltigt_val = False
strid_pågår = True
runda = 1


### FUNKTIONER ###

# Funktion för att hantera fiendens val av attack.
def fienden_väljer(spelarens_hp):
    
    # Bestäm vilken attack som fienden väljer
    fiendens_attacker = ["slag", "spark"]
    fiendens_val = random.choice(fiendens_attacker)
        
    T10 = random.randint(1, 10)         # Slumpar fram ett tal mellan 1 och 10 (rullar en tiosidig tärning)
    
    # Kontrollerar att fienden inte redan är besegrad
    if (fiendens_hp > 0):
        # Om fienden lever körs striden
        print ("Nu attackerar din motståndare dig!")
        if (fiendens_val == "slag"):
            print ("Din fiende slår hårt mot dig.") 
            if (T10 <= FIENDENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_JÄRNHÅRD_NÄVE):   
                print ("Och träffar!")

                # Beräknar vad skadan och berättar för spelaren vad som händer
                skada_järnhård_näve = random.randint(LÄGSTA_SKADA_JÄRNHÅRD_NÄVE, HÖGSTA_SKADA_JÄRNHÅRD_NÄVE)
                print (f"Din fiende gör {skada_järnhård_näve} hälsopoäng i skada.")

                spelarens_hp = spelarens_hp - skada_järnhård_näve
                print (f"Du har nu {spelarens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
        elif (fiendens_val == "spark"):
            print ("Din fiende skickar iväg en snabb spark mot dig.")
            if (T10 <= FIENDENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_KVICK_SPARK):
                print ("Och träffar!")

                # Beräknar vad skadan och berättar för spelaren vad som händer
                skada_kvick_spark = random.randint(LÄGSTA_SKADA_KVICK_SPARK, HÖGSTA_SKADA_KVICK_SPARK)
                print (f"Din fiende gör {skada_kvick_spark} hälsopoäng i skada.")

                spelarens_hp = spelarens_hp - skada_kvick_spark
                print (f"Du har nu {spelarens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
    
    if (fiendens_hp > 0):   # Hoppas över om spelaren redan vunnit. 
        tryck_på_valfri_tangent()

    return spelarens_hp  # Returnerar det uppdaterade värdet


# Funktion för att hantera spelarens val av attack.
def spelaren_väljer(fiendens_hp):
    ogiltigt_val = True
    while ogiltigt_val:
        # Spelaren får välja attack.
        spelarens_val = input ("\nVill du attackera med din järnhårda " + Fore.GREEN + "näve " + Style.RESET_ALL + "eller med din kvicka " + Fore.YELLOW + "spark? " + Style.RESET_ALL).lower()

        # Slumpar ett tal mellan 1 och 10
        T10 = random.randint(1, 10)    
            
        if (spelarens_val == "näve"):
            ogiltigt_val = False
            print ("\nDu slår hårt mot din motståndare.") 
            if (T10 <= SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_JÄRNHÅRD_NÄVE):   
                print ("Och träffar!")

                # Beräknar skadan och berättar för spelaren vad som händer
                skada_järnhård_näve = random.randint(LÄGSTA_SKADA_JÄRNHÅRD_NÄVE, HÖGSTA_SKADA_JÄRNHÅRD_NÄVE)
                print (f"Du gör {skada_järnhård_näve} hälsopoäng i skada.")

                fiendens_hp = fiendens_hp - skada_järnhård_näve
                print (f"Din fiende har nu {fiendens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
        elif (spelarens_val == "spark"):
            ogiltigt_val = False
            print ("\nDu skickar iväg en snabb spark.")
            if (T10 <= SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_KVICK_SPARK):
                print ("Och träffar!")

                # Beräknar skadan och berättar för spelaren vad som händer
                skada_kvick_spark = random.randint(LÄGSTA_SKADA_KVICK_SPARK, HÖGSTA_SKADA_KVICK_SPARK)
                print (f"Du gör {skada_kvick_spark} hälsopoäng i skada.")

                fiendens_hp = fiendens_hp - skada_kvick_spark
                print (f"Din fiende har nu {fiendens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
        else:
            print ("Ogiltigt val. Skriv antingen näve eller spark.")
            ogiltigt_val = True
    
    tryck_på_valfri_tangent()

    return fiendens_hp  # Returnerar det uppdaterade värdet

def visa_introtext():
    print ("Ni befinner er på en romersk arena omgivna av en förväntansfull publik")
    print ("Du håller hårt i ditt vapen, men har ingen rustning utan du är klädd i ett par")
    print ("korta läderbyxor, ett par pälsstövlar och armband gjorda av läder.")
    print ("Din bara bronsfärgade bringa lyses upp av den starka solen.")
    print ("Publiken som sitter runt omkring er ser förväntansfulla ut.")
    print ("Postemius ser ut att göra sig redo att gå till anfall.")
    print ("Striden kan börja.")

    tryck_på_valfri_tangent()


# Funktion som visar och uppdaterar rundan
def visa_och_uppdatera_rundan(runda):
    print (Fore.RED + "Ni spelar runda nummer " + Fore.YELLOW + str(runda) + Style.RESET_ALL + ".")
    runda = runda + 1
    return runda

# Funktion som visar spelarens och fiendens kvarvarande hälsopoäng
def visa_hälsopoäng():
    print ("\nDu har just nu " + Fore.GREEN + str(spelarens_hp) + Style.RESET_ALL + " hälsopoäng kvar.")
    print ("Din fiende har just nu " + Fore.RED + str(fiendens_hp) + Style.RESET_ALL + " hälsopoäng kvar.")

# Funktion som berättar vilka attacker det är som spelaren kan göra
def visa_tillgängliga_attacker():    
    print ("\nDu har följande attacker:")
    print (f"Järnhård näve: gör mellan {LÄGSTA_SKADA_JÄRNHÅRD_NÄVE} och {HÖGSTA_SKADA_JÄRNHÅRD_NÄVE} i skada. Träffchansen är {SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_JÄRNHÅRD_NÄVE} av 10.")
    print (f"Kvick spark: gör mellan {LÄGSTA_SKADA_KVICK_SPARK} och {HÖGSTA_SKADA_KVICK_SPARK} i skada. Träffchansen är {SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_KVICK_SPARK} av 10.")

# Funktion som lägger in en paus i spelet            
def tryck_på_valfri_tangent():            
    print("\nTryck på valfri tangent för att fortsätta...")
    msvcrt.getch()  # Väntar på att användaren trycker på en tangent
    print ("\n")

# Funktion som låter spelaren välja ett vapen till sin gladiator innan spelet startar.
def välj_vapen(vapen):
    print ("\n\n" + Fore.BLUE + "GLADIATORERNA" + Style.RESET_ALL)
    print (Fore.YELLOW + "=============" + Style.RESET_ALL)
    print ("Du är gladiatorn " + Fore.GREEN + "Rikke" + Style.RESET_ALL + ", nu ska du slåss mot gladiatorn " + Fore.RED + "Postumius.\n" + Style.RESET_ALL)
    print ("Innan striden kan börja behöver du välja ditt vapen.")
    print ("1. Kortsvärd (Ger +1 skada)")
    print ("2. Lasso (fångar spelaren en runda)")

    vapenval_pågår = True 

    while (vapenval_pågår):
        val_av_vapen = input("\nVad väljer du? ")
    
        if (val_av_vapen == "1"):
            vapen = "kortsvärd"
            vapenval_pågår = False
        elif (val_av_vapen == "2"):    
            vapen = "lasso"
            vapenval_pågår = False
        else:
            print ("Ogiltigt val. Välj igen.")

    print (f"\nDu valde {vapen} som ditt vapen.")
    
    tryck_på_valfri_tangent()

    # Uppdaterar variabeln vapen med det vapen som spelaren valde
    return vapen


### INTRO TILL SPELET ###

# Spelaren får välja ett vapen till sin gladiator
välj_vapen(vapen)

# Visar introtexten till spelet
visa_introtext()


### STRIDEN BÖRJAR HÄR ###

while (strid_pågår):
    ### VISA STATUS I STRIDEN ###
    
    # Visa vilken runda det är och uppdatera den
    runda = visa_och_uppdatera_rundan(runda)
        
    # Visa antal hälsopoäng som spelaren och fienden har
    visa_hälsopoäng()

    # Berättar vilka attacker som spelaren kan göra
    visa_tillgängliga_attacker()
    

    ### SPELAREN ATTACKERAR! ###

    # Se vad spelaren väljer att göra och uppdatera fiendens_hp baserat på resultatet
    fiendens_hp = spelaren_väljer(fiendens_hp) 

    
    ### FIENDEN ATTACKERAR! ###

    # Se vad fienden väljer att göra och uppdatera spelarens_hp baserat på resultatet
    spelarens_hp = fienden_väljer(spelarens_hp)
    
    
    ### SKA STRIDEN AVSLUTAS? ###

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