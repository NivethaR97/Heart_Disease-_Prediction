from django import forms
from .models import *


class heartForm(forms.ModelForm):
    class Meta():
        model=heartModel
        fields=['age','sex','cp','chol','thalach','exang','oldpeak','ca']

        labels = {
            'age': 'Patient Age',
            'sex': 'Gender',
            'cp': 'Chest Pain Type',
            'chol': 'Cholesterol Level (mg/dl)',
            'thalach': 'Maximum Heart Rate Achieved',
            'exang': 'Exercise Induced Angina',
            'oldpeak': 'ST Depression',
            'ca': 'Number of Major Vessels',
        }

        help_texts = {
            'sex': '1=Male, 0=Female',
            'cp': '0=Typical, 1=Atypical, 2=Non-anginal, 3=Asymptomatic',
            'exang': '1=Yes, 0=No',
            'ca': '0=None, 1=One, 2=Two, 3=Three',
            }
