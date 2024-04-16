# EN VANLIG DAG

# programmet är skrivet lite som en rysk docka i att det är funktioner i funktioner i funktioner,
# detta så att programmet alltid ska ha någonting att falla tillbaka till
# (om användaren ger ett oregistrerat värde till en input).


# IMPORT

# os används för ta bort all text i konsolen för nästa steg
import os
import PySimpleGUI as sg
import time

# VARIABLER
global ending
ending = []

global death
death = []

# (reset)
def reset():
    "Nästan alla variabler måste vara globala så de kan nollställas"
    os.system('cls')

    global intro
    intro = ""

    global val
    val = ""

    global tid
    tid = 0

    global vakenhet
    vakenhet = ""

    global frukost
    frukost = ""

    global dagsplan
    dagsplan = ""

    global droger
    droger = []

    global tunnan
    tunnan = ""

    global spelare
    spelare = []

    global skolval
    skolval = ""

    global korridor
    korridor = ""

    global läraren
    läraren = ""

    global böcker
    böcker = ""

    global läst
    läst = 0

    global trafik
    trafik = 0

    global riktning
    riktning = 0

    global tunnel
    tunnel = ""

    global inspektion
    inspektion = ""

    global vampyren
    vampyren = ""

    global stash
    stash = ""

    global räkning
    räkning = 0

    global hittad
    hittad = 0

    global galler
    galler = ""

    global antiklimax
    antiklimax = ""

    global gurg
    gurg = ""

    global romans
    romans = ""

    global agent
    agent = ""

    global gurg_the_groom
    gurg_the_groom = ""

    global nekad
    nekad = ""

    global sim
    sim = ""

    global respekt
    respekt = ""

# TUTORIAL
försök = 0
def tutorial():
    """körs bara en gång när programmet startas första gången"""

    global intro
    os.system('cls')
    while True:
        intro = """
        Hej! Välkommen till Sixten Wilde och Sigge Nilssons Spel:
         ______                          _ _             _             
        |  ____|                        | (_)           | |            
        | |__   _ __   __   ____ _ _ __ | |_  __ _    __| | __ _  __ _ 
        |  __| | '_ \  \ \ / / _` | '_ \| | |/ _` |  / _` |/ _` |/ _` |
        | |____| | | |  \ V / (_| | | | | | | (_| | | (_| | (_| | (_| |
        |______|_| |_|   \_/ \__,_|_| |_|_|_|\__, |  \__,_|\__,_|\__, |
                                              __/ |               __/ |
        (Körs i fullskärmsläge)              |___/               |___/ 
        Spelet är designat för att köras flera gånger och hitta så många avslut (Death + Ending) du kan, därför kan du alltid starta om genom att skriva: 0.
        För att välja en handling skriv dess siffra längst ned i konsolen (detta är i konsolen) och tryck på return (ny rad knappen), till exempel:

        Starta: 1
        (först måste du klicka här)→ """


        window = sg.Window('', layout=[
        [sg.Text('för att starta klicka START', font='arial 20')],
        [sg.Button('START')]
        ])

        while True:
            event, value = window.read()
            
            if event == sg.WIN_CLOSED:
                break

            if event == 'START':
                window.close()
                start()

#starta och starta om programmet
def start():
    """återställer programmet, initierar sovrummet"""
    while True:
        global event
        event = ''
        global ending
        global death
        global försök
        försök = försök + 1

        reset()

        print(f"""(hittade avslut {len(ending)+len(death)}/17)

        EN VANLIG DAG
        försök: {försök}
        """)
    
        sovrum()

