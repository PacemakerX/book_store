from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

# we define our data entities, blueprints for dataobjects , we are going to work with

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    author = models.CharField(max_length=100)
    is_bestselling = models.BooleanField()
    slug = models.SlugField( blank=True,db_index=True,editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-").lower()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return (
            f"Name: {self.title}\n"
            f"Rating: {self.rating}\n"
            f"Author: {self.author}\n"
            f"Is Bestselling: {'YES' if self.is_bestselling else 'NO'}\n"
            f"Slug: {self.slug}"
        )
