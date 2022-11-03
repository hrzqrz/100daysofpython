def format_name(f_name, l_name):
    if f_name =="" or l_name == "":
        return "You didnot provide valid inputs"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

print(format_name(input('Enter your first name: '), input('Enter your last name: ')))
    