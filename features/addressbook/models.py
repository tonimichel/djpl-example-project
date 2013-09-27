from django.db import models




TYPES = (
    ('business', 'Business',),
    ('friend', 'Friend',),
)


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    salutation = models.CharField(max_length=255, null=True, blank=True, verbose_name='Salutation')
    type = models.CharField(max_length=100, choices=TYPES, null=True, blank=True, verbose_name='Rating')
    employer = models.CharField(max_length=255, null=True, blank=True, verbose_name='Employer')
    note = models.TextField(null=True, blank=True, verbose_name='Anmerkung')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    


    def __unicode__(self):
        return self.name        
    
