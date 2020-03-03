from random import randint
import random
import datetime
import os
import re

def name_function(n_text):
    """Parameters:
       n_name  Begin waarde om de while loop in te gaan.
       n_text  De text die meegegeven wordt bij de input
       n_name  De verkregen naam.
       Deze functie vraagt om een naam in te vullen."""
    n_name = ''
    while n_name == '':
        n_name = input(n_text)
    return n_name

def print_function(p_text):
    """Parameters:
       p_text  De text die meegegeven en uitgeprint wordt.
       Deze functie print alles wat als variabel wordt meegegeven."""
    print(p_text)

def random_function():
    """"Parameters:
        r_hungry, r_dirt en r_mood bevatten allemaal een random getal
        tussen de 0 en 4.
        Deze functie slaat 3 willekeurige getallen op voor de status
    van de tamagotchi. Deze 3 variabelen worden terug gestuurt in de
    return."""
    r_hungry = randint(0, 4)
    r_dirt = randint(0, 4)
    r_mood = randint(0, 4)
    return r_hungry, r_dirt, r_mood

def petfile_function():
    """Parameters:
       Petfile  Deze opent het pet_pictures bestand en leest deze.
       pet_dict is een lege dictionarie.
       deel1 t/m deel5 bevatten de onderdelen van het tamagotchi plaatje
       pet_dict  bevat de losse onderdelen gekoppeld aan een nummer.
       Deze functie zet 3 onderdelen van de tamagotchi om naar een
    dictionarie en stuurt de dictionarie terug."""
    petfile = open('pet_pictures.txt', 'r', encoding='utf-8-sig')
    pet_dict = {}
    for line in petfile:
        devide = line.strip().split(':')
        try:
            leeg, deel1, deel2, deel3 = devide[1].split(';')
        except ValueError:
            leeg, deel1, deel2, deel3, deel4 = devide[1].split(';')
        pet_dict[int(devide[0])] = [deel1, deel2, deel3]
    return pet_dict

def mainmenu_function():
    """Parameters:
       answer  bevat een string 'go' om de while loop in te gaan.
       m_choice bevat een input van de gebruiker, de gemaakte keuze.
       m_choice wordt terug gestuurd.
       Deze functie print het hoofdmenu, zorgt dat de gebruiker
    een keuze maakt en dat de keuze wordt terug gestuurd."""
    answer = 'go' 
    while answer == 'go':
        print_function('\nWat wil je doen?\n1. Voeding toevoegen\n\
2. Tamagotchi spelen\n3. De ranking bekijken\n4. Afsluiten\n')
        m_choice = input('Maak een keuze: ')
        if m_choice == '1' or m_choice == '2'\
           or m_choice == '3' or m_choice == '4':
            return m_choice
        else:
            print_function('\nDit is geen geldige optie.')

def first_option_function():
    """Parameters:
       f_food input van de gebruiker met welke voeding.
       f_count checkt de input op rare tekens, lettertelling en
       kleine letters.
       Deze functie vraagt om het invoeren van eten, controleert
    of het eten voldoet aan de eisen en stuurt deze door naar andere
    functies. Uiteindelijk stuurt de functie een bericht terug."""
    f_food = input('\nVoer voeding in (voorbeeld:'
                 'wortel, snickers, spitskool, etc.: \n')
    f_count = len(re.sub("[^a-zA-Z]", "", f_food).lower())
    if f_count > 3 and f_count < 38:
        voedsel = foodfile_function()
        zin = check_function(voedsel, f_food)
        sort_function()
        return zin
    else:
        return '\nWoorden mogen niet korter zijn dan'\
               ' 3 letters en niet langer dan 38 letters.'

def foodfile_function():
    """Parameters:
       foodfile opent en leest het voeding.txt bestand.
       f_voedsel een dictionarie die alle voeding bevat met daarbij
       'g' of 'o'.
       f_voedsel wordt terug gestuurd.
       Deze functie zet het voedingsbestand om naar een dictionarie.
    Vervolgens stuurt de functie de dictionarie terug."""
    foodfile = open('voeding.txt', 'r')
    f_voedsel = {}
    for line in foodfile:
        f_first, f_second = line.strip().split(':')
        f_voedsel[f_first.strip()] = f_second.strip(':')
    foodfile.close()
    return f_voedsel

