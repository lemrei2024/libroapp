from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion']
