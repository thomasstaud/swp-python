# methode mit anzahl zahlen als parameter
# methode in main x mal aufrufen
# anzahl pro zahl mit matplotlib ausgeben lassen

# pulls = ziehungen
def lotto(pulls):
    # generate numbers
    numbers = []
    for i in range(45):
        numbers.append(i+1)

    # pull numbers
    print(numbers)

if __name__ == "__main__":
    lotto(6)