# Sovrum
def sovrum():
    """start rum, inget speciellt"""
    while True:
        global ending
        global death
        global vakenhet
        global tid

        vakenhet = """
        du vaknar, vad gör du?

        Somna om: 1.
        Gå upp: 2.
        → """

        window = sg.Window('Sovrum', layout=[
        [sg.Text('', key='-snooze-')],
        [sg.Text('Du vaknar, vad gör du?', font='arial 20')],
        [sg.Button('somna om'), sg.Button('gå upp')]
        ])

        while True:
            event, value = window.read()
            
            if event == sg.WIN_CLOSED:
                break

            if event == 'gå upp':
                window.close()
                köket()

            if event == 'somna om':
                if tid < 10:
                    tid += 1
                    window['-snooze-'].update(f'du somnade om {tid} gången')

                if tid == 10:
                    global ending
                    if ending.count("Oopsy!") == 0:
                        ending = ending + ["Oopsy!"]

                    window.close()
                    window = sg.Window('Sovrum', layout=[
                    [sg.Text('''
                    på labbet sitter en överarbetad arbetare och jobbar med en server,
                    han skulle egentligen fått åka hem för många timmar sedan.
                    på en annan server börjar en lampa blinka vilket betyder att något importerats?
                    han ställer sig upp för att se vad som hänt,
                    han märker inte att en sladd har virat sig runt hans ben,
                    när han går rycks den ur servern han jobbat på.
                    Servern med namnet "vintergatan" slocknar.''')],
                    [sg.Text(f'''Ending: Oopsy!
                    {len(ending)}/10 endings''', font='arial 20')],
                    [sg.Button('börja om?')]
                    ])

                    event, value = window.read()

                    # global val
                    
                        
                    # val = input(f"""
                    
                    # Ending: Oopsy!
                    # {len(ending)}/10 endings hittade
                    # börja om: 0
                    # → """)
                    if event == sg.WIN_CLOSED:
                        break

                    if event == "börja om?":
                        window.close()
                        start()

            if event == 'gå upp':
                if tid > 2:
                    if tid > 4:
                        if death.count("skördad") == 0:
                            death = death + ["skördad"]

                        window.close()
                        window = sg.Window('Sovrum', layout=[[sg.Text(f'''
                        (Du har snoozat så länge att världen omkring dig har förändrats.)
                        Du vaknar i nån slags pod, en alien märker att du vaknat.
                        Det trycker på en knapp och metalliska klor kommer ut ur väggarna... och in i dig.''')],
                        [sg.Text(f'''Death: skördad
                        {len(death)}/7 Deaths hittade''', font='arial 20')],
                        [sg.Button('börja om?')]])

                        event, value = window.read()

                        
                        
                        if event == "börja om?":
                            window.close()
                            start()
                    else:
                        if death.count("Wasteland") == 0:
                            death = death + ["Wasteland"]

                        window.close()
                        window = sg.Window('Sovrum', layout=[[sg.Text(f'''
                        (Du har snoozat så länge att världen omkring dig har förändrats.)
                        Du vaknar på en grå planet täck av damm... det finns inget kvar.''')],
                        [sg.Text(f'''Death: Wasteland
                        {len(death)}/7 Deaths hittade''', font='arial 20')],
                        [sg.Button('börja om?')]])

                        event, value = window.read()


                        
                        if event == "börja om?":
                            window.close()
                            start()
                    

        os.system('cls')

        if vakenhet == "0":
            start()
        while vakenhet == "1":
            if tid < 9:
                tid = tid+1
                print(f"""
                du somnar om {tid} gången
                """)
                sovrum()

            # while tid == 9:
            #     print("""
            #     på labbet sitter en överarbetad arbetare och jobbar med en server,
            #     han skulle egentligen fått åka hem för många timmar sedan.
            #     på en annan server börjar en lampa blinka vilket betyder att något importerats?
            #     han ställer sig upp för att se vad som hänt,
            #     han märker inte att en sladd har virat sig runt hans ben,
            #     när han går rycks den ur servern han jobbat på.
            #     Servern med namnet "vintergatan" slocknar.
            #     """)
            #     global val
            #     global ending
            #     if ending.count("Oopsy!") == 0:
            #         ending = ending + ["Oopsy!"]
            #     val = input(f"""
                
            #     Ending: Oopsy!
            #     {len(ending)}/10 endings hittade
            #     börja om: 0
            #     → """)
            #     if val == "0":
            #         start()
            
        # while vakenhet == "2":
        #     if tid > 2:
        #         print("du har snoozat så länge att världen omkring dig har förändrats")
        #     while 5 > tid > 2:
        #         print("""
        #         Du vaknar i nån slags pod, en alien märker att du vaknat.
        #         Det trycker på en knapp och metalliska klor kommer ut ur väggarna... och in i dig.
        #         """)
        #         if death.count("skördad") == 0:
        #             death = death + ["skördad"]
        #         val = input(f"""
                
        #         Death: skördad
        #         {len(death)}/7 Deaths hittade
        #         börja om: 0
        #         → """)
        #         if val == "0":
        #             start()

        #     while tid > 4 :
        #         print("""
        #         Du vaknar på en grå planet täck av damm... det finns inget kvar.
        #         """)
        #         if ending.count("Wasteland") == 0:
        #             ending = ending + ["Wasteland"]
        #         val = input(f"""
                
        #         Ending: Wasteland
        #         {len(ending)}/10 endings hittade
        #         börja om: 0
        #         → """)
        #         if val == "0":
        #             start()
            
        #     if tid < 3:
        #         print("du går till köket för att äta frukost")
        #         köket()
