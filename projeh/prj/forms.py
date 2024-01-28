from django import forms
from .models import comment

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea,required=False)
    
class CommentForm(forms.ModelForm):
    class Meta:
       model=comment
       fields=('name','email','body') 