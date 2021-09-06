
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name2(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name2('jimi', 'lee', 'hendrix')
print(musician)


def get_formatted_name3(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name3('jimi', 'lee', 'hendrix')
print(musician)
musician = get_formatted_name3('jimi', 'hendrix')
print(musician)