#Köket
def köket():
    """köket, här kan du välja frukost, har liten effekt på spelets slut"""
    global frukost
    window = sg.Window('köket', layout=[
        [sg.Text("""
    Du går till köket för att äta frukost.
    I köket står en svart tunna med en hazard symbol på,
    den osar en grön gas.
    bakom ugnen ligger en macka som varit där så länge du kan minnas.
    Ur skafferiet nästan lyser ett fantastiskt paket med smaskiga cornflakes från kellogs.
    vad gör du för frukost?
    """)],
    [sg.Button('sniffa på tunnan')],
    [sg.Button('kellogs cornflakes™')],
    [sg.Button('Mackan')],
    ])
    event, value = window.read()

    if frukost == "0":
        start()

    if event != 'sniffa på tunnan':
        window.close()
        hallen()

    while event == "sniffa på tunnan":
        global droger
        for i in droger:
            if i == "gas":
                droger.remove("gas")
        droger = droger + ["gas"]
        print(f"du har tagit drogerna {droger}")

        while event == "sniffa på tunnan":
            global tunnan
            window.close()
            window = sg.Window('köket', layout=[
            [sg.Text("""
            Allting snurrar, det känns ganska bra?
            """)],
            [sg.Button('Quit while youre ahead')],
            [sg.Button('Drick gift (som en idiot)')],
            ])
            event, value = window.read()

            os.system('cls')

            if tunnan == "0":
                start()
            while event == "Quit while youre ahead":
                window.close()
                köket()
            while event == "Drick gift (som en idiot)":
                global spelare
                spelare = spelare + ["cancer"]
                print(f"du har {spelare}")
                window.close()
                hallen()
#Hallen
def hallen():
    global ending
    """vilken ordning vill du utforska världen, korrekt är först skolan sedan äventyr, stanna hemma ger en ending"""
    global dagsplan

    window = sg.Window('hallen', layout=[
        [sg.Text("""
        Du funderar på vad du vill göra idag?
        """)],
    [sg.Button('gå till skolan')],
    [sg.Button('gå ut på äventyr')],
    [sg.Button('stanna hemma')]
    ])
    event, value = window.read()

    os.system('cls')

    if dagsplan == "0":
        start()

    while event == "stanna hemma":
        global ending
        window.close()
        window = sg.Window('hemma', layout=[
        [sg.Text("Du stannar hemma och chillar hela dagen")],
        [sg.Text(f'''
            Ending: Gött!
            {len(ending)}/10 endings hittade''', font='arial 20')]
        ])
        event, value = window.read()        

        if ending.count("Gött!") == 0:
            ending = ending + ["Gött!"]
        val = input(f"""
            

            börja om: 0
            → """)
        if val == "0":
            start()

    while event == "gå till skolan":
        global skolval
        window.close()
        window = sg.Window('skolan', layout=[
        [sg.Text("""
        Det är söndag... skolan är stängd.
        Vill du försöka ta dig in ändå?
        """)],
        [sg.Button('Inbrott')],
        [sg.Button('Åka hem igen')],
        ])
        event, value = window.read()
        
        os.system('cls')
        if skolval == "0":
            start()
        while event == "Åka hem igen":
            window.close()
            hallen()

        while event == "Inbrott":
            window.close()
            skolan()

    while event == "gå ut på äventyr":
        window.close()
        gatan()

