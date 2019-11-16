from django.db import models


# Create your models here.

class Config(models.Model):
    background = models.ImageField()

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Config, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Window(models.Model):
    day = models.IntegerField()
    content = models.ImageField(upload_to='window_contents')
    open = models.BooleanField(default=False)
    description = models.CharField(max_length=1000, default="Hast du das Türchen etwa zu früh geöffnet?")
