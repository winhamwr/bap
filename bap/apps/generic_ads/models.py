from django.db import models
from django.utils.translation import ugettext_lazy as _

class LinkedImage(models.Model):
    url = models.URLField(_('url'), max_length=255, blank=True)
    image = models.ImageField(_('image'), upload_to='gblocks/', blank=True)

    def __unicode__(self):
        return "(LinkedImage) %s" % self.url
