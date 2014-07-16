from django import forms
from stackpro.apps.employee.models import advert, answer

class advertform(forms.ModelForm):
    class Meta:
        model = advert
        exclude = {'status','pub_date'}
    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary < 700:
            raise forms.ValidationError('NO, metete en la puja >= 700 US')

class answerform(forms.ModelForm):
    class Meta:
        model = answer
        exclude = {'answerlink'}