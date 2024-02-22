class Firma:
    def __init__(self, name, abteilungen):
        self.name = name
        self.abteilungen = abteilungen

    def anzahl_mitarbeiter(self):
        return sum([a.anzahl_mitarbeiter() for a in self.abteilungen])

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        mx = ([], 0)
        for abteilung in self.abteilungen:
            name = abteilung.get_name()
            anzahl = abteilung.anzahl_mitarbeiter()
            if anzahl > mx[1]:
                mx = ([name], anzahl)
            elif abteilung.anzahl_mitarbeiter() == mx[1]:
                mx[0].append(name)
        return mx

    def frauenquote(self):
        anzahl_frauen = sum([a.anzahl_frauen() for a in self.abteilungen])
        return anzahl_frauen / self.anzahl_mitarbeiter()


class Abteilung:
    def __init__(self, name, mitarbeiter, leiter):
        self.name = name
        self.mitarbeiter = mitarbeiter
        self.leiter = leiter

    def get_name(self):
        return self.name

    def anzahl_mitarbeiter(self):
        # + 1 fuer den Abteilungsleiter
        return len(self.mitarbeiter) + 1

    def anzahl_frauen(self):
        return sum([m.is_weiblich() for m in self.mitarbeiter]) + self.leiter.is_weiblich()


class Person:
    def __init__(self, vorname, nachname, weiblich):
        self.vorname = vorname
        self.nachname = nachname,
        self.weiblich = weiblich

    def is_weiblich(self):
        return self.weiblich


class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, weiblich):
        super().__init__(vorname, nachname, weiblich)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, vorname, nachname, weiblich):
        super().__init__(vorname, nachname, weiblich)
