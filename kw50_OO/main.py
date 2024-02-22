from model import Firma, Abteilung, Mitarbeiter, Abteilungsleiter


def daten_erstellen():
    mitarbeiter_fertigung = [
        Mitarbeiter("Thomas", "Staud", False),
        Mitarbeiter("Hans", "Zwiebel", False),
        Mitarbeiter("Frauke", "Zwiebel", True),
        Mitarbeiter("Hanne", "Wenger", True)
    ]
    leiter_fertigung = Abteilungsleiter("Kasimir", "Brot", False)
    fertigung = Abteilung("Fertigung", mitarbeiter_fertigung, leiter_fertigung)

    mitarbeiter_verkauf = [
        Mitarbeiter("Walter", "Hintermueller", False)
    ]
    leiter_verkauf = Abteilungsleiter("Angela", "Hinterhalt", True)
    verkauf = Abteilung("Verkauf", mitarbeiter_verkauf, leiter_verkauf)

    return Firma("PflugTec", [fertigung, verkauf])


def bericht(firma):
    print(f"Bericht Firma {firma.name}:")
    print(f"  Anzahl Mitarbeiter: {firma.anzahl_mitarbeiter()}")
    print(f"  Anzahl Abteilungen: {firma.anzahl_abteilungen()}")
    groesste = firma.groesste_abteilung()
    print(f"  Größte Abteilung: {groesste[0]} ({groesste[1]} M.A.)")
    quote = 100 * firma.frauenquote()
    print("  Frauenanteil: {:.2f}%".format(quote))


def main():
    firma = daten_erstellen()
    bericht(firma)


if __name__ == "__main__":
    main()
