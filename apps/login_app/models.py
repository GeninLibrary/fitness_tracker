from __future__ import unicode_literals

from django.db import models

import bcrypt   # ENCODES PASSWORD

from time import gmtime,strftime


#Create a user with an encrypted password. 
#Retrieve user from database and test bcrypts ability
#      to decode and compare passwords


class CheckUser(models.Manager):
    
    def createUser(self, post_data):
        encrypted_password = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        print("THIS IS YOUR ENCRYPTED PASSWORD: ", encrypted_password)
        self.create(
            name = post_data["name"],
            username = post_data["username"],
            password = encrypted_password,
        )

    def retrieveUser(self, post_data):
        results = {
            'error' : [],
            'status' : True,
            'retrieved_User' : None,
        }
        user_match = self.filter(username = post_data['username'])
        if len(user_match) == 0:
            results['status'] = False
            results['errors'].append("Sorry! This username isn't in our database.") 
        else:
            results['retrieved_User'] = user_match[0]
            print("ALL GOOD UP TO BCRYPT DECOOOOOOODDDDDDEEEEEEE")
            # if not bcrypt.checkpw(post_data['password'].encode(), results['retrieved_User'].password.encode()):           
            #     results['errors'].append("That key ain't gonna get you in this door. Take another shot, Neo")
            #     results['status'] = False
            # ----- Bcrypt fails to decode and compare passwords correctly. ------
            # ----- Django version 2.1.2     Python 3.6.1 version   ------

        return results

class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    objects = CheckUser()