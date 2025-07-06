from django import forms
from .models import AvaliacaoTreino

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoTreino
        fields = '__all__'
        labels = {
            'nome': "Nome:",
            'disponibilidade': "Qual a disponibilidade/vontade de hoje para o treino de 0-10:",
            'intensidade': "Qual foi a intensidade do treino na tua opinião de 0-10:",
            'nota_geral': "Nota do treino todo de 0-10:",
            'opiniao': "Na tua opinião o que podia ser melhorado:",
        }
        widgets = {
            'opiniao': forms.Textarea(attrs={'rows': 4}),
        }
