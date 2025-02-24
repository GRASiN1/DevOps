def get_Data():
    with open("name.txt", "r") as file:
        names = file.read()
        names = names.split()
        return names