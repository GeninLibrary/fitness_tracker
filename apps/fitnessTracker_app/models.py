from __future__ import unicode_literals

from django.db import models

from time import gmtime,strftime


class checkProfile(models.Manager):

    def buildProfile(self, post_data):
        self.create(
            name = post_data['name'],
            age = post_data['age'],
            weight = post_data['weight'],
        )

class fit_Profile (models.Model) :

    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    weight = models.DecimalField(decimal_places = 2, max_digits = 5)
    objects = checkProfile()



