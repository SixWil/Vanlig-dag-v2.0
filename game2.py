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

global lock
lock = False

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
                {len(ending)}/10 endings hittade''', font='arial 20')],
                [sg.Button('börja om?'),]
                ])

                event, value = window.read()

                if ending.count("Kvarsittning") == 0:
                    ending = ending + ["Kvarsittning"]

                if event == "börja om?":
                    start()
                

            if ending.count("Fängelse") == 0:
                ending = ending + ["Fängelse"]

            window.close()
            window = sg.Window('skolan', layout=[
            [sg.Text("""du säger något så dumt att lärarens huvud exploderar
            """)],
            [sg.Text(f'''Ending: Fängelse
            {len(ending)}/10 endings hittade''', font='arial 20')],
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
                [sg.Button('''var tyst i biblioteket'''),],
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

    window = sg.Window('gata', layout=[
    [sg.Text(f"""Du står framför ett övergångställe""")],
    [sg.Button('gå över')],
    [sg.Button('vänta')],
    ])

    event, value = window.read()
    
    os.system('cls')

    if trafik == "0":
        start()
    while event == "gå över":
        global val
        global death
        if death.count("påkörd") == 0:
            death = death + ["påkörd"]
        window.close()

        window = sg.Window('gata', layout=[
        [sg.Text(f"""Death: påkörd
        {len(death)}/7 Deaths hittade
        börja om: 0 """, font='arial 20')],
        [sg.Button('börja om?')],
        ])

        event, value = window.read()
        
        if event == 'börja om?':
            window.close()
            start()
            
    while event == 'vänta':
        window.close()
        parken()
        
        ("Vilken tur att du väntade, den föraren var inte lämpad för bilar")
        

#vägvalet
def parken():
    "här får du välja riktning igen, korrekt är grottan först sedan staden, stanna ger en ending"
    global ending
    global riktning

    window = sg.Window('gata', layout=[
    [sg.Text(''' Vilken tur att du väntade, den föraren var inte lämpad för bilar.