def check_function(c_voedsel, c_food):
    """Parameters:
       c_foodfile leest het voeding.txt bestand en voegt de nieuwe
       voeding toe aan het bestand.
       Deze functie controleerd of het opgegeven eten al voorkomt
    in de dictionarie en geeft hier een bericht over terug."""
    if c_food not in c_voedsel:
        soort = health_unhealth_function()
        c_foodfile = open('voeding.txt', 'a')
        c_foodfile.write(c_food + ':' + soort + '\n')
        c_foodfile.close()
        return "\nDe voeding '" + c_food + "' is toegevoegd!"
    else:
        return '\nVoeding bestaat al.'

def health_unhealth_function():
    """Parameters:
       value  Is een input van de gebruiker die vraagt of de voeding
       gezond of ongezond is.
       value wordt terug gestuurd.
       Deze functie vraagt aan de gebruiker of de voeding
    gezond of ongezond is en stuurd dit terug."""
    value = input('Is de voeding gezond(g) of ongezond(o): ')
    while value != 'g' and value != 'o' :
        print_function('\nDit is geen geldige optie(kies (g) of (o): ')
        value = input('Is de voeding gezond(g) of ongezond(o): ')
    return value

def sort_function():
    """Parameters:
       file  leest en opent het voeding.txt bestand.
       lines  slaat de regels van het bestand op.
       file   opent en voegt iets toe aan het voeding.txt bestand.
       Deze functie sorteert het 'voeding.txt' bestand na
    het ingevoerde eten."""
    file = open('voeding.txt', 'r')
    lines = file.readlines()
    lines.sort(key=lambda item: (len(item),item))
    file.close()
    file = open('voeding.txt', 'w')
    file.writelines(lines)
    file.close()

def second_option_function():
    """Parameters:
       o_pet  vraagt naar een naam voor de tamagotchi en slaat deze op.
       o_text is een opgeslagen bericht aan de gebruiker.
       Deze functie stuurt berichten door naar andere functies
    en geeft de naam en een bericht terug"""
    print_function('\nHoera er is een nieuwe tamagotchi geboren!\n'\
                   'Hmm, hoe zullen we hem/haar noemen?\n')
    o_pet = name_function('Voer een naam in: ')
    o_text = 'Succes met spelen!'
    return o_pet, o_text

def status(s_dirt, s_hungry, s_mood):
    """Parameters:
       s_dirt, s_hungry, s_mood zet de waardes gelijk aan 0 als deze
       kleiner zijn dan 0.
       Deze functie controleert of de variabelen altijd boven
       de 0 zijn."""
    if s_dirt < 0:
        s_dirt = 0
    elif s_hungry < 0:
        s_hungry = 0
    elif s_mood < 0:
        s_mood = 0
    return s_dirt, s_hungry, s_mood

def age_pet_function(a_age, a_hungry, a_dirt, a_mood):
    """Deze functie controleert de totale leeftijd voor de afbeelding
    van de tamagotchi en stuurt deze waarde terug."""
    if a_mood > 12 or a_dirt > 12:
        return 30
    else:
        if a_age < 7:
            value = 0
        elif a_age < 14:
            value = 6
        elif a_age < 21:
            value = 12
        elif a_age < 25:
            value = 18
        else:
            value = 24
    return value + emotion_pet_function(a_hungry, a_dirt, a_mood)

def emotion_pet_function(e_hungry, e_dirt, e_mood):
    """Deze functie controleert de totale emotie voor de afbeelding
    van de tamagotchi en stuurt deze terug."""
    total = sum([e_hungry, e_dirt, e_mood])
    if e_hungry > 12:
        return 6
    elif total < 6:
        return 1
    elif total < 10:
        return 2
    elif total < 14:
        return 3
    elif total < 18:
        return 4
    else:
        return 5
def screen_function(s_text, s_pet, s_age, s_tamagotchi_dict,
                    s_value, s_hungry, s_dirt, s_mood):
    """Deze functie stuurt het startmenu van optie 2 door naar de print
    functie zodat deze uitgeprint kan worden."""
    print_function('\n'*40 + s_text.center(82, ' '))
    print_function('Naam:\t' + (' '*4) + s_pet)
    print_function('{0:<12}{1:<40}{2}'.format('Leeftijd:', s_age,\
                                    s_tamagotchi_dict[s_value][0]))
    print_function('{0:<12}{1:<40}{2}'.format('Honger:', s_hungry*'•',\
                                    s_tamagotchi_dict[s_value][1]))
    print_function('{0:<12}{1:<40}{2}'.format('Afval:', s_dirt*'•',\
                                    s_tamagotchi_dict[s_value][2]))
    print_function('Ongelukkig:'+ (' ')+ s_mood*'•')