#skolan
def skolan():
    global ending
    """i skolan kan du uppnå intelligens, det kommer du behöva senare, går du för långt får du en ending"""
    global val
    global korridor
    window = sg.Window('skolan', layout=[
    [sg.Text('',key='-läst-')],
    [sg.Text("""
    du går runt i skolans korridorer, du kan fortsätta framåt in i ett kontor, vika in till biblioteket, eller vända om.
    """)],
    [sg.Button('Lämna skolan'), sg.Button('Kontor'),sg.Button('Biblioteket')]
    ])

    event, value = window.read()

    os.system('cls')
    if korridor == "0":
        start()
    while event == "Lämna skolan":
        window.close()
        hallen()
    while event == "Kontor":
        window.close()

        window = sg.Window('skolan', layout=[
        [sg.Text("""
        du stormar in ett kontor, en lärare har hört dig och kommer ut ur sitt näste.
        """)],
        [sg.Text('''BOSS FIGHT!:
        Magister V. Nordlund''',font='timesnewroman 33', key='-victor-')],
        [sg.Button('Ge upp'),sg.Button('Psychological warfare')]
        ])

        event, value = window.read()

        os.system('cls')
        if läraren == "0":
            start()
        while event == "Ge upp":
            global val
            global ending
            if ending.count("Kvarsittning") == 0:
                ending = ending + ["Kvarsittning"]

            window.close()

            window = sg.Window('skolan', layout=[
            [sg.Text(f"""
            Ending: Kvarsittning
            {len(ending)}/10 endings hittade
            """, font='arial 20')],
            [sg.Button('börja om?')]
            ])

            event, value = window.read()
            
            if event == "börja om?":
                window.close()
                start()

        while event == "Psychological warfare":
            global spelare
            while spelare.count("intelligens") == 1:
                window.close()

                window = sg.Window('skolan', layout=[
                [sg.Text("""du är inte korkad nog att besegra läraren
                """)],
                [sg.Text(f'''Ending: Kvarsittning
                {len(ending)}/10 endings hittade''', font='arial 20')]
                [sg.Button('börja om?'),]
                ])

                event, value = window.read()

                if ending.count("Kvarsittning") == 0:
                    ending = ending + ["Kvarsittning"]

                if event == "börja om?":
                    start()
                
            window.close()

            if ending.count("Fängelse") == 0:
                ending = ending + ["Fängelse"]

            window = sg.Window('skolan', layout=[
            [sg.Text("""du säger något så dumt att lärarens huvud exploderar
            """)],
            [sg.Text(f'''Ending: Fängelse
            {len(ending)}/10 endings hittade''', font='arial 20')]
            [sg.Button('börja om?'),]
            ])

            event, value = window.read()

            if event == "börja om?":
                window.close()
                start()

            
    while event == "Biblioteket":
        if spelare.count("intelligens") == 1:
            window['-läst-'].update("(det finns inget mer att lära dig i biblioteket)")
        else: 
            window.close()
            biblioteket()

#biblioteket
def biblioteket():
    """läs 3 böcker för att bli smart, läser du 10 kommer bibliotekarien"""
    global death
    global läst
    global böcker

    window = sg.Window('biblioteket', layout=[
        [sg.Text("""Du sätter dig i biblioteket""")],
        [sg.Text(f"", key='-läsning-')],

        [sg.Button('läs'),],
        [sg.Button('lämna biblioteket'),]
        ])
    while True:

        event, value = window.read()

        os.system('cls')

        if böcker == "0":
            start()

        while event == "lämna biblioteket":
            window.close()
            skolan()

        if event == "läs":
            läst = läst + 1
            window['-läsning-'].update(f"""
            du har läst i {läst} stund(er)
            """)
            
            while läst == 3:
                global spelare
                if spelare.count("intelligens") == 0:
                    spelare = spelare + ["intelligens"]

                window.close()

                window = sg.Window('biblioteket', layout=[
                [sg.Text("""du har läst klart boken, du har blivit smart.
                         Vill du läsa mer eller lämna biblioteket?""")],
                [sg.Text(f"", key='-läsning-')],
                [sg.Button('läs'),],
                [sg.Button('lämna biblioteket'),]
                ])

                event, value = window.read()

                global nörd

                os.system('cls')

                while event == "lämna biblioteket":
                    window.close()
                    skolan()
                if event == "läs":
                    läst = läst + 1
                    window['-läsning-'].update(f"""
                    du har läst böcker i {läst} stund(er)
                    """)
                    event, value = window.read()
                
            # while läst != 10:
            #     biblioteket()
            while läst == 10:
                global respekt

                window.close()

                window = sg.Window('biblioteket', layout=[
                [sg.Text("Ur en hög böcker vaknar en bibliotekarie, du får inte vara här idag")],
                [sg.Text('BOSS FIGHT: bibliotekarien', font='arial 33')],
                [sg.Button('''var tyst
                           i biblioteket'''),]
                [sg.Button('skrik och slamra'),]
                ])

                event, value = window.read()

                os.system('cls')
                if respekt == "0":
                    start()
                if event == '''var tyst
                           i biblioteket''':
                    # print("""
                    # "eh, du läser ju faktiskt riktiga böcker"
                    # hon låter dig slippa undan
                    # """)
                    window.close()
                    skolan()

                while event == "skrik och slamra":
                    global death
                    if death.count("karma") == 0:
                        death = death + ["karma"]

                    window.close()

                    window = sg.Window('biblioteket', layout=[
                    [sg.Text(f"""
                    din ligism gör att biblioteket reagerar våldsamt,
                    en hylla tippar över och krossar dig""")],
                    
                    [sg.Text(f'''Death: karma
                    {len(death)}/7 Deaths hittade''', font='arial 20')],
                    [sg.Button('börja om'),]
                    ])

                    event, value = window.read()

                    if event == "börja om":
                        window.close()
                        start()  

