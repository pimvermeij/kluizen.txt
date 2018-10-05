def toon_aantal_kluizen_vrij(filename):
    'toont aantal lege kluizen door aantal lege lijnen in kluizen.txt'
    infile = open(filename, 'r')
    linesList = infile.readlines()
    infile.close()

    return 12 - len(linesList)

def nieuwe_kluis(filename):
    'vraagt een nieuw kluisnummer aan, vraagt om het wachtwoorden en zet die dan als duo naar kluizen.txt'
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    infile = open(filename, 'r')
    infile.read()
    for numbers in infile.read():
        kluisnummers.remove(int(numbers))
    infile.close()
    ww = input("voer uw wachtwoord in:")
    gegeven_kluisnummer = kluisnummers[0]
    outfile = open(filename, 'a')
    kluisnummer = outfile.write(str(kluisnummers[0]))
    puntComma = outfile.write(";")
    wachtwoord = outfile.write(str(ww))
    next_line = outfile.write('\n')
    print("u heeft kluisnummer" + " " + str(gegeven_kluisnummer))
    return kluisnummer + puntComma + wachtwoord + next_line

def kluis_openen(filename):
    kluisnummer = int(input("wat is uw kluisnummer?"))
    wachtwoord = input("wat is uw wachtwoord?")
    infile = open(filename, 'r')
    infile.readlines()
    for combo in infile.readlines():
        if combo == str(kluisnummer) + ";" + str(wachtwoord):
           return("uw kluisje is geopend!")
        else:
            return("helaas klopt de combinatie van uw kluisnummer en uw wachtwoord niet!")

def kluis_teruggeven():
    ppp


print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
print("4: Ik geef mijn kluis terug")
waarde = int(input("kies een waarde:"))
if waarde == 1:
    print(toon_aantal_kluizen_vrij('kluizen.txt'))
elif waarde == 2:
    nieuwe_kluis('kluizen.txt')
elif waarde == 3:
    kluis_openen("kluizen.txt")
elif waarde == 4:
    blabla
else:
    print("kies een geldige waarde")


