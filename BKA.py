#BAK_Rechner

#Gewichtsangabe
gewicht = float(input('Bitte geben Sie Ihr Gewicht an'))


#Auswahl des Geschlechtes um den Reduktionsfaktor zu bestimmen
def auswahl_Reduktionsfaktor():
    user_input = input('Sind Sie weiblich oder männlich?(w/m)').lower()
    if user_input == 'm':
        return 0.7

    elif user_input == 'w':
        return 0.6

    else:
        print ('Bitte geben Sie an ob sie weiblich oder männlich sind')
        return auswahl_Reduktionsfaktor
        
    
def berechnungALK(): #ml*(alk in % / 100)*0,8g/cm^3 / Berechnung des getrunkenen Alkohols
    alk_Menge = float(input('Bitte geben Sie Ihren Konsum in ml an'))*\
                float(input('Bitte geben Sie den Alkoholanteil in Prozen an'))*0.8
    return alk_Menge

#Berechnung der Promille = getrunkener Alk / (gewicht * reduktionsfaktor)
def berechnung_Promille(geschlecht, alk_Menge, gewicht):
    Promille = alk_Menge / (gewicht*geschlecht)
    return Promille
    
def main():
    geschlecht = auswahl_Reduktionsfaktor()
    alk_Menge = berechnungALK ()
    Promille = berechnung_Promille(geschlecht, alk_Menge, gewicht)
    print(f"Die Blutalkoholkonzentration beträgt {Promille: .2f} Promille")

main()