def submenu_function():
    """Deze functie print het submenu. De gebruiker kan een keuze
    maken en deze keuze wordt terug gestuurd."""
    ans = 'g'
    while ans == 'g':
        s_menu = 'Wat wil je doen?\n1. Geef te eten\n\
2. Verschoon\n3. Speel een spelletje\n4. Afsluiten\n'
        for line in s_menu.split('\n'):
            print_function(4*'\t' + line)
        s_choice = input('Maak een keuze: ')
        if s_choice == '1' or s_choice == '2' or s_choice == '3'\
           or s_choice == '4':
            return s_choice
        else:
            print_function('\nDit is geen geldige optie.')

def eat_sort_function():
    """Parameters:
       voedingfile  opent en leest het voeding.txt bestand.
       content  slaat de inhoud van voedingfile op.
       healt&unhealth bevat een lijst met gezonde/ongezonde voeding.
       e_healthy&e_unhealthy bevast een random keuze uit de lijsten.
       Deze functie sorteerd het eten in gezond en ongezond en dit wordt
    toegevoegd aan een list."""
    voedingfile = open('voeding.txt', 'r')
    content = voedingfile.readlines()
    health = []
    unhealth = []
    for item in content:
        if item[-3:] == ':g\n':
            health.append(item[:-3])
        else:
            unhealth.append(item[:- 3])
    e_healthy = random.choice(health)
    e_unhealthy = random.choice(unhealth)
    return e_healthy, e_unhealthy

def eatmenu_function(e_tamagotchi, e_gezond, e_ongezond):
    """Deze functie laat het eetmenu doorsturen naar de printfunctie en
    en vraagt aan de gebruiker om een keuze te maken. Deze wordt weer
    terug gestuurd."""
    ans = 'g'
    while ans == 'g':
        print_function('Wat geef je ' + e_tamagotchi + ' te eten?')
        print_function('1.' + e_gezond + '\n'\
                       '2.' + e_ongezond + '\n'\
                       '3.Geef niets\n')
        e_choice = input('Maak een keuze: ')
        if e_choice == '1' or e_choice == '2' or e_choice == '3':
            return e_choice
        else:
            print_function('\nDit is geen geldige optie.')

def giving_food_function(g_choice, g_hungry, g_dirt, g_mood):
    """Deze functie controleerd of de tamagotchi wel echt
    honger heeft en geeft de nieuwe statussen terug naar
    de main of de andere functie."""
    if g_hungry == 0:
        if g_choice == '3':
            g_text = 'Ik krijg hier wel trek van.'
            return g_hungry + 1, g_dirt, g_mood, g_text
        else:
            g_text = 'Ik heb geen honger.'
            return g_hungry, g_dirt, g_mood + 1, g_text
    else:
        return giving_food2_function(g_choice, g_hungry, g_dirt, g_mood)

def giving_food2_function(choice, g_hungry, g_dirt, g_mood):
    """Deze functie controleerd ook of de tamagotchi honger
    heeft en stuurt de nieuwe statussen terug."""
    if choice == '1':
        g_text = 'Nomnom'
        return g_hungry - 2, g_dirt + 1, g_mood, g_text
    elif choice == '2':
        g_text = 'Nomnomnom'
        return g_hungry - 1, g_dirt + 3, g_mood - 1, g_text
    elif choice == '3':
        g_text = 'Maar ik heb honger!'
        return g_hungry + 1, g_dirt, g_mood + 1, g_text

def clean_function(c_hungry, c_dirt, c_mood):
    """Deze functie controlerd of de tamagotchi schoon
    is of niet en stuurd de nieuwe waarden terug."""
    if c_dirt >= 2:
        c_text = 'Fris en fruitig!'
        return c_hungry + 1, c_dirt - 2, c_mood + 1, c_text
    elif c_dirt < 2:
        c_text = 'Grmpf, het is al schoon.'
        return c_hungry + 1, c_dirt, c_mood + 2, c_text

def gamemenu_function():
    """Deze functie stuurt het menu naar de print functie en vraagt de
    gebruiker om een keuze te maken. Hierna stuurt deze functie de keuze
    terug."""
    ans = 'g'
    while ans == 'g':
        print_function('\nWelk spel wil je spelen?\n1. Kop of munt\n\
2. Steen, papier schaar\n3. Toch maar niet\n')
        g_choice = input('Maak een keuze: ')
        if g_choice == '1' or g_choice == '2' or g_choice == '3':
            return g_choice
        else:
            print_function('\nDit is geen geldige optie.')

