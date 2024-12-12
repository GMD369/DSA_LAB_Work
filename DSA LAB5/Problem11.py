students = ["John", "Alice", "Bob", "Mary", "Steve","Ali","GMD","ABD","Ghayoor"]

def search_Student(name):
    if name in students:
        index=students.index(name)
        print(f"{name} is found at index {index}.")
    else:
        print(f"{name} is not found in the list.")

name=input("Enter Name to search:")
search_Student(name)