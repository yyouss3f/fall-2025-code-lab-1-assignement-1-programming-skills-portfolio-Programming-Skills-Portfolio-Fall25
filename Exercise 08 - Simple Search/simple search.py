names = ["Jake", "Zac", "John", "Ron", "Sam", "Dave"]

search_term = input("Enter a name to search: ")

if search_term in names:
    print(search_term, "is in the list!")
else:
    print(search_term, "is not in the list.")