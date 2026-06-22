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