def game_choice_function(g_choice, g_hungry, g_dirt, g_mood):
    """Deze functie bepaald aan de hand van de keuze van de gebruiker
    welk spel er gespeeld gaat worden."""
    if g_choice == '1':
        g_choice = kopofmunt_menu_function()
        g_text, g_uitslag, g_choice = first_game_function(int(g_choice))
        g_hungry, g_mood = game_position_function(g_choice,
                                                  g_hungry, g_mood)
        return g_text, g_hungry, g_dirt, g_mood
    elif g_choice == '2':
        return 'Helaas..Dit spel is mij niet meer gelukt.', g_hungry,\
               g_dirt, g_mood
    elif g_choice == '3':
        return 'Jammer!', g_hungry + 1, g_dirt + 2, g_mood

def kopofmunt_menu_function():
    """Deze functie stuurt het kopofmuntmenu naar de print
    functie en laat de gebruiker een keuze maken.""" 
    ans = 'g'
    while ans == 'g':
        g_spel1 = 'Kop of munt?\n1.Kop\n2.Munt\n'
        for line in g_spel1.split('\n'):
            print_function(4 * '\t' + line)
        g_spelerskeuze = input('Maak een keuze: ')
        if g_spelerskeuze == '1' or g_spelerskeuze == '2':
            return g_spelerskeuze
        else:
            print_function('\nDit is geen geldige optie.')

def first_game_function(f_choice):
    """Deze functie neemt een random getal en linkt dit aan kop of munt.
    Hierna stuurt de functie de uitslag als tekst terug."""
    g_uitslag = randint(1, 2)
    if g_uitslag != f_choice:
        g_speluitslag = 'gewonnen!'
    elif g_uitslag == f_choice:
        g_speluitslag = 'verloren.'
    if g_uitslag == 1:
        g_uitslag = 'kop'
    elif g_uitslag == 2:
        g_uitslag = 'munt'
    return 'Uitslag: ' + g_uitslag + '. Tamagotchi heeft ' + g_speluitslag,\
           g_uitslag, g_speluitslag

def game_position_function(g_speluitslag, g_hungry, g_mood):
    """Deze functie geeft dee nieuwe statussen terug na het
    kopofmuntspel."""
    if g_speluitslag == 'gewonnen!':
        return g_hungry + 1, g_mood - 2
    elif g_speluitslag == 'verloren.':
        return g_hungry + 1, g_mood + 2

def position_function(p_rank, p_total_score):
    """Deze functie bepaald de positie van de gebruiker
    en stuurt de positie terug."""
    p_rankingfile = open('ranking.txt', 'r')
    ranking_2 = p_rankingfile
    next(ranking_2)
    for p_line in ranking_2:
        p_line = p_line.strip('\n')
        p_index = max([x for x, y in enumerate(p_line) if y == ';'])
        p_rank += 1
        if p_rank == 10:
            p_rankingfile.close()
            return 0, 'Sorry, je score is niet goed genoeg.'
        elif p_total_score > int(p_line[p_index + 1:]):
            p_rankingfile.close()
            return p_rank, 'Daarmee sta je op positie ' + str(p_rank) +\
                   ' in de ranking!\n'

def change_part1_function(c_nameplayer, c_pet, c_age, c_total_score,
                          c_end_position, c_value, c_number):
    """Deze functie vervangt het ranking bestand voor een
    nieuw ranking zodat de ranking bijgewerkt kan worden."""
    rankingfile = open('ranking.txt', 'r')
    new = open('voorbeeld.txt', 'w')
    new.write(rankingfile.readline())
    position = str(c_end_position) + ';'
    change_part2_function(rankingfile, c_nameplayer, c_pet, c_age,
                          c_total_score, position, c_value,
                          c_number, new)
    new.close()
    rankingfile.close()
    os.remove('ranking.txt')
    os.rename('voorbeeld.txt', 'ranking.txt')

def change_part2_function(ranking_file, c_nameplayer, c_pet, c_age,
                          c_total_score, c_position, c_value,
                          c_number, c_new):
    """Deze functie stuurt alle variabelen die nodig zijn
    voor het nieuwe ranking bestand door naar een nieuwe functie.
    Tenzij de positie buiten de ranking valt."""
    date = datetime.datetime.now()
    for line in ranking_file:
        index = line.find(';')
        change_part3_function(c_position, line, date,
                              c_nameplayer, c_pet, c_age,
                              c_total_score, c_number,
                              c_new, c_value, index)
        if c_number == 10:
            break
        c_number += 1

