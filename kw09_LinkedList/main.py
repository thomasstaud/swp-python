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

    # todo: test methods


if __name__ == "__main__":
    main()
