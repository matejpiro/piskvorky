# !!! udělat, aby šlo zadávat jen čísla od 1 do 9
# !!! umět hlásit remízu

values = [1,2,3,4,5,6,7,8,9]                # hodnoty na která se vkládají znaky
USER_INPUT_CHECK = [1,2,3,4,5,6,7,8,9]      # list kvůli kontrole vkládání správných hodnot
user_input_crosses = []
user_input_circles = []

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

def win_checker():
    if values[0] == "X" and values[1] == "X" and values[2] == "X":
        return "krizek vyhral"
    elif values[3] == "X" and values[4] == "X" and values[5] == "X":
        return "krizek vyhral"
    elif values[6] == "X" and values[7] == "X" and values[8] == "X":
        return "krizek vyhral"
    elif values[0] == "X" and values[3] == "X" and values[6] == "X":
        return "krizek vyhral"
    elif values[1] == "X" and values[4] == "X" and values[7] == "X":
        return "krizek vyhral"
    elif values[2] == "X" and values[5] == "X" and values[8] == "X":
        return "krizek vyhral"
    elif values[0] == "X" and values[4] == "X" and values[8] == "X":
        return "krizek vyhral"
    elif values[2] == "X" and values[4] == "X" and values[6] == "X":
        return "krizek vyhral"                                                      # !!! FANDA radí vyhnout se té duplicitě - kontroluju stejnou věc pro "O" i "X": nějak takle: for player in ["X","O"]

    elif values[0] == "O" and values[1] == "O" and values[2] == "O":
        return "kolecko vyhralo"
    elif values[3] == "O" and values[4] == "O" and values[5] == "O":
        return "kolecko vyhralo"
    elif values[6] == "O" and values[7] == "O" and values[8] == "O":
        return "kolecko vyhralo"
    elif values[0] == "O" and values[3] == "O" and values[6] == "O":
        return "kolecko vyhralo"
    elif values[1] == "O" and values[4] == "O" and values[7] == "O":
        return "kolecko vyhralo"
    elif values[2] == "O" and values[5] == "O" and values[8] == "O":
        return "kolecko vyhralo"
    elif values[0] == "O" and values[4] == "O" and values[8] == "O":
        return "kolecko vyhralo"
    elif values[2] == "O" and values[4] == "O" and values[6] == "O":
        return "kolecko vyhralo"

    else:
        return "zatim nikdo nevyhral"

print_grid()

while True:                                                                 # !!! PROČ je tady while true???
    user_input_cross = int(input("Umísti křížek na pole číslo: "))          # vlož křížek na pole číslo:
    if user_input_cross in USER_INPUT_CHECK:                                # membership testing: je to, co zadal uživatel platné? (je to v listu "USER INPUT CHECK"?)
        i = user_input_cross - 1                                            # odečti jedničku, protože indexování jede od nuly
        if user_input_cross not in user_input_circles:                      # přidej křížek na pole pouze pokud na něm ještě není kolečko.
            values.insert(i, "X")                                               # vlož křížek na pole "i"
            del values[i + 1]                                               # smaž hodnutu na indexu i + 1 (páč se celej list o 1 posune), aby se list nepřeindexoval
            user_input_crosses.append(user_input_cross)                     # ulož do seznamu pole, kde teď přibyl křížek
            print_grid()                                                    # vytiskni aktuální stav hry
            if win_checker() == "krizek vyhral":                            # zkontroluj, zda křížek nevyhrál
                print("KŘÍŽEK VYHRÁL - KONEC HRY")
                break                                                           # pokud křížek vyhrál, přeruš cyklus
        else:                                                               # pokud na poli už je kolečko...
            print("Nelze umístit. Na tomto poli už je kolečko.")
    else:                                                                   # pokud zadám neplatnou hodnotu pole
        print("Neplatná hodnota.")
        continue

    user_input_circle = int(input("Umísti kolečko na pole číslo: "))
    if user_input_circle in USER_INPUT_CHECK:
        j = user_input_circle -1
        if user_input_circle not in user_input_crosses:
            values.insert(j,"O")
            del values[j+1]
            user_input_circles.append(user_input_circle)
            print_grid()
            if win_checker() == "kolecko vyhralo":                         # zkontroluj, zda kolečko nevyhrálo
                print("KOLEČKO VYHRÁLO - KONEC HRY")
                break
        else:
            print("Nelze umístit. Na tomto poli už je křížek.")
    else:
        print("Neplatná hodnota.")
        continue                    # !!! TADY bych se potřeboval vrátit na vkládání kolečka a ne na začátek smyčky!
