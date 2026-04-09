from django import forms
from .models import Topic,Entiy

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':'主题名'}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entiy
        fields = ['text']
        labels = {'text':'实体'}
        widgets = {'text':forms.Textarea(attrs={'cols':40})}
    
        


