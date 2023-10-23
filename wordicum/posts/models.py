from django.db import models


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Publication date", auto_now_add=True)

    def __str__(self):
        return self.text
