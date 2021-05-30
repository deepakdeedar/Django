from django import forms
from django.forms.forms import Form

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your Name', max_length=100)
    review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)