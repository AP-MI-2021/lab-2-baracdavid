from datetime import date
def get_largest_prime_below(n):
    if n > 3:
        for i in range(n-1,1 ,-1):
            sem=1
            if i==1 or (i%2==0 and i!=2) :
                sem=0
            for j in range (3,i//2):
                 if i % j == 0 :
                      sem=0
            if sem==1 :
                return i
    elif n==3:
        return 2
    else:
        return 0
def test_get_largest_prime_below():
    assert get_largest_prime_below(3) == 2
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(6) == 5
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(7) == 5

def get_age_in_days(birthday):
    todays_date = date.today()
    zile_totale = 0
    list_luni =[ 31,28,31,30,31,30,31,31,30,31,30,31 ]
    birthday_list=birthday.split("/")
    int_list =[int(x) for x in birthday_list]
    anii_bisecti = (todays_date.year - int_list[2]) // 4
    if int_list[1] > 12 or int_list[1] < 1 :
        return 0
    elif int_list[0]> 31 or int_list[1]  < 1 :
        return 0
    elif int_list[2] < 1:
        return 0
    else :
        if todays_date.month > int_list[1]:
            i = int_list[1] + 1
            while i < todays_date.month:
                zile_totale += list_luni[i]
                i = i + 1
            if todays_date.day > int_list[0]:
                zile_totale += todays_date.day - int_list[0]
            else:
                zile_totale += list_luni[int_list[1]] - int_list[0] + todays_date.day
        else:
            j = int_list[1]
            while j < 12:
                zile_totale += list_luni[j]
                j = j + 1
            if todays_date.day > int_list[0]:
                zile_totale += todays_date.day - int_list[0]
            else:
                zile_totale += list_luni[int_list[1]] - int_list[0] + todays_date.day
            for x in range(1, todays_date.month):
                zile_totale += list_luni[x]
        zile_totale += (todays_date.year - int_list[2]) * 365
        zile_totale += anii_bisecti

        return zile_totale
def test_get_age_in_days():
    assert get_age_in_days("155/01/2001") == 0
    assert get_age_in_days("20/100 /2005") == 0
    assert get_age_in_days("-20/100 /2005") == 0
    assert get_age_in_days("21/01 /-111") == 0
    assert get_age_in_days("2/-1 /2005") == 0
def main ():
    while True :
        print("1.Gaseste ultimul număr prim, mai mic decât un număr dat.")
        print("2.Determinați vârsta unei persoanei în zile")
        print("x.Inchide program")
        optiune=input("Alegeti o optiune: ")
        if optiune == 'X' :
            break
        elif optiune == '1':
            numar = int(input("Dati un numar: "))
            if numar < 3:
                print("Introduceti o valoare valida")
            else:
                maxprim = get_largest_prime_below(numar)
                print (f'ultimul numar prim mai mic decat {numar} este: {maxprim}')
        elif optiune == '2':
            data_nasterii=input("introduceti data nasterii in formatul urmator: DD/MM/YYYY ")
            string_list=data_nasterii.split("/")
            intlist =[int(x) for x in string_list]
            if intlist[1] > 12 or intlist[1] < 1  :
                print("Numarul lunilor trebuie sa fie  in intervalul [1,12]")
                get_age_in_days(data_nasterii)
            elif intlist[0]> 31 or intlist[0] < 1 :
                print("Numarul zilelor trebuie sa fie  in intervalul [1,31]")
                get_age_in_days(data_nasterii)
            elif intlist[2] <1 :
                print("Numarul anilor nu poate fi negativ")
                get_age_in_days(data_nasterii)
            else:
                print("Varsta in zile este: ")
                print (f'{get_age_in_days(data_nasterii)} zile' )

        else:
            print("Optiune invalida")
    test_get_largest_prime_below()
    test_get_age_in_days()
main()