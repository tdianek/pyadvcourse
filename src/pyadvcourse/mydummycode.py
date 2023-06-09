def fibonnacci_iterativ(n):
    """ Berechnet das n-te Folgenglied
    der Fibonacci-Folge iterativ. """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = 0 # vorletztes Folgenglied
        j = 1 # letztes Folgenglied
        for k in range(2, n+1):
            fb = i + j # neues Folgenglied
            i = j
            j = fb
        return fb            
    
def main():
    print("Fibonnacci-Folge")
    eingabe = int(input("Bitte Zahl eingeben:"))
    ausgabe = fibonnacci_iterativ(eingabe)
    print("Das", eingabe, "-te Folgenglied der Fibonnacci-Folge ist", ausgabe)

if __name__ == "__main__": 
    main()