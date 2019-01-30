def create_an_acronym(name):
    acronym_value = ""
    if len(name) > 0:
        splited_name_list = name.split(" ")
        for item in splited_name_list:
            acronym_value += item[0].upper()
    return acronym_value

