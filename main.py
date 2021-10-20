def show_menu():
    print('Alegeti optiunea:')
    print('1.Citire lista de stringuri')
    print('2.Cautarea unui sir de caractere citit de la tastatura')
    print('3.Afisare a unei liste cu toate sirurile care se repeta')
    print('4.Afisare siruri care nu sunt palindrom')
    print('5.Lista obtinuta prin inlocuirea sirurilor care contin caract care apare de cele mai multe ori cu nr de aparitii')
    print('6.Exit')


def read_list():
    list_of_strings=input('Introduceti o lista de siruri de caractere: ')
    list_of_strings_final=list_of_strings.split(' ')
    strings=[]
    for string in list_of_strings_final:
        strings.append(str(string))
    return strings


def if_in_list(lst):
    ok=0
    n=input('Introduceti numarul: ')
    for i in lst:
        if i==n:ok=1
    if ok==1: print('DA')
    else: print('NU')
    return 0


def list_of_duplicates(lst):
    seen = {}
    dupes = []

    for x in lst:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    return dupes

def show_list_of_duplicates(lst):
    print(f'lista de duplicate din {lst} este:{list_of_duplicates(lst)}')


def siruri_palindrom(lst):
    result=[]
    for i in  lst:
        if(i!=i[::-1]):
            result.append(i)
    return result

def show_siruri_palindrom(lst):
    print(f'lista de numere care nu sunt palindroame din {lst} este:{siruri_palindrom(lst)}')


def inlocuire(lst):
    all_freq = {}
    for i in lst:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    res = max(all_freq, key=all_freq.get)




def main():
    lst=[]
    while True:
        show_menu()
        option=input('Alegeti optiunea: ')
        if option=='1':
            lst=read_list()
        elif option=='2':
            if_in_list(lst)
        elif option=='3':
            show_list_of_duplicates(lst)
        elif option=='4':
            show_siruri_palindrom(lst)
        elif option=='5':
            break


if __name__ == '__main__':
    main()

