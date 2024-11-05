from cmath import e

def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        cat_id, name, age = line.split(",")
                        cat_info = {"id": cat_id, "name": name, "age": age}
                        cats_info.append(cat_info)
                    except ValueError:
                        print(f"Skipping line with error: {line}")
                        
        return cats_info
    
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

cats_info = get_cats_info("/Users/vitalinka/vscode-basics/goit-pycore-hw-04/cats_file.txt")
print(cats_info)
