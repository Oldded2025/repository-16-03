from django.db import models

class Currency(models.Model):
    char_code = CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateFild(auto_now=True)

    def__str__(self):
        return f"{self.char_code} ({self.name}):{self.rate}"
