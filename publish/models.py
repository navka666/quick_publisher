from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	created = models.DateTimeField('Created Date', default=timezone.now)
	title = models.CharField('Title', max_length=200)
	content = models.TextField('Content')
	slug = models.SlugField('Slug')
	view_count = models.IntegerField('View Count', default=0)

	def __str__(self):
		return '"%s" by %s' %(self.title, self.author)
