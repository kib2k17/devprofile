from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','description',
                  'demo_link','source_link','tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})

        self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        self.fields['featured_image'].widget.attrs.update({'class':'input','placeholder':'Add Image'})
        self.fields['description'].widget.attrs.update({'class':'input','placeholder':'Add Description'})
        self.fields['demo_link'].widget.attrs.update({'class':'input','placeholder':'Add Demo Link'})
        self.fields['source_link'].widget.attrs.update({'class':'input','placeholder':'Add Source Link'})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})


        self.fields['body'].widget.attrs.update({'class':'input','placeholder':'Add a comment with your vote'})
        self.fields['value'].widget.attrs.update({'class':'input','placeholder':'Add Image'})