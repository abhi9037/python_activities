from user import User
from database import Database

my_user = User('faku@gmail.com','Favas','AT')

Database.initialise(user='postgres', password='1234', database='learning',
                                                          host='localhost')

my_user.save_to_db()

user_from_db = my_user.load_from_db_by_email('faku@gmail.com')

print(user_from_db)