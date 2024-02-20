
# result = []
with open('../контакты.txt', 'r') as file:
    name = 'Frank'
    labels = [
        "id", "full_name", "organization", "work_phone", "cell_phone"
    ]
    temp = file.read().splitlines()
    formatted_contact = False
    for people in temp:
        human = people.split(', ')
        if human[1] == name:
            formatted_contact = ""
            for label, value in zip(labels, human):
                formatted_contact += f"{label}: {value}\n"
    if formatted_contact:
        print(formatted_contact)

# with open('../контакты.txt', 'a') as file:
#     file.write("{'id': 1, 'full_name': 'Андрей', 'organization': 'фрилансер', 'work_phone_number': '', 'cell_phone_number': '8-909-333-33-22'}")
