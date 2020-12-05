from django.db import models
import os
from twilio.rest import Client


# Create your models here.
class score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)
    
    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'AC9e8b21c2bf457c8127265a359a50a94d'
            auth_token = 'f096900d4cb23a234674d58c9712a3d3'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                    body=f'current result is bad - {self.result} ',
                    from_='+15122136792',
                    to='+34634058231'
                )

            print(message.sid)
        return super().save(*args, **kwargs)