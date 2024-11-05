from django import forms

from Crud_Task_App.models import AddStudy


class Add_study_forms (forms.ModelForm):
    class Meta:
        model = AddStudy
        fields = ('studyName','studyDescription','SutdyPhase','SponsorName')
