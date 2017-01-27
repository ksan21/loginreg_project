from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_pw):
        em1 = False
        em2 = False
        em3 = False
        em4 = False
        em5 = False
        em6 = False
        no_problem = False
        if len(email) < 3:
            em1 = True
        elif not EMAIL_REGEX.match(email):
            em2 = True
        if len(first_name) < 3:
            em3 = True
        if len(last_name) < 3:
            em4 = True
        if len(password) < 8:
            em5 = True
        elif password != confirm_pw:
            em6 = True
        else:
            no_problem = True
        return  {'em1':em1,'em2':em2,'em3':em3,'em4':em4,'em5':em5,'em6':em6,'no_problem':no_problem}

    def login(self, email,password):
        em1 = False
        em2 = False
        no_problem = False
        if len(email) < 2:
            em1 = True
        if len(password) < 2:
            em2 = True
        else:
            no_problem = True
        return  {'em1':em1,'em2':em2, 'no_problem':no_problem}



class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    pw_hash = models.CharField(max_length=60)
    created_at = models.CharField(max_length=60)
    updated_at = models.CharField(max_length=60)
    objects = UserManager()
