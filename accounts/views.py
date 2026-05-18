from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistoForm
from .models import MagicLinkToken
from django.urls import reverse

# 1. Vista de Registo
def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Já pode iniciar sessão.")
            return redirect('accounts:login')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})

# 2. Vista de Login Tradicional
def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        chave = request.POST.get('password')
        user = authenticate(request, username=usuario, password=chave)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect('portfolio:home')
        else:
            messages.error(request, "Utilizador ou password incorretos.")
    return render(request, 'accounts/login.html')
# 3. Pedir Link Mágico (Versão Corrigida e Segura)
def request_magic_link_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # .filter().first() evita o crash caso existam várias contas com o mesmo email
        user = User.objects.filter(email=email).first()
        
        if user is not None:
            link_obj = MagicLinkToken.objects.create(user=user)
            
            # Usar o reverse é mais seguro do que hardcodar o texto do URL
            # Nota: Garante que o 'name' no teu accounts/urls.py para a confirmação é 'magic_login_confirm'
            try:
                link_relativo = reverse('accounts:magic_login_confirm', kwargs={'token': link_obj.token})
                magic_url = request.build_absolute_uri(link_relativo)
            except Exception:
                # Caso a tua rota no urls.py se chame de outra forma (ex: 'login_magic')
                magic_url = request.build_absolute_uri(f"/accounts/magic-login/{link_obj.token}/")
            
            print("\n" + "="*60)
            print(f"--- LINK MÁGICO GERADO PARA: {email} ---")
            print(magic_url)
            print("="*60 + "\n")
            
            messages.info(request, "Link mágico gerado! Copie-o a partir do terminal do seu Codespaces.")
        else:
            messages.error(request, "Não existe utilizador com esse email.")
            
    return render(request, 'accounts/magic_request.html')
# 4. Confirmar Link Mágico
def magic_login_confirm_view(request, token):
    link_obj = get_object_or_404(MagicLinkToken, token=token)
    if link_obj.is_valid():
        link_obj.is_used = True
        link_obj.save()
        login(request, link_obj.user)
        messages.success(request, f"Autenticado via Link Mágico! Olá, {link_obj.user.username}.")
        return redirect('portfolio:home')
    else:
        messages.error(request, "O link expirou ou já foi usado.")
        return redirect('accounts:login')

# 5. Vista de Logout
def logout_view(request):
    logout(request)
    messages.info(request, "Sessão terminada.")
    return redirect('portfolio:home')