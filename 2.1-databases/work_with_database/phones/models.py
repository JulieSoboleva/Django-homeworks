from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, null=False, default='Nokia')
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    image = models.URLField(max_length=200, null=True)
    release_date = models.DateField(auto_now=False, auto_now_add=False,
                                    null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL',
                            default='Nokia')

    def __str__(self):
        return f"Phone(id={self.id}, name={self.name!r})"
