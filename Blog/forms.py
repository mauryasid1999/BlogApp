from Blog import models
from django import forms
    

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=models.BlogPost
        fields={'title','slug','content','image'}
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }
