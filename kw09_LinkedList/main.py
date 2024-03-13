from linked_list import LinkedList
import random


def main():
    lst = LinkedList()
    for i in (random.randint(0, 100) for _ in range(10)):
        lst.append(i)

    print(lst)
    print(f"length: {len(lst)}")

    print("printing list...")
    for element in lst:
        print(element)

    lst = LinkedList.from_list([1, 2, 3])
    print(lst)
    lst.append([4, 5, 6])
    print(lst)


if __name__ == "__main__":
    main()
