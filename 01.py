from cmath import e



def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                line = line.strip()
                if line:
                    try:
                        name, salary = line.split(",")
                        salaries.append(float(salary))
                    except ValueError:
                        print(f"We skip the line with error: {line}")
            
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            return total, average

    except FileNotFoundError:
        print("File not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

total, average = total_salary("/Users/vitalinka/vscode-basics/goit-pycore-hw-04/salary_file.txt")
print(f"The total amount of wages: {total}, Average salary: {average}")
