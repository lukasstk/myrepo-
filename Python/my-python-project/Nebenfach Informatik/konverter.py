def str_to_list(eingabe_str):
    eingabe_list = eingabe_str.split(",")
    ausgabe_list = []

    for elem in eingabe_list:
        type_cast = get_type(elem)
        ausgabe_list.append(type_cast(elem))

    return ausgabe_list


def list_to_str(eingabe_list):
    if not eingabe_list:
        # leere Liste
        return ""

    ausgabe_str = str(eingabe_list[0])

    for elem in eingabe_list[1:]:
        ausgabe_str = ausgabe_str + "," + str(elem)

    return ausgabe_str


def get_type(elem):

    if elem.isdigit():
        return int

    if is_float(elem):
        return float

    elif elem == "True" or elem == "False":
        return eval

    else:
        return str


def is_float(elem):
    try:
        float(elem)
        return True
    except ValueError:
        return False
