import random, colorama, msvcrt
from colorama import Fore, Style
from rundan import Runda  # Importerar klassen Runda från filen rundan.py som jag skapat själv.

# Initierar colorama (speciellt viktigt på Windows)
colorama.init()

# Skapa en instans av klassen Runda (som finns i filen rundan.py)
spelets_runda = Runda()

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
MODIFIERING_TRÄFFCHANS_JÄRNHÅRD_NÄVE = -1 

# Kvick spark
LÄGSTA_SKADA_KVICK_SPARK = 1
HÖGSTA_SKADA_KVICK_SPARK = 2
MODIFIERING_TRÄFFCHANS_KVICK_SPARK = 2

# Kortsvärd
LÄGSTA_SKADA_KORTSVÄRD = 2
HÖGSTA_SKADA_KORTSVÄRD = 4
MODIFIERING_TRÄFFCHANS_KORTSVÄRD = -1
SKADA_KORTSVÄRD = [2, 3, 4]
blodiga_beskrivningar_kortsvärd = ["Kortsvärdet skär djupt och blodet skvätter!", "Kortsvärdet träffar armen och ger ett tydligt köttsår. Rött blod rinner ut.", "Kortsvärdet skär genom alla skydd och blodsdroppar flyger åt alla håll."]

# Lasso
fiende_fångad = False                   # Blir True om spelaren träffar med lassot
modifiering_träffchans_lasso = 0        # Om fienden är fångad ökar detta värde
skada_lasso = 0                         # Om fienden är fångad ökar detta värde
lasso_räknare = -1                      # Håller reda på hur många rundor som fienden är fångad

