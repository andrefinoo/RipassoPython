"""Da `bytes` a esadecimale: `.hex()`
Il metodo `.hex()` converte un oggetto `bytes` in una stringa esadecimale."""

dati = b"Hello"
esadecimale = dati.hex()
print(dati, type(dati))
print(esadecimale, type(esadecimale))

""" Da esadecimale a `bytes`: `bytes.fromhex()`
La funzione `bytes.fromhex()` fa l’operazione inversa: prende una stringa esadecimale e la converte in un oggetto `bytes`."""

esadecimale = "48656c6c6f" # numero pari di caratteri
dati = bytes.fromhex(esadecimale)
print(dati)  # Output: b'Hello'

esadecimale = "48 65 6c 6c 6f" # Anche con spazi funziona
dati = bytes.fromhex(esadecimale)
print(dati)  # Output: b'Hello'

"""Da bytes a base64: b64encode()"""

from base64 import b64encode

dati = b"Hello, world!"
codificato = b64encode(dati)
print(codificato, type(codificato))
# Output: b'SGVsbG8sIHdvcmxkIQ==' <class 'bytes'>

codificato_str = codificato.decode('ascii')
print(codificato_str)
# Output: 'SGVsbG8sIHdvcmxkIQ=='

"""Da base64 a bytes: b64decode()"""

from base64 import b64decode

codificato = 'SGVsbG8sIHdvcmxkIQ=='
dati = b64decode(codificato)
print(dati)  # Output: b'Hello, world!'

"""La funzione int.from_bytes() converte un oggetto bytes in un numero intero."""

dati = b'\x00\x01\x02\x03'
numero = int.from_bytes(dati, byteorder='big') #big legge byte da sinistra a destra mentre little da destra a sinistra
print(numero)  # Output: 66051 (che in esadecimale è 0x00010203)

dati = b'\x01\x02\x03\x04'

# Big endian (da sinistra a destra)
numero_big = int.from_bytes(dati, byteorder='big')
print(numero_big)  # Output: 16909060 (0x01020304)

# Little endian (da destra a sinistra)
numero_little = int.from_bytes(dati, byteorder='little')
print(numero_little)  # Output: 67305985 (0x04030201)

"""Il metodo .to_bytes() fa l’operazione inversa: converte un numero intero in un oggetto bytes."""

numero = 66051  # 0x00010203
dati = numero.to_bytes(length=4, byteorder='big')
print(dati)  # Output: b'\x00\x01\x02\x03'

"""- **`length`**: quanti byte usare per rappresentare il numero. 
Se il numero è troppo grande per entrare in `length` byte, ottieni un `OverflowError`.
- **`byteorder`**: `'big'` o `'little'`, come prima."""

numero = 255  # 0xFF

# Con 1 byte
print(numero.to_bytes(1, 'big'))  # b'\xff'

# Con 2 byte (aggiungerà padding)
print(numero.to_bytes(2, 'big'))  # b'\x00\xff'

# Con 4 byte (più padding)
print(numero.to_bytes(4, 'big'))  # b'\x00\x00\x00\xff'