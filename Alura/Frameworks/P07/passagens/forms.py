from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(
        label='Data da Pesquisa', disabled=True, initial=datetime.today())
    classe_viagem = forms.ChoiceField(
        label='Classe de Viagem', choices=tipos_de_classe)
    information = forms.CharField(
        label='Informações adicionais',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(
        label='E-mail',
        max_length=150
    )
