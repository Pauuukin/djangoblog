from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


# class TagForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     slug = forms.CharField(max_length=50)
#
#     # изменяем словарь для объектов формы
#     title.widget.attrs.update({'class': 'form-control'})
#     slug.widget.attrs.update({'class': 'form-control'})

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        """очищаем данные: запрещаем создавать объекты с slug == create и условие UNIQUE"""
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug

    # def save(self):
    #     """сохраняем данные в БД"""
    #     new_tag = Tag.objects.create(title=self.cleaned_data['title'],
    #                                  slug=self.cleaned_data['slug'])
    #     return new_tag


