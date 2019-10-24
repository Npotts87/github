from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def validate_reg(self, postData):
        print(self)
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match'
        print(errors)
        return errors
    def validate_login(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"

        user = User.objects.filter(email = postData['email'])
        # IF EMAIL DOESNT EXIST USER = []
        # IF EMAIL DOES EXIST USER = [{USER OBJECT}]
        # user = [{USER OBJECT}]
        # user[0] = {USER OBJECT}
        if len(user) == 0:
            errors['not_found'] = "Email not found"
        else:
            logged_user = user[0]
            if bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                pass
            else:
                errors['wrong_pw'] = "Wrong Password"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return f"User: {self.first_name} {self.last_name} {self.email} {self.password} {self.confirm_pw} {self.id}"

class ItemManager(models.Manager):
    def validate_item(self, postData):
        print(self)
        errors = {}
        if len(postData['title']) < 3:
            errors["title"] = "Item Name should be at least 3 characters"
        if len(postData['price']) < 1:
            errors["price"] = "A PRICE must be provided"
        if len(postData['description']) < 8:
            errors["description"] = "A DESCRIPTION must be provided"
        return errors

class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()


# class JobManager(models.Manager):
#     def validate_job(self, postData):
#         print(self)
#         errors = {}
#         if len(postData['title']) < 3:
#             errors["title"] = "Job Name should be at least 3 characters"
#         if len(postData['location']) < 1:
#             errors["location"] = "A location must be provided"
#         return errors

# class Job(models.Model):
#     title = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     jobs = models.ManyToManyField(User, related_name="users")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = JobManager()


#     def __repr__(self):
#         return f"Job: {self.title} {self.location} {self.description} {self.id} {self.created_at}"