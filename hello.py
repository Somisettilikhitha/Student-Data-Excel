import openpyxl

def main():
    data = []
    max_entries = 3

    for entry_count in range(max_entries):
        roll_number = input("Enter Roll Number (or 'exit' to stop): ")
        if roll_number.lower() == 'exit':
            break
        name = input("Enter Name: ")
        data.append((roll_number, name))

    file_name = 'student_data.xlsx'
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["Roll Number", "Name"])

    for roll_number, name in data:
        sheet.append([roll_number, name])

    wb.save(file_name)
    print("Data successfully saved to", file_name)

if __name__ == "__main__":
    main()
