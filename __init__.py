import questions as q

data = {
    "Nombre": "", 
    "Fecha de nacimiento": "",
    "Direccion": "",
    "Metas personales": "",
    "Objetivo principal": ""
}

def validate_input(question_text, validator):
    while True:
        print(question_text)
        user_input = input()
        if validator(user_input):
            return user_input
        else:
            print("Caracter invalido. Intente de nuevo.")

def enter_data(key, answer):
    data[key] = answer

if __name__ == "__main__":
    question = q.questions()
    
    for key in data.keys():
        if key == "Fecha de nacimiento":
            user_input = validate_input(question.pregunta(), question.validate_date)
        else:
            user_input = validate_input(question.pregunta(), question.validate_text)
        
        enter_data(key, user_input)
        print()

    for key, value in data.items():
        print("%s: %s" % (key, value))

