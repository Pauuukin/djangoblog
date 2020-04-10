from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        """возвращает ссылку на конкретный экземпляр класса(url reverse)"""
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})





#

# from blog.models import Post
# p=Post(title= 'New post', slug = 'new_slug', body = 'bodybody')
# p.save()
#
# p1 = Post.objects.create(title='new post 2', slug='new_slug2', body='body2body2')
# Post.objects.all()
#
# Вернем один объект (get чувствителен к регистру):
# post = Post.objects.get(slug = 'new_slug')
#
# регистронезависимый:
# post = Post.objects.get(slug__iexact='New_sluG')
#
# вернем QwerySet c содержанием 'new':
# post = Post.objects.filter(slug__contains='new')
#
# получаем все значения модели:
# Post.objects.values()
#
# меняем значение поля:
# post = Post.objects.get(slug='new_slug')
# post.slug = 'new_post'
#
# создаем зависимость Many_to_many:
# django_t = Tag.objects.create(title = 'Django', slug = 'django')
# post.tags.add(django_t)
# post.tags.all()

#