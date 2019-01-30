def reverse_name(name):
    if ',' in name:
        comma_index = name.index(',')
        first_name = name[:comma_index].strip()
        last_name = name[comma_index + 1:].strip()
        if len(first_name) > 0 and len(last_name) > 0:
            correct_name = last_name + " " + first_name
            return correct_name
        elif len(first_name) > 0 and len(last_name) == 0:
            return first_name
        elif len(first_name) == 0 and len(last_name) > 0:
            return last_name
        else:
            return ''

    else:
        return name.strip()

