import re

class questions:

    def __init__(self):
        self.__number = 0
        self.__questions = ["Cual es su nombre?", "Cual es su fecha de nacimiento?", "Cual es su direccion?", "Cuales son sus metas personales?", "Cual es tu principal objetivo?"]

    def pregunta(self):
        question = self.__questions[self.__number]
        self.__number += 1
        return question
    
    def validate_text(self, text):
        if re.match(r"([A-Za-z])\w+", text):
            return True
        else:
            return False
        
    def validate_date(self, date):
        if re.match(r"\b(0[1-9]|[12]\d|3[01])\/(0[1-9]|1[0-2])\/\d{4}\b", date):
            return True
        else:
            return False