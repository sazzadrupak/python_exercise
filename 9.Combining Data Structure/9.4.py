def read_file(file_name):
    contacts = {}
    try:
        f = open(file_name, "r")
        i = 1
        for line in f:
            if i != 1:
                split_row = line.split(";")
                key = split_row[0]
                contacts[key] = {
                    'name': split_row[1],
                    'phone': split_row[2],
                    'email': split_row[3],
                    'skype': split_row[4],
                }

            else:
                pass
            i += 1
        return contacts
    except IOError:
        print("Error: file %s cannot be read." % file_name)
