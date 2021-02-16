import re

def remove_spaces(full_name: str):
    output = full_name.replace(' ', '')
    print(f"""{remove_spaces.__name__}() ==> {output}""")
    return output


def remove_special_chars(full_name: str):
    output = re.sub("[^A-Za-z0-9]", "", full_name)
    print(f"""{remove_special_chars.__name__}() ==> {output}""")
    return output


def lowercase(full_name: str):
    output = full_name.lower()
    print(f"""{lowercase.__name__}() ==> {output}""")
    return output
