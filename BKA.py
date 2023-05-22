#BAK_Rechner

def reduktionsfaktor():
    user_input = input('Sind Sie weiblich oder männlich?(w/m)').lower()
    if user_input == 'm':
        geschlecht = 0.7

    elif user_input == 'w':
        geschlecht = 0.6

    else:
        print ('Bitte geben Sie an ob sie weiblich oder männlich sind')
        
    return geschlecht
    
def berechnungALK(): #ml*(alk in % / 100)*0,8g/cm^3
    alk_Menge = float(input('Bitte geben Sie Ihren Konsum in ml an'))*\
                float(input('Bitte geben Sie den Alkoholanteil in Prozen an'))*0,8
    return alk_Menge


gewicht = float(input('Bitte geben Sie Ihr Gewicht an'))


def main(alk_Menge, gewicht, reduktionsfaktor):
    return alk_Menge / (gewicht*reduktionsfaktor)
    
main()