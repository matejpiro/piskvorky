USER_INPUT_CHECK = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]           # list kvůli kontrole vkládání správných hodnot
WINNING_COMBINATIONS= [[1,2,3],[2,3,4],[3,4,5],[6,7,8],[7,8,9],[8,9,10],[11,12,13],[12,13,14],[13,14,15],[16,17,18],[17,18,19],[18,19,20],[21,22,23],[22,23,24],[23,24,25],      # řádky
                       [1,6,11],[6,11,16],[11,16,21],[2,7,12],[7,12,17],[12,17,22],[3,8,13],[8,13,18],[13,18,23],[4,9,14],[9,14,19],[14,19,24],[5,10,15],[10,15,20],[15,20,25],  # sloupce
                       [11,17,23],[6,12,18],[12,18,24],[1,7,13],[7,13,19],[13,19,25],[2,8,14],[8,14,20],[3,9,15],                                                                # úhlopříčky I
                       [11,7,3],[16,12,8],[12,8,4],[21,17,13],[17,13,9],[13,9,5],[22,18,14],[18,14,10],[23,19,15]]                                                               # úhlopříčky II
values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]                # hodnoty na která se vkládají znaky
user_input_crosses = []                         # list ukládající hodnoty kde je křížek
user_input_circles = []                         # list ukládající hodnoty kde je kolečko

def print_grid():                           # herní pole
    print("\n")
    print("\t     |     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}".format(values[0], values[1], values[2], values[3], values[4]))
    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}  |  {}".format(values[5], values[6], values[7], values[8], values[9]))
    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")
    print("\t  {} |  {} |  {} |  {} |  {}".format(values[10], values[11], values[12], values[13], values[14]))
    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")
    print("\t  {} |  {} |  {} |  {} |  {}".format(values[15], values[16], values[17], values[18], values[19]))
    print('\t_____|_____|_____|_____|_____')

    print("\t     |     |     |     |")
    print("\t  {} |  {} |  {} |  {} |  {}".format(values[20], values[21], values[22], values[23], values[24]))
    print('\t     |     |     |     |     ')

    print("\n")

# JE PODMNOŽINOU? S timhle dál pracuje fce vyhoducující výhru
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

# TĚLO KÓDU
def main():
    print_grid()

    state = ""                                                               # STATE řeší aby po špatném vložením kolečka/křížku skočila smyčka opět na vložení kolečka/křížku
    while True:                                                                 # !!! PROČ je tady while true???
        if state != "kolecko":
            user_input_cross = int(input("Umísti křížek na pole číslo: "))          # vlož křížek na pole číslo:
            if user_input_cross in USER_INPUT_CHECK:                                # membership testing: je to, co zadal uživatel platné? (je to v listu "USER INPUT CHECK"?)
                i = user_input_cross - 1                                            # odečti jedničku, protože indexování jede od nuly
                if user_input_cross not in user_input_circles:                      # přidej křížek na pole pouze pokud na něm ještě není kolečko.
                    state = "kolecko"
                    if user_input_cross > 9:                                        # rozcestník aby se nekurvilo zobrazování mřížky (vložit dva znaky nebo jeden podle délky čísla)
                        values.insert(i, "X ")
                    else:
                        values.insert(i, "X")                                       # vlož křížek na pole "i"
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
                    if user_input_circle > 9:
                        values.insert(j, "O ")
                    else:
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

if __name__ == "__main__":
    main()