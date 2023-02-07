import requests

SHEETY_USERS_API = "https://api.sheety.co/be64346ee3d1115d4ff84148f53ae7c0/copyOfFlightDeals/users"



class User:
    #This class is responsible for talking to the Google Sheet.
    
    
    def __init__(self):
        
        print("Welcome to the Flight Club.")
        print("We find the best flight deals and email you.")

        self.first_name = input("What is your first name? ")
        self.last_name = input("What is your last name? ")
        self.email = input("What is your email? ")
        self.email_confirmation = input("Type your email again. ")

        while self.email != self.email_confirmation:                
                print("Emails do not match. Please try again.")    
                self.email = input("What is your email? ")    
                self.email_confirmation = input("Type your email again. ")

        self.user_data = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        
        response = requests.post(url=SHEETY_USERS_API, json=self.user_data)
        print(response.text)
        print("You have been added to the Flight Club. Happy travels!")
        
    
    def get_users(self):
        response = requests.get(url=SHEETY_USERS_API)
        data = response.json()
        print(data)
        return data["users"]
    
    def get_user(self, email):

        users = self.get_users()
        for user in users:
            if user["email"] == email:
                return user
        return "User not found."
    
    def update_user(self, email, new_first_name, new_last_name, new_email):
        user = self.get_user(email)
        if user != "User not found.":
            user["firstName"] = new_first_name
            user["lastName"] = new_last_name
            user["email"] = new_email
            response = requests.put(url=f"{SHEETY_USERS_API}/{user['id']}", json=user)
            print(response.text)
            print("User updated.")
        else:
            print("User not found.")
    
    

    
user = User()

        
        
                
   
