from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)        # auto_add_now=True current date 
                                                                # and time of create new topic
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic)        # Many-to-many
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + ("..." if len(self.text) > 50 else "")