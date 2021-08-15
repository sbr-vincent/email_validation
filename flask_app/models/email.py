from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# model the class after the friend table from our database
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('email_schema').query_db(query)
        # Create an empty list to append our instances of emails
        emails = []
        # Iterate over the db results and create instances of emails with cls.
        for email in results:
            emails.append( cls(email) )
        return emails
    

    @staticmethod
    def validate_user( email ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        
        if EMAIL_REGEX.match(email['email']): 
            flash(f"The email address you entered {email['email']} is a VALID email address! Thank you!")

        return is_valid