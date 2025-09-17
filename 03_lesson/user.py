class User:

    def __init__ (self,first_name, last_nane):
        self.first_name = first_name
        self.last_name = last_nane

    def sayFirst_name(self):
        print("Меня зовут " , self.first_name)

    def sayLast_name(self):
        print("Моя фамилия " , self.last_name)

    def sayUserInfo(self):
        print(f"{self.first_name} {self.last_name}")
        


    