def change_part3_function(c_position, c_line, c_date, c_nameplayer,\
                          c_pet, c_age, c_total_score, c_number,\
                          c_new, c_value, c_index):
    """Deze functie werkt daadwerkelijk het bestand bij zodat de
    naam enz. op de goede plek in de ranking komt te staan."""
    if c_position[:2] == c_line[:2]:
        c_date = '%s/%s/%s' % (c_date.day, c_date.month, c_date.year)
        c_new.write('%s%s\t%s;%s;%s;%s\n' \
                    % (c_position, c_date, c_nameplayer, c_pet,
                       c_age, c_total_score))
        c_new.write(str(c_number)+ c_line[c_index:])
        c_value += 1
    else:
        if c_number > 1 and c_value > 0:
            c_new.write(str(c_number) + c_line[c_index:])
        else:
            c_new.write(c_line)

def grown_check(g_total_mood):
    """Deze functie controleert de totale gemoedstoestand
    van de tamagotchi.Hierbij wordt het getal gereturnt voor de
    afbeelding van de tamagotchi."""
    if -1 < g_total_mood < 6:
        return 25
    elif g_total_mood < 10:
        return 26
    elif g_total_mood < 14:
        return 27
    elif g_total_mood < 18:
        return 28
    else:
        return 29

def ranking_function():
    """Deze functie leest de ranking file en split op de ';'.
    Hierbij wordt ook de ranking door gestuurd naar de print functie."""
    rankingfile = open('ranking.txt', 'r')
    r_ranking = (''.join(rankingfile.readlines()).replace(';', '\t\t'))
    rankingfile.close()
    print_function(r_ranking)

def dead_check(d_age):
    """Deze functie controleert of de tamagotchi dood is. Dit hangt af\
    van de leeftijd van de tamagotchi."""
    if -1 < d_age < 7:
        return 6
    elif d_age < 14:
        return 12
    elif d_age < 21:
        return 18
    elif d_age < 25:
        return 24
    else:
        return 24

def main():
    nameplayer = name_function('Wat is je naam? ')
    hungry, dirt, mood = random_function()
    tamagotchi_dict = petfile_function()
    age = 0
    choice = 0
    score = 0
    while choice != '4':
        choice = mainmenu_function()
        if choice == '1':
            print(first_option_function())
        elif choice == '2':
            pet, text = second_option_function()
            while age < 25 and hungry <= 12 and\
                  dirt <= 12 and mood <= 12:
                dirt, hungry, mood = status(dirt,hungry,mood)
                key = age_pet_function(age, hungry, dirt, mood)
                screen_function(text, pet, age, tamagotchi_dict,
                                key, hungry, dirt, mood)
                choice = submenu_function()
                if choice == '1':
                    healthy, unhealthy = eat_sort_function()
                    choice = eatmenu_function(pet, healthy, unhealthy)
                    hungry, dirt, mood, text = \
                            giving_food_function(choice, hungry, dirt, mood)
                    age += 1
                    score += hungry + dirt + mood
                elif choice == '2':
                    hungry, dirt, mood, text = clean_function(hungry,
                                                              dirt, mood)
                    age += 1
                    score += hungry + dirt + mood
                elif choice == '3':
                    choice = gamemenu_function()
                    text,hungry, dirt, mood =\
                                 game_choice_function(choice, hungry,
                                                      dirt, mood)
                    age += 1
                    score += hungry + dirt + mood
                elif choice == '4':
                    print('Het spel wordt niet opgeslagen.')
                    choice = '1'
                    break
                else:
                    print('\nDit is geen geldige optie.\n')
            else:
                rank = 0
                total_score = (900-score) * age
                end_position, end_text = position_function(rank, total_score)
                if end_position > 0:
                    value = 0
                    number = 2
                    change_part1_function(nameplayer, pet, age, total_score,
                                          end_position, value, number)
                if age == 25:
                    total_mood = hungry + dirt + mood
                    grown = grown_check(total_mood)
                    text = 'Hoera, ' + pet + ' is volwassen!'
                    screen_function(text, pet, age, tamagotchi_dict,
                                    grown, hungry, dirt, mood)
                if mood > 12 or dirt > 12:
                    if dirt > 12:
                        text = 'Ik ga weg, er is teveel rommel.'
                    else:
                        text = 'Vaarwel. Ik had er meer van verwacht..'
                    getal = 30 
                    screen_function(text, pet, age, tamagotchi_dict,
                                    getal, hungry, dirt, mood)
                if hungry > 12:
                    dead = dead_check(age)
                    text = 'Je moet de Tamagotchi wel te eten geven..'
                    screen_function(text, pet, age, tamagotchi_dict,
                                    dead, hungry, dirt, mood)
                print('Eindscore: ', total_score)
                print(end_text)
                if end_position != 0:
                    ranking_function()
                print('\n') 
        elif choice == '3':
            ranking_function()
    print('Bedankt voor het spelen, tot de volgende keer.')
  
main()
