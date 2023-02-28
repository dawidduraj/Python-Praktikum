# Zusammenarbeit mit folgenden Teilnehmern:
def shortName(name):
    namen = name.split(" ")
    if len(namen) == 1:
        return name

    nachname = namen.pop()

    for n in namen:
        namen[namen.index(n)]=n[0]
    
    shortedName = ".".join(namen) + ". "

    return (shortedName + nachname).strip()
