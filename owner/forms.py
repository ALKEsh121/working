from django import forms
from django.forms import ModelForm
from tezcoapp.models import *


#service
class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


#projects
class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'


class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'



# gallery
class AddGalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


class UpdateGalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

# Blog
class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class AddTestForm(forms.ModelForm):
    class Meta:
        model = Testimo
        fields = '__all__'

class UpdateTestForm(forms.ModelForm):
    class Meta:
        model= Testimo
        fields = '__all__'