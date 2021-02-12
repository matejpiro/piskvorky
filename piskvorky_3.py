# !!! udělat, aby šlo zadávat jen čísla od 1 do 9
# !!! umět hlásit remízu
# !!! fce "vyhrálo kolečko" a "vyhrál křížek" určitě jdou spojit..... nějak:P

values = [1,2,3,4,5,6,7,8,9]                # hodnoty na která se vkládají znaky
USER_INPUT_CHECK = [1,2,3,4,5,6,7,8,9]      # list kvůli kontrole vkládání správných hodnot
user_input_crosses = []                     # list ukládající hodnoty kde je křížek
user_input_circles = []                     # list ukládající hodnoty kde je kolečko
WINNING_COMBINATIONS= [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7,]]

def print_grid():                           # herní pole
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# JE PODMNOŽINOU? S timhle pracuje fce vyhoducující výhru
def subset_test(testovana_podmnozina,mnozina):
    for number in testovana_podmnozina:
        if number not in mnozina:               # tady je "not in" protože potřebuju aby z té podmnožiny byly všechny čísla v té množnině
            return False                        # tedy, pokud jen 1 číslo z podmnožiny není v množině, vrací se False
    return True

# VYHRÁL KŘÍŽEK? tomuhle sem na 5 minut rozuměl až potom, co sem do toho hodinu vejral
def cross_check_win(all_winning_combinations,list_of_crosses):
    vyhral_krizek = False
    for win_possibility in all_winning_combinations:
        if subset_test(win_possibility,list_of_crosses):
            vyhral_krizek = True
    return vyhral_krizek

# VYHRÁLO KOLEČKO?
def circle_check_win(all_winning_combinations,list_of_circles):
    vyhralo_kolecko = False
    for win_possibility in all_winning_combinations:
        if subset_test(win_possibility,list_of_circles):
            vyhralo_kolecko = True
    return vyhralo_kolecko

# OD TEĎ SE NĚCO DĚJE
print_grid()

state = ""                                                               # STATE řeší aby po špatném vložením kolečka/křížku skočila smyčka opět na vložení kolečka/křížku
while True:                                                                 # !!! PROČ je tady while true???
    if state != "kolecko":
        user_input_cross = int(input("Umísti křížek na pole číslo: "))          # vlož křížek na pole číslo:
        if user_input_cross in USER_INPUT_CHECK:                                # membership testing: je to, co zadal uživatel platné? (je to v listu "USER INPUT CHECK"?)
            i = user_input_cross - 1                                            # odečti jedničku, protože indexování jede od nuly
            if user_input_cross not in user_input_circles:                      # přidej křížek na pole pouze pokud na něm ještě není kolečko.
                state = "kolecko"
                values.insert(i, "X")                                           # vlož křížek na pole "i"
                del values[i + 1]                                               # smaž hodnutu na indexu i + 1 (páč se celej list o 1 posune), aby se list nepřeindexoval
                user_input_crosses.append(user_input_cross)                     # ulož do seznamu pole, kde teď přibyl křížek
                print_grid()                                                    # vytiskni aktuální stav hry
                cross_variable = cross_check_win(WINNING_COMBINATIONS, user_input_crosses)  # výstup fce cross_check_win
                print("křížky na pozicích: ", user_input_crosses)               # !!! tohle z finálního kodu zmizí
                if cross_variable == True:                                       # zkontroluj, zda křížek nevyhrál
                    print("KŘÍŽEK VYHRÁL - KONEC HRY")
                    break                                                       # pokud křížek vyhrál, přeruš cyklus
            else:                                                               # pokud na poli už je kolečko...
                state = "krizek"
                print("Nelze umístit. Na tomto poli už je kolečko.")
        else:                                                                   # pokud zadám neplatnou hodnotu pole
            print("Neplatná hodnota.")
            continue

    if state != "krizek":
        user_input_circle = int(input("Umísti kolečko na pole číslo: "))
        if user_input_circle in USER_INPUT_CHECK:
            j = user_input_circle -1
            if user_input_circle not in user_input_crosses:
                state = "krizek"
                values.insert(j,"O")
                del values[j+1]
                user_input_circles.append(user_input_circle)
                print_grid()
                circle_variable = circle_check_win(WINNING_COMBINATIONS,user_input_circles)
                print("kolečka na pozicích: ", user_input_circles)                # !!! tohle z finálního kodu zmizí
                if circle_variable == True:
                    print("KOLEČKO VYHRÁLO - KONEC HRY")
                    break
            else:
                print("Nelze umístit. Na tomto poli už je křížek.")
                state = "kolecko"
        else:
            print("Neplatná hodnota.")
            continue