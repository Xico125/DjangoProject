from django.shortcuts import render, redirect
from .forms import AvaliacaoForm

def formulario_view(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'treino/obrigado.html')
    else:
        form = AvaliacaoForm()
    return render(request, 'treino/formulario.html', {'form': form})
