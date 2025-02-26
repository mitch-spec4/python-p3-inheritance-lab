from user import User

class Student(User):
    
    # Setting up the student's first and last name, and an empty list for knowledge
    def __init__(self, first_name, last_name):
        # Using the parent class to set the name
        super().__init__(first_name, last_name)
        
        # Creating an empty list to store what the student learns
        self.knowledge = []

    # Method for the student to learn something new
    def learn(self, knowledge_string):
        self.knowledge.append(knowledge_string)
