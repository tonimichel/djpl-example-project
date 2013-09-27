from django.db import models


class NewsEntry(models.Model):
    headline = models.CharField(max_length=255, verbose_name='Headline')
    teaser = models.TextField(verbose_name='Teaser')
    text = models.TextField(verbose_name='Text')
    date = models.DateField()
    published = models.BooleanField()
    
    
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        
    def __unicode__(self):
        return self.headline
