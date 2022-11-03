def format_names(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name}, {last_name}"

print(format_names(input('Enter first name: '), input("Enter the last name: ")))