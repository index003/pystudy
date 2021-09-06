
def build_person(first_name, last_name):
    person = {
        'first_name': first_name,
        'last_name': last_name
    }
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=None):
    person = {
        'first_name': first_name,
        'last_name': last_name
    }
    if age:
        person['age'] = age

    return person


musician = build_person('jimi', 'hendrix', 27)
print(musician)
