from django.db import models
from django.utils.text import slugify

# Create your models here.

class AiplugPost(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    img = models.ImageField()
    content = models.TextField()
    url = models.URLField()
    slug = models.SlugField(unique=True, null=False, blank=False)
    favourite = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tittle)
        super(AiplugPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/AiplugPost/{self.slug}"

    def __str__(self):
        return f'Tittle {self.tittle}'