#övergångstället
def gatan():
    global death
    """detta är bara för att retas, fyller ingen funktion alls."""
    global trafik
    trafik = input("""
    Du står framför ett övergångställe

    Gå över: 1
    Vänta : 2
    → """)
    os.system('cls')
    if trafik == "0":
        start()
    while trafik == "1":
        global val
        global death
        if death.count("påkörd") == 0:
            death = death + ["påkörd"]
        val = input(f"""
            
            Death: påkörd
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
        if val == "0":
            start()
    while trafik == "2":
        print("Vilken tur att du väntade, den föraren var inte lämpad för bilar")
        parken()

#vägvalet
def parken():
    "här får du välja riktning igen, korrekt är grottan först sedan staden, stanna ger en ending"
    global ending
    global riktning
    riktning = input("""
    du står nu i en park, mot skogen finns en grotta, mot andra sidan finns en öppning till tunnlarna under staden, vart vill du gå?

    Grottan i skogen:       1
    Tunnlarna under Staden: 2
    Stanna i parken:        3
    → """)
    os.system('cls')
    if riktning == "0":
        start()
    while riktning == "3":
        global val
        global ending
        if ending.count("Mental health") == 0:
            ending = ending + ["Mental health"]
        val = input(f"""
        du sitter och njuter av solens värme och fåglarnas dova bakgrunds kvitter
        
        Ending: Mental health
        {len(ending)}/10 endings hittade
        börja om: 0
        → """)
        if val == "0":
            start()

    while riktning == "1":
        print("du ramlar ner i grottan")
        grottan()

    while riktning == "2":
        kloaken()

#grottan
def grottan():
    """här kan du gå vänster till staden ändå, du ska gå till höger"""
    global tunnel
    tunnel = input("""
    efter ett tag delar grottan sig i två,
    vart vill du gå?

    vänster mot under staden:  1
    höger mot under skogen:    2
    → """)
    os.system('cls')
    if tunnel == "0":
        start()
    while tunnel == "2":
        borgen()
    while tunnel == "1":
        mötesplatsen()

#vampyrens lya
def borgen():
    """här slåss du med vampyren, och får grejerna för att besegra gurg i staden, pålen krävs för att besegra vampyren, intelligens krävs för pålen."""
    global inspektion
    inspektion = input("""
    tillslut kommer du fram till en borg i grottan,
    utanför ligger en kristall, vad vill du?

    återvänd åt andra hållet i grottan: 1
    inbrott i borgen:                   2
    kolla på kristallen:                3
    → """)
    os.system('cls')
    if inspektion == "0":
        start()
    while inspektion == "1":
        grottan()
    if inspektion == "3":
        global death
        global ending
        global spelare
        global hittad
        hittad = spelare.count("intelligens")
        if hittad > 0:
            print("""
            du är smart nog att inse att kristallen är gjord av trä,
            detta är ju inte alls en kristall, det är en påle.
            """)
            if spelare.count("träpåle") == 0:
                spelare = spelare + ["träpåle"]
            print(f"du har {spelare}")
            inspektion = input("""
                vad vill du?

                återvänd åt andra hållet i grottan: 1
                inbrott i borgen:                   2
                → """)
            os.system('cls')
            if inspektion == "0":
                start()
            global räkning
            räkning = räkning +1
        if hittad < 0:
            print("du är inte smart nog för att förstå kristallen, hur du kan bli smartare?..")
            inspektion = input("""
                tillslut kommer du fram till en borg i grottan,
                utanför ligger kristallen, vad vill du?

                återvänd åt andra hållet i grottan: 1
                inbrott i borgen:                   2
                → """)
            os.system('cls')
            if inspektion == "0":
                start()
    while inspektion == "2":
        print("""
        du fortsätter framåt in i mörkret,
        innan du hinner reagera flyger något från skuggorna mot dig,
        det bränner till i din hals vilket sprider sig genom dina blodådror till hela kroppen
        """)
        if spelare.count("vampirism") == 0:
            spelare = spelare + ["vampirism"]
        print(f"du har {spelare}")
        global vampyren

        vampyren = input("""
        BOSS FIGHT: vampyren

        ge upp:                 1
        lökig andedräkt:        2
        träpåle i dess hjärta: 3
        → """)
        os.system('cls')
        if vampyren == "0":
            start()
        while vampyren == "1":
            global val
            global death
            if death.count("uppäten av vampyr") == 0:
                death = death + ["uppäten av vampyr"]
            val = input(f"""
            
            Death: uppäten av vampyr
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()

        while vampyren == "2":
            if death.count("uppäten av vampyr") == 0:
                death = death + ["uppäten av vampyr"]
            val = input(f"""
            att vampyrer dör av lök är en myt.
            
            death: uppäten av vampyr
            {len(death)}/7 deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()
    

        while vampyren == "3":
            global tunnel
            if spelare.count("träpåle") > 0:
                global stash
                stash = input("""
                vampyren, precis som alla andra, dör om man spettar dem i hjärtat, (du har besegrat vampyren).
                Bakom vampyren hittar du en klump med spagetti ett piller och en laddad pistol:

                ta grejerna:    1
                lämna grejerna: 2
                → """)
                os.system('cls')
                if stash == "0":
                    start()
                while stash == "1":
                    global droger
                    droger = droger + ["piller"]
                    print(f"du har tagit drogerna {droger}")
                    spelare = spelare + ["spagetti"]
                    spelare = spelare + ["pistol"]
                    print(f"du har {spelare}")

                    global tunnel
                    tunnel = input("""
                    vill du kika på andra sidan grottan eller vill du gå hem?

                    gå hem:                                 1
                    kolla på andra sidan mot under staden:  2
                    → """)
                    while tunnel == "2":
                        mötesplatsen()
                    while tunnel == "1":
                        flykt()

                    if tunnel == "0":
                        start()

                while stash == "2":
                    tunnel = input("""
                    vill du kika på andra sidan grottan eller vill du gå hem?

                    gå hem:                                 1
                    kolla på andra sidan mot under staden:  2
                    → """)
                    while tunnel == "2":
                        mötesplatsen()
                        os.system('cls')
                    while tunnel == "1":
                        flykt()
            if spelare.count("träpåle") < 0:
                if death.count("uppäten av vampyr") == 0:
                    death = death + ["uppäten av vampyr"]
                val = input(f"""
                du har ingen träpåle
                
                Death: uppäten av vampyr
                {len(death)}/7 Deaths hittade
                börja om: 0
                → """)
                if val == "0":
                    start()
            
def flykt():
    global death
    global ending
    print("du har sätt något du inte borde ha sätt")
    while spelare.count("vampirism") > 0: 
        print("""
        dina nya vampyr krafter låter dig ducka undan från skotten något skjutit mot dig,
        bara en bra stund efter din flykt in i skogen inser du att din hud fräter,
        """)
        if ending.count("vampyr") == 0:
            ending = ending + ["vampyr"]
        val = input(f"""
            
            Ending: vampyr
            {len(ending)}/7 endings hittade
            börja om: 0
            → """)
        if val == "0":
            start() 
        else:
            if death.count("skjuten") == 0:
                death = death + ["skjuten"]
            val = input(f"""
            
            Death: skjuten
            {len(death)}/10 Deaths hittade
            börja om: 0
            → """)
        if val == "0":
            start()
# där tunnlarna och grottorna möts
def mötesplatsen():
    """där grottan och kloaken möts, är du vampyr kan du gå igenom gallret och få en ending"""
    print("""
    du ser att kloakerna leder ned i grottorna,
    det kan inte vara bra.
    """)
    global death
    global galler
    galler = spelare.count("vampirism")
    while galler > 0:
        global antiklimax
        antiklimax = input("""
        du kan använda dina vampyr krafter för att ta din igenom gallren, eller så kan du fortsätta framåt

        genom gallret:                     1
        fortsätt framåt mot under staden: 2
        → """)
        os.system('cls')
        if antiklimax == "0":
            start()
        while antiklimax == "1":
            global death
            if death.count("MEH!") == 0:
                death = death + ["MEH!"]
            val = input(f"""
            du förvandlar dig till fladdermöss och flyger igenom gallret,
            på andra sidan ser du en skyllt där det står:
            "DEVELOPER NOTE: här finns det inget"
            du dog av antiklimax
            
            Death: MEH!
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()
        while antiklimax == "2":
            kloaken()
    else:
        kloaken()

#Stadens tunnlar
def kloaken():
    """under staden, du möter gurg, detta är sista scenen i spelet (om du gjort rätt)"""
    global death
    global ending
    global val
    print("""
    du fortsätter framåt till du plötsligt ser en siluett av vad du tror är en man, men något är off,
    det ser ut som att han smälter. Du snubblar och ljudet du gör för att återfå balansen ekar genom tunneln,
    figuren tittar på dig.
    """)
    global gurg
    global droger
    while droger.count("piller") > 0:
        gurg = input("""
        BOSS FIGHT: gurg the ...guy?

        fly: 1
        blockera: 2
        dodge'a: 3
        spaghetti: 4
        pistol: 5
        vampyr kraft: 6
        → """)
        os.system('cls')
        if gurg == "0":
            start()
        while gurg == "1":
            global death
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            val = input(f"""
            Motstånd är meningslöst,
            Gurg äter upp dig,
            
            Death: uppäten av gurg
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()
        while gurg == "2":
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            val = input(f"""
            Motstånd är meningslöst,
            Gurg äter upp dig,
            
            Death: uppäten av gurg
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()
        while gurg == "3":
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            val = input(f"""
            Motstånd är meningslöst,
            Gurg äter upp dig,
            
            Death: uppäten av gurg
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()
        while gurg == "5":
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            val = input(f"""
            Du plockar fram pistolen och skjuter vilt mot varelsen,
            du har avlossat alla skott i pistolen, några kulor träffar och gör skada... inte många nog.
            Motstånd är meningslöst,
            Gurg äter upp dig,
            
            Death: uppäten av gurg
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()

        while gurg == "6":
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            val = input(f"""
            du flyger fram och biter gurg i halsen och ger honom vampirism,
            han biter dig i halsen tillbaka och ger dig död,
            
            Death: uppäten av gurg
            {len(death)}/7 Deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()
        while gurg == "4":
            global romans
            romans = input("""
            du greppar frenetiskt efter något att och får fram spaghettin,
            du håller fram den som en sköld framför dig.
            Efter en liten stund öppnar du ögonen igen och ser att figuren rodnar,
            den har tagit spaghettin som en romantisk gest, och vänder sig om för att ge dig något i retur.

            vänta:  1
            SKJUT:  2
            → """)
            os.system('cls')

            if romans == "0":
                start()  

            while romans == "2":
                global agent
                agent =input("""
                du plockar fram pistolen, *ditt hjärta slår* du siktar, *ditt hjärta slår* och du skjuter...
                PANG! *det piiiper i dina öron* omgivningen byter färg och varelsen faller ihop på golvet.
                Bakom dig för du att en person klappar händerna "imponerande",
                när du vänder dig om ser du en person i kostym,
                de erbjuder dig ett jobb och säger att de kanske kan bota din vampirism om du godkänner.
            
                acceptera: 1
                neka:      2
                → """)
                os.system('cls')
                if agent == "0":
                    start()
                while agent == "1":
                    if ending.count("Killer") == 0:
                        ending = ending + ["Killer"]
                    val = input(f"""
                    "mycket bra val"
                    
                    Ending: Killer
                    {len(ending)}/10 endings hittade
                    börja om: 0
                    → """)
                    if val == "0":
                        start()
                while agent == "2":
                    print("""
                    "dåligt val"
                    Boss fight: agent K

                    """)
                    if death.count("avrättad") == 0:
                        death = death + ["avrättad"]
                    val = input(f"""
                    PANG! *det isar i bröstet* innan du hinner reagera har agenten skjutit dig...
                    "mycket dåligt val"
                    
                    death: avrättad
                    {len(death)}/7 deaths hittade
                    börja om: 0
                    → """)
                    if val == "0":
                        start()     

            while romans == "1":
                global gurg_the_groom
                gurg_the_groom = input("""
                gurg erbjuder dig en (självlysande) svamp som sin gåva til dig, vill du bli ihop med gurg?

                acceptera:     1
                neka:          2
                → """)
                os.system('cls')
                if gurg_the_groom == "0":
                    start()
                while gurg_the_groom == "1":
                    if droger.count("gas") > 0:
                        global sim
                        sim = input("""
                        du har tagit alla tre droger och har därför blivit upplyst,
                        du inser att du lever i en simulation... och att det finns andra serverar.

                        utforska: 1
                        återvänd: 2
                        → """)
                        os.system('cls')
                        if sim == "0":
                            start()
                        while sim == "1":
                            if ending.count("destroyer of worlds") == 0:
                                ending = ending + ["destroyer of worlds"]
                            val = input(f"""
                            Det tar en stund att åka genom sladdarna,
                            när du väl anländer har den förra servern slocknat.
                            
                            Ending: destroyer of worlds
                            {len(ending)}/10 endings hittade
                            börja om: 0
                            → """)
                            if val == "0":
                                start()
                        if sim=="2":
                            print("du återvänder till jorden")
                            droger = []
                    if ending.count("gurg jn") == 0:
                        ending = ending + ["gurg jn"]
                    val = input(f"""
                    du och gurg lever lyckliga i alla era dagar.
                    
                    Ending: Ordinary day 2?.. gurg jn the swamp monster vampire?
                    {len(ending)}/10 endings hittade
                    börja om: 0
                    → """)
                    
                    if val == "0":
                        start()  

                while gurg_the_groom == "2":
                    global nekad
                    nekad = input("""
                    gurg ser förvirrad ut

                    vänta: 1
                    skjut: 2
                    → """)
                    os.system('cls')
                    if nekad == "0":
                        start()
                    while nekad == "1":
                        print("""
                        när han inser vad du gjort blir han förargad
                        """)
                        if death.count("uppäten av gurg") == 0:
                            death = death + ["uppäten av gurg"]
                        val = input(f"""
                        Motstånd är meningslöst,
                        Gurg äter up dig,
                        
                        Death: uppäten av gurg
                        {len(death)}/7 Deaths hittade
                        börja om: 0
                        → """)
                        if val == "0":
                            start()
                    while nekad == "2":
                        agent =input("""
                        du plockar fram pistolen, *ditt hjärta slår* du siktar, *ditt hjärta slår* och du skjuter...
                        PANG! *det piiiper i dina öron* omgivningen byter färg och varelsen faller ihop på golvet.
                        Bakom dig för du att en person klappar händerna "imponerande",
                        när du vänder dig om ser du en person i kostym,
                        de erbjuder dig ett jobb och säger att de kanske kan bota din vampirism om du godkänner.
                    
                        acceptera: 1
                        neka:      2
                        → """)
                        os.system('cls')
                        while agent == "1":
                            if ending.count("Killer") == 0:
                                ending = ending + ["Killer"]
                            val = input(f"""
                            "mycket bra val"
                            
                            Ending: Killer
                            {len(ending)}/10 endings hittade
                            börja om: 0
                            → """)
                            if val == "0":
                                start()
                        while agent == "2":
                            if death.count("avrättad") == 0:
                                death = death + ["avrättad"]
                            print("""
                            "dåligt val"
                            Boss fight: agent K

                            """)
                            val = input(f"""
                            PANG! *det isar i bröstet* innan du hinner reagera har agenten skjutit dig...
                            "mycket dåligt val"
                            
                            Death: avrättad
                            {len(death)}/7 Deaths hittade
                            börja om: 0
                            → """)
                            if val == "0":
                                start()   

                        


    else:
        gurg = input("""
        BOSS FIGHT: gurg the ...guy?

        fly:       1
        blockera:  2
        dodge'a:   3
        → """)
        os.system('cls')
        while True:
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            val = input(f"""
            Motstånd är meningslöst,
            Gurg äter upp dig,
            
            death: uppäten av gurg
        {len(death)}/7 deaths hittade
            börja om: 0
            → """)
            if val == "0":
                start()

#dra igång allt
tutorial()