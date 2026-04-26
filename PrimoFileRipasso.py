"""Selezione"""

potere = 9001

if potere > 9000:
    print("È oltre novemila!")
elif potere > 1000:
    print("Niente male.")
else:
    print("Torna ad allenarti.")

"""Truthy or Falsy"""

inventario = []

# ❌ Inutilmente verboso
if len(inventario) == 0:
    print("Zaino vuoto.")

# ✅ Pythonic
if not inventario:
    print("Zaino vuoto.")

"""Confronti concatenati"""

livello = 42

# ❌ Come si farebbe in Java
if livello >= 1 and livello <= 100:
    print("Livello valido.")

# ✅ Pythonic
if 1 <= livello <= 100:
    print("Livello valido.")