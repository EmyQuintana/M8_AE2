from django import forms
from .models import Voluntario, Evento

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', 'email', 'telefono', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan Pérez'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EventoForm(forms.ModelForm):
    # ESTE ES EL CAMPO MAGICO QUE FALTA
    foto_portada = forms.ImageField(
        required=False, 
        label="Foto de Portada", 
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'aforo', 'voluntarios']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'aforo': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'voluntarios': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }