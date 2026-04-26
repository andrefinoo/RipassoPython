"""La funzione open() e il with statement"""

f = open("dati.txt", "r", encoding="utf-8")
contenuto = f.read()
f.close()

"""Questo codice funziona, ma è fragile: 
se tra open() e close() viene sollevata un’eccezione, il file rimane aperto. 
Il modo corretto di operare è usare il with statement, che garantisce la chiusura del file in ogni caso"""

with open("dati.txt", "r", encoding="utf-8") as f:
    contenuto = f.read()
# qui il file è già chiuso, anche se è scoppiato tutto

# ❌ Dipende dalla piattaforma
with open("log.txt", "r") as f:
    ...

# ✅ Esplicito e portabile
with open("log.txt", "r", encoding="utf-8") as f:
    ...

""".read() carica l’intero contenuto in una stringa. Se il file è molto grande, potrebbe causare problemi di memoria."""

with open("regole.txt", "r", encoding="utf-8") as f:
    tutto = f.read()
    print(f"File da{len(tutto)} caratteri")

""".readline() legge una riga alla volta e avanza il cursore. Utile per file di grandi dimensioni."""

with open("log.txt", "r", encoding="utf-8") as f:
    prima_riga = f.readline()   # include il \n finale
    seconda_riga = f.readline()

"""Iterazione diretta sul file: ogni iterazione restituisce una riga (con \n finale)."""

with open("indirizzi.txt", "r", encoding="utf-8") as f:
    for riga in f:
        ip = riga.strip()   # .strip() rimuove \n e spazi
        if ip:              # salta righe vuote
            print(f"Processo:{ip}")

""".write() scrive una stringa nel file. Se il file non esiste, viene creato. Se esiste, viene sovrascritto."""

with open("risultati.txt", "w", encoding="utf-8") as f:
    f.write("Scansione completata\n")
    f.write(f"Host trovati: 42\n")

""".writelines() accetta un iterabile di stringhe e le scrive in sequenza.
Non aggiunge automaticamente \n, quindi è necessario includerli se si vogliono righe separate."""

righe = [f"{ip}\n" for ip in host_attivi]
with open("host_attivi.txt", "w", encoding="utf-8") as f:
    f.writelines(righe)

"""Gestire i path con pathlib"""

from pathlib import Path

# Costruzione di percorsi con /
base = Path("dati")
config = base / "config.json"
log_dir = base / "logs"

# Informazioni sul percorso
print(config.name)      # "config.json"
print(config.stem)      # "config"
print(config.suffix)    # ".json"
print(config.parent)    # "dati"

# Lettura e scrittura diretta (alternativa a open())
testo = Path("note.txt").read_text(encoding="utf-8")
Path("output.txt").write_text("risultato", encoding="utf-8")

# Verifica esistenza prima di aprire
if config.exists():
    with config.open("r", encoding="utf-8") as f:
        ...

"""Leggere da file: json.load()"""

import json
from pathlib import Path

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# config è ora un dict (o list, a seconda del JSON)
print(config["hostname"])

"""Leggere da stringa: json.loads()"""

testo = '{"ip": "10.0.0.1", "porta": 22}'
host = json.loads(testo)
print(host["ip"])   # "10.0.0.1"

"""Scrivere su file: json.dump()"""

risultati = {
    "scan_date": "2026-04-10",
    "target": "192.168.1.0/24",
    "hosts_up": 14
}

with open("scan_results.json", "w", encoding="utf-8") as f:
    json.dump(risultati, f, indent=2, ensure_ascii=False)

"""Serializzare a stringa: json.dumps()"""

testo_json = json.dumps(risultati, indent=2, ensure_ascii=False)
print(testo_json)

"""Se il file JSON è malformato, json.load() solleva json.JSONDecodeError — una sottoclasse di ValueError"""

import json

try:
    with open("dati.json", "r", encoding="utf-8") as f:
        dati = json.load(f)
except FileNotFoundError:
    print("File non trovato — verificare il percorso")
except json.JSONDecodeError as e:
    print(f"JSON non valido:{e.msg} alla riga{e.lineno}, colonna{e.colno}")

""".get() è un metodo dei dict che restituisce il valore associato a una chiave, o un valore di default se la chiave non esiste. Utile per evitare KeyError."""

# JSON annidato
{
    "utente": {
        "nome": "gandalf",
        "ruolo": {
            "titolo": "wizard",
            "livello": 20
        }
    }
}

utente = dati.get("utente", {})
nome = utente.get("nome", "sconosciuto")
ruolo = utente.get("ruolo", {})
titolo = ruolo.get("titolo", "nessuno")