# Övrigt
ogiltigt_val = False
strid_pågår = True




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
                
                if (blodiga_beskrivningar == True):
                    print ("Du får en rejäl smäll och du känner blodsmaken i munnen.")

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

                if (blodiga_beskrivningar == True):
                    print ("Sparken träffar hårt och du kvider av smärta.")

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
def spelaren_väljer(fiendens_hp, fiende_fångad, modifiering_träffchans_lasso, skada_lasso, lasso_räknare):
    ogiltigt_val = True
    while ogiltigt_val:
        # Spelaren får välja attack.
        spelarens_val = input ("\nVilken attack väljer du? ").lower()

        # Slumpar ett tal mellan 1 och 10
        T10 = random.randint(1, 10)    

        ### JÄRNHÅRD NÄVE ###    
        if (spelarens_val == "näve"):
            ogiltigt_val = False
            print ("\nDu slår hårt mot din motståndare.")
            if (fiende_fångad == True):
                print (f"Eftersom fienden är insnärjd i ditt lasso ökar din träffchans med {modifiering_träffchans_lasso}.") 

            if (T10 <= SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_JÄRNHÅRD_NÄVE + modifiering_träffchans_lasso):   
                print ("Och träffar!")
                if (blodiga_beskrivningar == True):
                    print ("Blodet skvätter från hans näsa och mun. Ser ut att göra ont!")

                # Beräknar skadan och berättar för spelaren vad som händer
                skada_järnhård_näve = random.randint(LÄGSTA_SKADA_JÄRNHÅRD_NÄVE, HÖGSTA_SKADA_JÄRNHÅRD_NÄVE)
                print (f"Du gör {skada_järnhård_näve} hälsopoäng i skada.")
                
                # Om fienden är fångad av ett lasso tar den extra skada
                if fiende_fångad == True:
                    print (f"Eftersom fienden är fångad får den {skada_lasso} extra i skada.")

                fiendens_hp = fiendens_hp - (skada_järnhård_näve + skada_lasso)
                print (f"Din fiende har nu {fiendens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
        ### KVICK SPARK ### 
        elif (spelarens_val == "spark"):
            ogiltigt_val = False
            print ("\nDu skickar iväg en snabb spark.")
            
            if (T10 <= SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_KVICK_SPARK + modifiering_träffchans_lasso):
                print ("Och träffar!")
                if (blodiga_beskrivningar == True):
                    print ("Din motståndare kvider av smärta när din spark tränger djupt in i hans mage.")
                
                # Beräknar skadan och berättar för spelaren vad som händer
                skada_kvick_spark = random.randint(LÄGSTA_SKADA_KVICK_SPARK, HÖGSTA_SKADA_KVICK_SPARK)
                print (f"Du gör {skada_kvick_spark} hälsopoäng i skada.")

                # Om fienden är fångad av ett lasso tar den extra skada
                if fiende_fångad == True:
                    print (f"Eftersom fienden är fångad får den {skada_lasso} extra i skada.")

                fiendens_hp = fiendens_hp - (skada_kvick_spark + skada_lasso)
                print (f"Din fiende har nu {fiendens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
        ### KORTSVÄRD ###        
        elif (spelarens_val == "kortsvärd" and vapen == "kortsvärd"):
            ogiltigt_val = False
            print ("\nDu hugger med ditt kortsvärd.")
            if (T10 <= SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_KORTSVÄRD + modifiering_träffchans_lasso):
                print ("Och träffar!")
                if (blodiga_beskrivningar == True):
                    blodsbeskrivning_kortsvärd = random.choice(blodiga_beskrivningar_kortsvärd)
                    print (blodsbeskrivning_kortsvärd)

                # Beräknar skadan från kortsvärdet
                skada_kortsvärd = random.choice(SKADA_KORTSVÄRD)
                
                # Drar av skadan från kortsvärdet från fiendens hälsopoäng.
                fiendens_hp = fiendens_hp - skada_kortsvärd
                
                # Berättar för spelaren vad som händer
                print (f"Du gör {skada_kortsvärd} hälsopoäng i skada.")

                # Om fienden är fångad av ett lasso tar den extra skada
                if fiende_fångad == True:
                    print (f"Eftersom fienden är fångad fick den {skada_lasso} extra i skada.")
                    
                    # Drar av den extra skadan från lassot
                    fiendens_hp = fiendens_hp + skada_lasso

                # Berättar hur många hälsopoäng fienden har kvar
                print (f"Din fiende har nu {fiendens_hp} hälsopoäng kvar.")
            else:
                print ("Och missar!")
        ### LASSO ###        
        elif (spelarens_val == "lasso" and vapen == "lasso" and fiende_fångad == False):
            ogiltigt_val = False
            print ("\nDu svingar din lasso för att fånga din fiende.")
            if (T10 <= SPELARENS_TRÄFFCHANS + modifiering_träffchans_lasso):
                # Uppdaterar variablerna för lassot
                fiende_fångad = True
                modifiering_träffchans_lasso = 2
                skada_lasso = 1
                lasso_räknare = 2
            
                # Berättar för spelaren vad som händer
                print ("Och träffar!")
                print (f"Din fiende är fångad vilket ökar din träffchans med {modifiering_träffchans_lasso} och skada med {skada_lasso} på alla attacker du gör nästa runda.")
            else:
                print ("Och missar!")
        else:
            print ("Ogiltigt val.")
            ogiltigt_val = True
    
    tryck_på_valfri_tangent()

    # Returnerar de uppdaterade värdena
    return fiendens_hp, fiende_fångad, modifiering_träffchans_lasso, skada_lasso, lasso_räknare  

# Funktion som visar en introtext
def visa_introtext(vapen):
    print ("Ni befinner er på en romersk arena omgivna av en förväntansfull publik")
    print (f"I din hand har du vapnet {vapen}. Du är klädd i ett par")
    print ("korta läderbyxor, ett par pälsstövlar och armband gjorda av läder.")
    print ("Din bara bronsfärgade bringa lyses upp av den starka solen.")
    print ("Publiken som sitter runt omkring er ser förväntansfulla ut.")
    print ("Postemius ser ut att göra sig redo att gå till anfall.")
    print ("Striden kan börja.")

    tryck_på_valfri_tangent()

# Funktion som visar spelarens och fiendens kvarvarande hälsopoäng
def visa_hälsopoäng():
    print ("\nDu har just nu " + Fore.GREEN + str(spelarens_hp) + Style.RESET_ALL + " hälsopoäng kvar.")
    print ("Din fiende har just nu " + Fore.RED + str(fiendens_hp) + Style.RESET_ALL + " hälsopoäng kvar.")

# Funktion som berättar vilka attacker det är som spelaren kan göra
def visa_tillgängliga_attacker():    
    print ("\nDu har följande attacker:")
    print (f"Järnhård näve: gör mellan {LÄGSTA_SKADA_JÄRNHÅRD_NÄVE} och {HÖGSTA_SKADA_JÄRNHÅRD_NÄVE} i skada. Träffchansen är {SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_JÄRNHÅRD_NÄVE + modifiering_träffchans_lasso} av 10.")
    print (f"Kvick spark: gör mellan {LÄGSTA_SKADA_KVICK_SPARK} och {HÖGSTA_SKADA_KVICK_SPARK} i skada. Träffchansen är {SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_KVICK_SPARK + modifiering_träffchans_lasso} av 10.")
    if (vapen == "kortsvärd"):
        print (f"Kortsvärd: gör mellan {LÄGSTA_SKADA_KORTSVÄRD} och {HÖGSTA_SKADA_KORTSVÄRD} i skada. Träffchansen är {SPELARENS_TRÄFFCHANS + MODIFIERING_TRÄFFCHANS_KORTSVÄRD + modifiering_träffchans_lasso} av 10.")
    elif (vapen == "lasso" and fiende_fångad == False):
        print (f"Lasso: fångar in din motståndare och ökar din träffchans och skada så länge som fienden är fångad.")
    
    if (fiende_fångad == True):
                print (f"Eftersom fienden är insnärjd i ditt lasso ökar din träffchans med {modifiering_träffchans_lasso}.")

# Funktion som lägger in en paus i spelet            
def tryck_på_valfri_tangent():            
    print("\nTryck på valfri tangent för att fortsätta...")
    msvcrt.getch()  # Väntar på att användaren trycker på en tangent
    print ("\n")

# Funktion som låter spelaren välja ett vapen till sin gladiator innan spelet startar.
def välj_vapen(vapen, modifiering_träffchans_lasso):
    print ("Innan striden kan börja behöver du välja ditt vapen.")
    print ("1. Kortsvärd (ger extra skada)")
    print ("2. Lasso (fångar din fiende)")

    vapenval_pågår = True 

    while (vapenval_pågår):
        val_av_vapen = input("\nVad väljer du? ").lower()
    
        if (val_av_vapen == "1" or val_av_vapen == "kortsvärd"):
            vapen = "kortsvärd"
            vapenval_pågår = False
        elif (val_av_vapen == "2" or val_av_vapen == "lasso"):    
            vapen = "lasso"
            modifiering_träffchans_lasso = -2
            vapenval_pågår = False
        else:
            print ("Ogiltigt val. Välj igen.")

    print (f"\nDu valde {vapen} som ditt vapen.")
    
    tryck_på_valfri_tangent()

    # Uppdaterar variablerna med nya värden
    return vapen, modifiering_träffchans_lasso


### INTRO TILL SPELET ###

# Introtext
print ("\n\n" + Fore.BLUE + "GLADIATORERNA" + Style.RESET_ALL)
print (Fore.YELLOW + "=============" + Style.RESET_ALL)
print ("Du är gladiatorn " + Fore.GREEN + "Rikke" + Style.RESET_ALL + ", nu ska du slåss mot gladiatorn " + Fore.RED + "Postumius.\n" + Style.RESET_ALL)

# Spelaren får välja om den vill se blodiga beskrivningar i spelet
menyval_pågår = True

while (menyval_pågår):
    svar_blodbeskrivningar = input ("Vill du se beskrivningar med mycket blod i spelet (ja/nej)? ").lower()

    if (svar_blodbeskrivningar == "ja"):
        blodiga_beskrivningar = True
        print ("Du valde att få se blodiga beskrivningar i spelet.")
        tryck_på_valfri_tangent()
        menyval_pågår = False
    elif (svar_blodbeskrivningar == "nej"):
        blodiga_beskrivningar = False
        print ("Du vill inte få se blodiga beskrivningar i spelet.")
        tryck_på_valfri_tangent()
        menyval_pågår = False
    else:
        print ("Ogiltigt val. Välj igen!\n")

# Spelaren får välja ett vapen till sin gladiator
vapen, modifiering_träffchans_lasso = välj_vapen(vapen, modifiering_träffchans_lasso)

# Visar introtexten till spelet
visa_introtext(vapen)


### STRIDEN BÖRJAR HÄR ###

while (strid_pågår):
    ### VISA STATUS I STRIDEN ###
    
    # Använder klassen Runda för att Visa vilken runda det är och uppdatera den
    runda = spelets_runda.visa_och_uppdatera()

    # Visa om fienden är fångad av lasso + uppdatera räknaren
    if (lasso_räknare > 0):
        print ("\nDin fiende är fortfarande fångad av lassot.")
        lasso_räknare = lasso_räknare - 1
    elif (lasso_räknare == 0):
        print ("\nDin fiende bryter sig loss ur lassot men du plockar snabbt upp det igen.")
        lasso_räknare = -1
        fiende_fångad = False
        modifiering_träffchans_lasso = 0
        skada_lasso = 0

    # Visa antal hälsopoäng som spelaren och fienden har
    visa_hälsopoäng()

    # Berättar vilka attacker som spelaren kan göra
    visa_tillgängliga_attacker()
    

    ### SPELAREN ATTACKERAR! ###

    # Se vad spelaren väljer att göra och uppdatera fiendens_hp baserat på resultatet
    fiendens_hp, fiende_fångad, modifiering_träffchans_lasso, skada_lasso, lasso_räknare = spelaren_väljer(fiendens_hp, fiende_fångad, modifiering_träffchans_lasso, skada_lasso, lasso_räknare)

    
    ### FIENDEN ATTACKERAR! ###

    # Se vad fienden väljer att göra och uppdatera spelarens_hp baserat på resultatet
    if (fiende_fångad == False):
        spelarens_hp = fienden_väljer(spelarens_hp)
    elif (fiende_fångad == True):
        print ("Din fiende är fångad och kan inte attackera denna runda.\n")

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