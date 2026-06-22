
shikai = ["Zangetsu", "Hyorinmaru", "Senbonzakura", "Sakanade", "Kyokasuigetsu"]
"""
index = 0
for name in shikai:
    print(f"Index {index} dari shikai {name}")
    index += 1
"""
#Or use enumerate(), also can have an optional start parameter
for index, name in enumerate(shikai):
    print(f"Index {index} dari shikai {name}")

#Iterate two lists with zip()
Captains = ["Yamamoto", "Kenpachi", "Mayuri"]
Ids = [1, 11, 12]
for name, id in zip(Captains, Ids):
    print(f"Name: {name}\nId: {id}")
