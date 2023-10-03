from django.forms import ModelForm
from django import forms
from .models import Project, Userm

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['owner','title','feature_image','description','demo_link','source_link','tags']
        widgets={
                    'tags':forms.CheckboxSelectMultiple(),
                }
    def __init__(self,*args, **kwargs):
        super(ProjectForm, self). __init__ (*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        """
        Single field css
        self.fields['title'].widget.attrs.update({'class':'input'})
        self.fields['description'].widget.attrs.update({'class':'input'})"""

class UserForm(forms.ModelForm):
    class Meta:
        model=Userm
        fields=['name','email']
    
