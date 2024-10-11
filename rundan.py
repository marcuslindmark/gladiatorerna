# Vi importerar Colorama för att kunna använda färger i utskriften. 
# Notera att vi bara initierar Colorama en gång i spelets huvudfil (gladiatorerna.py), 
# men vi behöver ändå importera den i varje fil där vi vill använda dess funktioner.
import colorama                         
from colorama import Fore, Style

# Här skapar vi en klass som heter 'Runda' som ska hantera rundorna i spelet. 
# En klass är som en mall för att skapa objekt, i detta fall objekt som håller reda på vilken runda spelet är på.
class Runda:
    def __init__(self):
        # __init__ är en speciell metod som kallas när vi skapar ett nytt objekt av klassen.
        # Här använder vi den för att sätta en startvärde för rundan till 1. 
        # Notera att vi nu har flyttat variabeln 'runda' till klassen, så den behövs inte längre i huvudfilen.
        self.runda = 1  

    # Detta är en metod som vi definierar inne i klassen. En metod fungerar likt en funktion, 
    # men den är kopplad till ett objekt av klassen. Den här metoden visar rundnummer och uppdaterar det till nästa runda.
    def visa_och_uppdatera(self):
        # Vi skriver ut vilken runda som spelas, och använder färger från Colorama för att göra texten mer engagerande.
        print(Fore.RED + "Ni spelar runda nummer " + Fore.YELLOW + str(self.runda) + Style.RESET_ALL + ".")
        
        # Vi uppdaterar rundan genom att öka värdet med 1 för att förbereda för nästa omgång.
        self.runda = self.runda + 1  
