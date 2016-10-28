from django import forms
from stackpro.apps.employee.models import advert, answer

class advertform(forms.ModelForm):
    class Meta:
        model = advert
        exclude = {'status','pub_date'}
        widgets = {
            'descriptionofjob': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'prove': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            # 'status': forms.CheckboxInput(attrs={'class': 'filled-in',}),
        }
    
    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary < 700:
            raise forms.ValidationError('NO, metete en la puja >= 700 US')
        return salary

class answerform(forms.ModelForm):
    class Meta:
        model = answer
        exclude = {'fk'}