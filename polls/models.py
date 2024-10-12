from django.db import models
from django.utils.text import slugify
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date_published", auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
         now = timezone.now()
         return now - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
            self.slug = slugify(f"{self.question_text[:5]}")
            super().save(*args, **kwargs)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=100, unique=True)
    votes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.choice_text)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.choice_text
    