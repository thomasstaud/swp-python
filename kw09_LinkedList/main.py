from linked_list import LinkedList
import random


def main():
    liste = LinkedList()
    for i in (random.randint(0, 100) for _ in range(10)):
        liste.append(i)

    print(liste)
    print(f"length: {len(liste)}")

    print("printing list...")
    for element in liste:
        print(element)

    liste = LinkedList.from_list([1, 2, 3])
    print(liste)
    liste.append([4, 5, 6])
    print(liste)


if __name__ == "__main__":
    main()
