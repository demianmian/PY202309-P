# shopping_list_manager.py
def save_shopping_list(shopping_list, filename="shopping_list.txt"):
    with open(filename, "w") as file:
        for item in shopping_list:
            file.write(f"{item}\n")
    return filename
