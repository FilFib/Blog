from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.date} | {self.title}'