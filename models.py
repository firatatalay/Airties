from datetime import datetime

class Person:
    def __init__(self, id, first_name, last_name, email, phone, created_date):
        self.id=id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.created_date = datetime.strptime(created_date.split(".")[0], "%Y-%m-%d %H:%M:%S")
                            #2021-09-05 23:30:54.906879     The default date data is splitted.
    def serialize(self):
        '''Serializing the response from the API.'''
        return{
            "id" : self.id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email": self.email,
            #"phone": self.phone,
            "created_date": datetime.strftime(self.created_date, "%Y-%d-%m" ) #Date data is listed as Year/Day/Month as in the document.
            }