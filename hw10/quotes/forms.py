from django import forms
from .models import Author, Quote



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'location_born', 'bio']
        
class QuoteForm(forms.ModelForm):
    quote = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Separated by commas'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select an author")

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']

# class ContributeAuthorForm(Form):
#     fullname = CharField(max_length=200, required=True, widget=TextInput(attrs={"class": "form-control", "placeholder": "Enter authors fullname"}))
#     date_born = CharField(max_length=50, widget=TextInput(attrs={"class":"form-control", "placeholder": "Enter born date"}))
#     location_born = CharField(max_length=35, widget=TextInput(attrs={"class":"form-control", "placeholder": "Enter born location"}))
#     bio = CharField(max_length=400, widget=TextInput(attrs={"class": "form-control", "placeholder": "Enter biography"}))
#     Some_field = CharField(widget=TextInput(attrs={"class": "form-control", "placeholder": "Enter biography"}))
    
# class ContributeForm(Form):
#     quote = CharField(max_length=200, required=True, widget=TextInput(attrs={"class": "form-control", "placeholder": "Enter quote"}))
#     tags = CharField(max_length=50,required=True, widget=TextInput(attrs={"class":"form-control", "placeholder": "Enter tag"}))
#     author = CharField(max_length=35,required=True, widget=TextInput(attrs={"class":"form-control", "placeholder": "Enter author"}))