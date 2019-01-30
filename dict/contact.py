# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: contacts, program code template


def main():
    contacts = {"Tom": {"name": "Tom Techie",
                        "phone": "040 123546",
                        "email": "tom@tut.fi",
                        "skype": "tom_92_"},
                "Mike": {"name": "Mike Mechanic",
                         "phone": "050 123546",
                         "email": "mike@tut.fi",
                         "skype": "-Mike-M-"},
                "Archie": {"name": "Archie Architect",
                           "phone": "050 987654",
                           "email": "archie@tut.fi"}}

    contact = input("Enter the name of the contact: ")
    field = input("Enter the field name you're searching for: ")
    if not contacts.get(contact):
        print("No contact information for {}".format(contact))
    elif contacts[contact]['name'] and not contacts[contact].get(field):
        print("No {} for {}".format(field, contacts[contact]['name']))
    else:
        print('{}, {}: {}'.format(contacts[contact]['name'], field, contacts[contact][field]))


main()