du står nu i en park, mot skogen finns en grotta, mot andra sidan
finns en öppning till tunnlarna under staden, vart vill du gå?''')],
    [sg.Button('Grottan i skogen')],
    [sg.Button('Tunnlarna under Staden')],
    [sg.Button('Stanna i parken')],
    ])

    event, value = window.read()
    os.system('cls')

    if riktning == "0":
        start()

    while event == "Stanna i parken":
        global val
        global ending
        if ending.count("Mental health") == 0:
            ending = ending + ["Mental health"]

        window.close()
        window = sg.Window('gata', layout=[
        [sg.Text('du sitter och njuter av solens värme och fåglarnas dova bakgrunds kvitter')],
        [sg.Text(f"""Ending: Mental health
        {len(ending)}/10 endings hittade """, font='arial 20')],
        [sg.Button('börja om?')],
        ])

        event, value = window.read()
        
        if event == "börja om?":
            window.close()
            start()

    while event == "Grottan i skogen":
        print("du ramlar ner i grottan")
        window.close()
        grottan()

    while event == "Tunnlarna under Staden":
        window.close()
        kloaken()

#grottan
def grottan():
    """här kan du gå vänster till staden ändå, du ska gå till höger"""
    global tunnel

    window = sg.Window('grotta', layout=[
    [sg.Text('''efter ett tag delar grottan sig i två,
    vart vill du gå?''')],
    [sg.Button('vänster mot under staden')],
    [sg.Button('höger mot under skogen')],
    ])

    event, value = window.read()

    os.system('cls')
    if tunnel == "0":
        start()

    while event == "höger mot under skogen":
        window.close()
        borgen()

    while event == "vänster mot under staden":
        window.close()
        mötesplatsen()

#vampyrens lya
def borgen():
    """här slåss du med vampyren, och får grejerna för att besegra gurg i staden, pålen krävs för att besegra vampyren, intelligens krävs för pålen."""
    global inspektion
    global lock
    if lock == False:
        window = sg.Window('grotta', layout=[
        [sg.Text('''tillslut kommer du fram till en borg i grottan,
        utanför ligger en kristall, vad vill du? ''')],
        [sg.Text('', key='-kristall-')],
        [sg.Button('återvänd åt andra hållet i grottan')],
        [sg.Button('inbrott i borgen')],
        [sg.Button('kolla på kristallen')],
        ])
        lock = True

        event, value = window.read()

    os.system('cls')
    if inspektion == "0":
        start()

    while event == "återvänd åt andra hållet i grottan":
        window.close()
        grottan()
    if event == "kolla på kristallen":
        global death
        global ending
        global spelare
        global hittad

        hittad = spelare.count("intelligens")
        if hittad > 0:

            window['-kristall-'].update("""
            du är smart nog att inse att kristallen är gjord av trä,
            detta är ju inte alls en kristall, det är en påle. (+ träpåle)
            """)

            event, value = window.read()
            if spelare.count("träpåle") == 0:
                spelare = spelare + ["träpåle"]
            print(f"du har {spelare}")
            # inspektion = input("""
            #     vad vill du?

            #     återvänd åt andra hållet i grottan: 1
            #     inbrott i borgen:                   2
            #     → """)
            os.system('cls')
            if inspektion == "0":
                start()
            global räkning
            räkning = räkning +1
        if hittad < 0:
            window['-kristall-'].update("du är inte smart nog för att förstå kristallen, hur du kan bli smartare?..")
            event, value = window.read()
            # inspektion = input("""
            #     tillslut kommer du fram till en borg i grottan,
            #     utanför ligger kristallen, vad vill du?

            #     återvänd åt andra hållet i grottan: 1
            #     inbrott i borgen:                   2
            #     → """)
            os.system('cls')
            if inspektion == "0":
                start()
    while event == "inbrott i borgen":
        window.close()
        window = sg.Window('grotta', layout=[
        [sg.Text('''du fortsätter framåt in i mörkret,
        innan du hinner reagera flyger något från skuggorna mot dig,
        det bränner till i din hals vilket sprider sig genom dina blodådror till hela kroppen.
                 (Du är vampyr nu)''')],
        [sg.Text('BOSS FIGHT: vampyren', font='arial 33')],
        [sg.Button('ge upp')],
        [sg.Button('lökig andedräkt')],
        [sg.Button('träpåle i dess hjärta')],
        ])

        event, value = window.read()

        if spelare.count("vampirism") == 0:
            spelare = spelare + ["vampirism"]
        global vampyren

        os.system('cls')

        if vampyren == "0":
            start()

        while event != "träpåle i dess hjärta":
            global val
            global death
            if death.count("uppäten av vampyr") == 0:
                death = death + ["uppäten av vampyr"]
            window.close()
            window = sg.Window('grotta', layout=[
            [sg.Text('', key='-vampyr-')]
            [sg.Text(f"""
            Death: uppäten av vampyr
            {len(death)}/7 Deaths hittade""")],
            [sg.Button('börja om?')],
            ])

            if event == 'lökig andedräkt':
                window['-vampyr-'].update('att vampyrer dör av lök är en myt.')

            event, value = window.read()

            if event == "börja om?":
                window.close()
                start()
    

        while event == "träpåle i dess hjärta":
            global tunnel

            if spelare.count("träpåle") > 0:
                global stash
                window.close()
                window = sg.Window('grotta', layout=[
                [sg.Text('''vampyren, precis som alla andra, dör om man spettar dem i hjärtat, (du har besegrat vampyren).
                Bakom vampyren hittar du en klump med spagetti ett piller och en laddad pistol''')],
                [sg.Button('ta grejerna')],
                [sg.Button('lämna grejerna')],
                ])

                event, value = window.read()
                
   
                os.system('cls')
                if stash == "0":
                    start()
                if event == "ta grejerna":
                    global droger
                    droger = droger + ["piller"]
                    print(f"du har tagit drogerna {droger}")
                    spelare = spelare + ["spagetti"]
                    spelare = spelare + ["pistol"]
                    # print(f"du har {spelare}")

                    global tunnel

                window.close()
                window = sg.Window('grotta', layout=[
                [sg.Text('''vill du kika på andra sidan grottan eller vill du gå hem?''')],
                [sg.Button('gå hem')],
                [sg.Button('kolla på andra sidan mot under staden')],
                ])

                event, value = window.read()

                while event == "kolla på andra sidan mot under staden":
                    window.close()
                    mötesplatsen()
                while tunnel == "gå hem":
                    window.close()
                    flykt()

                    if tunnel == "0":
                        start()

                # while stash == "2":
                #     tunnel = input("""
                #     vill du kika på andra sidan grottan eller vill du gå hem?

                #     gå hem:                                 1
                #     kolla på andra sidan mot under staden:  2
                #     → """)
                #     while tunnel == "2":
                #         mötesplatsen()
                #         os.system('cls')
                #     while tunnel == "1":
                #         flykt()
                        
            if spelare.count("träpåle") < 0:
                if death.count("uppäten av vampyr") == 0:
                    death = death + ["uppäten av vampyr"]
                window.close()
                window = sg.Window('grotta', layout=[
                [sg.Text('''(du har ingen träpåle)
                Death: uppäten av vampyr
                {len(death)}/7 Deaths hittade ''', font='arial 20')],
                [sg.Button('börja om?')],
                ])

                event, value = window.read()

                if event == "börja om?":
                    window.close()
                    start()
            
def flykt():
    global death
    global ending
    print("")
    while spelare.count("vampirism") > 0: 
        if ending.count("vampyr") == 0:
            ending = ending + ["vampyr"]

        window = sg.Window('skogen', layout=[
        [sg.Text('''du har sett något du inte borde...
        dina nya vampyr krafter låter dig ducka undan från skotten något skjutit mot dig,
        bara en bra stund efter din flykt in i skogen inser du att din hud fräter,''')],
        [sg.Text(f'''Ending: vampyr
        {len(ending)}/7 endings hittade''')],
        [sg.Button('börja om?')],
        ])

        event, value = window.read()

        if event == "börja om?":
            window.close()
            start() 
        # else:
        #     if death.count("skjuten") == 0:
        #         death = death + ["skjuten"]
        #     val = input(f"""
            
        #     Death: skjuten
        #     {len(death)}/10 Deaths hittade
        #     börja om: 0
        #     → """)
        # if val == "0":
        #     start()
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
        window = sg.Window('kloak', layout=[
        [sg.Text('''du kan använda dina vampyr krafter för att ta din igenom några galler, eller så kan du fortsätta framåt''')],
        [sg.Button('genom gallret')],
        [sg.Button('fortsätt framåt mot under staden')],
        ])

        event, value = window.read()
        
        os.system('cls')
        if antiklimax == "0":
            start()
        while event == "genom gallret":
            global death
            if death.count("MEH!") == 0:
                death = death + ["MEH!"]
            
            window.close()
            window = sg.Window('kloak', layout=[
            [sg.Text('''du förvandlar dig till fladdermöss och flyger igenom gallret,
            på andra sidan ser du en skyllt där det står:
            "DEVELOPER NOTE: här finns det inget ännu, glöm inte att lägga till något"
            du dog av antiklimax ''')],
            [sg.Text(f'''Death: MEH!
            {len(death)}/7 Deaths hittade''', font='arial 20')],
            [sg.Button('börja om?')],
            ])

            event, value = window.read()
            
            if event == "börja om?":
                window.close()
                start()

        while event == "fortsätt framåt mot under staden":
            window.close()
            kloaken()
    else:
        window.close()
        kloaken()

#Stadens tunnlar
def kloaken():
    """under staden, du möter gurg, detta är sista scenen i spelet (om du gjort rätt)"""
    global death
    global ending
    global val

    global gurg
    global droger
    while droger.count("piller") > 0:
        window.close()
        window = sg.Window('kloak', layout=[
        [sg.Text('''Du fortsätter framåt till du plötsligt ser en siluett av vad du tror är en man, men något är off,
        det ser ut som att han smälter. Du snubblar och ljudet du gör för att återfå balansen ekar genom tunneln,
        figuren tittar på dig.''')],
        [sg.Text('''BOSS FIGHT: gurg the ...guy?''', font='timesnewroman 33')],
        [sg.Button('fly')],
        [sg.Button('blockera')],
        [sg.Button('ducka')],
        [sg.Button('spaghetti')],
        [sg.Button('pistol')],
        [sg.Button('vampyr kraft')],
        ])

        event, value = window.read()

        os.system('cls')
        if gurg == "0":
            start()
        while event != "spaghetti":
            global death
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            window.close()
            window = sg.Window('kloak', layout=[
            [sg.Text('''Motstånd är meningslöst,
            Gurg äter upp dig, ''')],
            [sg.Text(f'''Death: uppäten av gurg
            {len(death)}/7 Deaths hittade''', font='arial 20')],
            [sg.Button('börja om?')],
            ])

            event, value = window.read()

            if val == "börja om?":
                window.close()
                start()
        # while gurg == "2":
        #     if death.count("uppäten av gurg") == 0:
        #         death = death + ["uppäten av gurg"]
        #     val = input(f"""
        #     Motstånd är meningslöst,
        #     Gurg äter upp dig,
            
        #     Death: uppäten av gurg
        #     {len(death)}/7 Deaths hittade
        #     börja om: 0
        #     → """)
        #     if val == "0":
        #         start()
        # while gurg == "3":
        #     if death.count("uppäten av gurg") == 0:
        #         death = death + ["uppäten av gurg"]
        #     val = input(f"""
        #     Motstånd är meningslöst,
        #     Gurg äter upp dig,
            
        #     Death: uppäten av gurg
        #     {len(death)}/7 Deaths hittade
        #     börja om: 0
        #     → """)
        #     if val == "0":
        #         start()
        # while gurg == "5":
        #     if death.count("uppäten av gurg") == 0:
        #         death = death + ["uppäten av gurg"]
        #     val = input(f"""
        #     Du plockar fram pistolen och skjuter vilt mot varelsen,
        #     du har avlossat alla skott i pistolen, några kulor träffar och gör skada... inte många nog.
        #     Motstånd är meningslöst,
        #     Gurg äter upp dig,
            
        #     Death: uppäten av gurg
        #     {len(death)}/7 Deaths hittade
        #     börja om: 0
        #     → """)
        #     if val == "0":
        #         start()

        # while gurg == "6":
        #     if death.count("uppäten av gurg") == 0:
        #         death = death + ["uppäten av gurg"]
        #     val = input(f"""
        #     du flyger fram och biter gurg i halsen och ger honom vampirism,
        #     han biter dig i halsen tillbaka och ger dig död,
            
        #     Death: uppäten av gurg
        #     {len(death)}/7 Deaths hittade
        #     börja om: 0
        #     → """)
        #     if val == "0":
        #         start()
        while gurg == "4":
            global romans
            window.close()
            window = sg.Window('kloak', layout=[
            [sg.Text('''du greppar frenetiskt efter något att och får fram spaghettin,
            du håller fram den som en sköld framför dig.
            Efter en liten stund öppnar du ögonen igen och ser att figuren rodnar,
            den har tagit spaghettin som en romantisk gest, och vänder sig om för att ge dig något i retur.''')],
            [sg.Button('vänta')],
            [sg.Button('SKJUT!')],
            ])

            event, value = window.read()

            os.system('cls')

            if romans == "0":
                start()  

            while event == "SKJUT!":
                global agent
                window.close()
                window = sg.Window('kloak', layout=[
                [sg.Text('''du plockar fram pistolen, *ditt hjärta slår* du siktar, *ditt hjärta slår* och du skjuter...
                PANG! *det piiiper i dina öron* omgivningen byter färg och varelsen faller ihop på golvet.
                Bakom dig för du att en person klappar händerna "imponerande",
                när du vänder dig om ser du en person i kostym,
                de erbjuder dig ett jobb och säger att de kanske kan bota din vampirism om du godkänner.''')],
                [sg.Button('acceptera')],
                [sg.Button('neka')],
                ])

                event, value = window.read()

                os.system('cls')
                if agent == "0":
                    start()
                while event == "acceptera":
                    if ending.count("Killer") == 0:
                        ending = ending + ["Killer"]

                    window.close()
                    window = sg.Window('kloak', layout=[
                    [sg.Text(''' "mycket bra val" ''')],
                    [sg.Text(f'''Ending: Killer
                    {len(ending)}/10 endings hittade''', font='arial 20')],
                    [sg.Button('börja om?')],
                    ])

                    event, value = window.read()

                    if event == "börja om?":
                        window.close()
                        start()

                while event == "neka":
                    if death.count("avrättad") == 0:
                        death = death + ["avrättad"]
                    window.close()
                    window = sg.Window('kloak', layout=[
                    [sg.Text('''"dåligt val"''')],
                    [sg.Text('''Boss fight: agent K''', font='timesnewroman 33')],
                    [sg.Button('')],
                    [sg.Text('''PANG! *det isar i bröstet* innan du hinner reagera har agenten skjutit dig...
                    "mycket dåligt val"''')],
                    [sg.Text(f'''death: avrättad
                    {len(death)}/7 deaths hittade''', font='arial 20')],
                    [sg.Button('börja om?')],
                    ])

                    event, value = window.read()

                    if event == "börja om?":
                        window.close()
                        start()     

            while event == "vänta":
                global gurg_the_groom
                window.close()
                window = sg.Window('kloak', layout=[
                [sg.Text('''gurg erbjuder dig en (självlysande) svamp som sin gåva til dig, vill du bli ihop med gurg?''')],
                [sg.Button('acceptera')],
                [sg.Button('neka')],
                ])

                event, value = window.read()

                os.system('cls')
                if gurg_the_groom == "0":
                    start()
                while event == "acceptera":
                    if droger.count("gas") > 0:
                        global sim
                        window.close()
                        window = sg.Window('kloak', layout=[
                        [sg.Text('''du har tagit alla tre droger (gas, piller, svamp) och har därför blivit upplyst,
                        du inser att du lever i en simulation... och att det finns andra serverar.''')],
                        [sg.Button('utforska')],
                        [sg.Button('återvänd')],
                        ])

                        event, value = window.read()

                        os.system('cls')
                        if sim == "0":
                            start()
                        while event == "utforska":
                            if ending.count("destroyer of worlds") == 0:
                                ending = ending + ["destroyer of worlds"]

                            window.close()
                            window = sg.Window('kloak', layout=[
                            [sg.Text('''Det tar en stund att åka genom sladdarna,
                            när du väl anländer har den förra servern slocknat.''')],
                            [sg.Text(f'''Ending: destroyer of worlds
                            {len(ending)}/10 endings hittade''', font='arial 20')],
                            [sg.Button('börja om?')],
                            ])

                            event, value = window.read()

                            if event == "börja om?":
                                window.close()
                                start()

                        if sim=="2":
                            print("du återvänder till jorden")
                            droger = []
                    if ending.count("gurg jn") == 0:
                        ending = ending + ["gurg jn"]

                    window.close()
                    window = sg.Window('kloak', layout=[
                    [sg.Text('''Du och gurg lever lyckliga i alla era dagar.''')],
                    [sg.Text(f'''Ending: Ordinary day 2?.. gurg jn the swamp monster vampire?
                    {len(ending)}/10 endings hittade''', font='arial 20')],
                    [sg.Button('börja om?')],
                    ])

                    event, value = window.read()
                    
                    if event == "börja om?":
                        window.close()
                        start()  

                while event == "neka":
                    global nekad
                    window.close()
                    window = sg.Window('kloak', layout=[
                    [sg.Text('''gurg ser förvirrad ut''')],
                    [sg.Button('vänta')],
                    [sg.Button('skjut')],
                    ])

                    event, value = window.read()

                    os.system('cls')
                    if nekad == "0":
                        start()
                    while event == "vänta":
                        if death.count("uppäten av gurg") == 0:
                            death = death + ["uppäten av gurg"]
                        window.close()
                        window = sg.Window('kloak', layout=[
                        [sg.Text('''när han förstår vad du menar blir han förargad
                        Motstånd är meningslöst, Gurg äter up dig,''')],
                        [sg.Text(f'''Death: uppäten av gurg
                        {len(death)}/7 Deaths hittade''', font='arial 20')],
                        [sg.Button('börja om?')],
                        ])

                        event, value = window.read()

                        if event == "börja om?":
                            start()
                    while event == "skjut":
                        window.close()
                        window = sg.Window('kloak', layout=[
                        [sg.Text('''du plockar fram pistolen, *ditt hjärta slår* du siktar, *ditt hjärta slår* och du skjuter...
                        PANG! *det piiiper i dina öron* omgivningen byter färg och varelsen faller ihop på golvet.
                        Bakom dig för du att en person klappar händerna "imponerande",
                        när du vänder dig om ser du en person i kostym,
                        de erbjuder dig ett jobb och säger att de kanske kan bota din vampirism om du godkänner.''')],
                        [sg.Button('acceptera')],
                        [sg.Button('neka')],
                        ])

                        event, value = window.read()

                        os.system('cls')

                        while event == "acceptera":
                            if ending.count("Killer") == 0:
                                ending = ending + ["Killer"]

                            window.close()
                            window = sg.Window('kloak', layout=[
                            [sg.Text(''' "mycket bra val" ''')],
                            [sg.Text(f'''Ending: Killer
                            {len(ending)}/10 endings hittade''', font='arial 20')],
                            [sg.Button('börja om?')],
                            ])

                            event, value = window.read()

                            if event == "börja om?":
                                window.close()
                                start()

                        while event == "neka":
                            if death.count("avrättad") == 0:
                                death = death + ["avrättad"]
                            window.close()
                            window = sg.Window('kloak', layout=[
                            [sg.Text('''"dåligt val"''')],
                            [sg.Text('''Boss fight: agent K''', font='timesnewroman 33')],
                            [sg.Button('')],
                            [sg.Text('''PANG! *det isar i bröstet* innan du hinner reagera har agenten skjutit dig...
                            "mycket dåligt val"''')],
                            [sg.Text(f'''death: avrättad
                            {len(death)}/7 deaths hittade''', font='arial 20')],
                            [sg.Button('börja om?')],
                            ])

                            event, value = window.read()

                            if event == "börja om?":
                                window.close()
                                start()     


                        


    else:
        window.close()
        window = sg.Window('kloak', layout=[
        [sg.Text('''BOSS FIGHT: gurg the ...guy?''', font='timesnewroman 33')],
        [sg.Button('fly')],
        [sg.Button('blockera')],
        [sg.Button('ducka')],
        [sg.Button('spaghetti')],
        [sg.Button('pistol')],
        [sg.Button('vampyr kraft')],
        ])

        event, value = window.read()

        os.system('cls')
        if gurg == "0":
            start()
        while event != "spaghetti":
            if death.count("uppäten av gurg") == 0:
                death = death + ["uppäten av gurg"]
            window.close()
            window = sg.Window('kloak', layout=[
            [sg.Text('''Motstånd är meningslöst,
            Gurg äter upp dig, ''')],
            [sg.Text(f'''Death: uppäten av gurg
            {len(death)}/7 Deaths hittade''', font='arial 20')],
            [sg.Button('börja om?')],
            ])

            event, value = window.read()

            if val == "börja om?":
                window.close()
                start()

#dra igång allt
tutorial()