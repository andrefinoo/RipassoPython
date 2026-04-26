"""La funzione ord() (che sta per ordinal) prende in input un singolo carattere e restituisce il suo codice numerico (intero)."""

codice_a = ord('a')
print(codice_a)  # Output: 97

codice_A = ord('A')
print(codice_A)  # Output: 65

# Nota: 'a' e 'A' sono numeri diversi!

"""La funzione chr() (che sta per character) fa l’operazione inversa: prende un numero intero e restituisce il carattere corrispondente."""

lettera = chr(97)
print(lettera)   # Output: 'a'

simbolo = chr(64)
print(simbolo)   # Output: '@'

"""Poiché le stringhe sono sequenze di caratteri (e non di bit!), possiamo usare queste funzioni per trasformare interi messaggi in liste di numeri e viceversa."""

messaggio = "Ciao"
numeri = []

for carattere in messaggio:
    numeri.append(ord(carattere))

print(numeri)
# Output: [67, 105, 97, 111]
# Nota: C=67, i=105, a=97, o=111

output = ""
numeri_da_tradurre = [102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125]
for numero in numeri_da_tradurre:
    output += chr(numero)

print(output)

"""Creare bit da una stringa"""

testo ="caffè"
dati = testo.encode("utf-8")
print(dati)
print(type(dati))

"""Creare bit da una lista di numeri"""

dati = bytes([65, 66, 67])
print(dati)  # b'ABC'

"""Creare stringa da un letterale b"..."""

dati = b"ABC"
altro = b"\x41\x42\x43"
print(dati, altro)  # b'ABC' b'ABC'

"""Dai byte al testo: decode()"""

dati = b'caff\xc3\xa8'
testo = dati.decode("utf-8")
print(testo)  # caffè

"""Usi di bytes: indicizzazione, slicing e iterazione"""

dati = b"GAME"
print(dati[0])     # 71 (numero del byte)
print(dati[1:3])   # b'AM'

for b in b"OK":
    print(b)
# 79
# 75
