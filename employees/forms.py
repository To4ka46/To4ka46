from django import forms
from .models import EmployeeImage
from .models import EmployeeSkill

class SingleImageUploadForm(forms.ModelForm):
    class Meta:
        model = EmployeeImage
        fields = ['image', 'order']
        widgets = {
            'image': forms.FileInput(),
            'order': forms.NumberInput(attrs={'placeholder': 'Например, 1'}),
        }
