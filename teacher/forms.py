from dataclasses import field, fields
from django import forms

from teacher.models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        # fields = '__all__' ---------#this line means called all fildes from models. 
        fields = ['f_name','l_name',"group",'gender','age']