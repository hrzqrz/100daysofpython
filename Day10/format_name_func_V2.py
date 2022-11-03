def format_names(f_name, l_name):
    formated_first_name = f_name.title()
    formated_last_name = l_name.title()
    return f"{formated_first_name}, {formated_last_name}"

formated = format_names('ALI', 'MOhamadi')
print(formated)