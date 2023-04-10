from django.forms import ModelForm
from .models import Course, Student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(ModelForm):
    search = True

    class Meta:
        model = Course
        fields = ['title']


class ApplicationForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'course']
        widgets = {
            'course': forms.CheckboxSelectMultiple(),
        }


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
