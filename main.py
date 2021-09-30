def get_largest_prime_below(n):
    for i in range (n,1 ,-1):
        sem=1
        if i==1 or i%2==0 and i!=2:
            sem=0
        for j in range (3,i//2):
             if i % j == 0 :
                  sem=0
        if sem==1 :
            return i

def main ():
    while True :
        print("1.Ultimul număr prim, mai mic decât un număr dat.")
        print("x.Inchide program")
        optiune=input("Alegeti o optiune: ")
        if optiune == 'x' :
            break
        elif optiune == '1':
            numar = int(input("Alegeti un numar: "))
            maxprim = get_largest_prime_below(numar)
            print (f'ultimul numar prim mai mic decat {numar} este: {maxprim}')
        else:
            print("Optiune invalida")
main()