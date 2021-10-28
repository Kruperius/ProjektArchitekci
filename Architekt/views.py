from django.shortcuts import render, redirect
from .models import Projekt
from .formularze import Dodaj_proj, SignUpForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.

UserModel = get_user_model()

def strona_gl(request, *args, **kwargs):
	return render(request, 'glowna.html', {})

def architekci(request, *args, **kwargs):
	architekci = UserModel.objects.all()
	return render(request, 'architekci.html', {'architekci': architekci})

def projekty(request, *args, **kwargs):
	projekty = Projekt.objects.all()

	paginator = Paginator(projekty, 3)

	numer_str = request.GET.get('page')
	obj_str = paginator.get_page(numer_str)
	return render(request, 'projekty.html', {'projekty': obj_str})

def dodaj_architekta(request, *args, **kwargs):
	# formularz = Dodaj_arch(request.POST or None)
	# if request.method == 'GET':
	# 	return render(request, 'dodaj-architekta.html', {'formularz': formularz})

	if request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		formularz = SignUpForm(request.POST or None)
		if formularz.is_valid():
			user = formularz.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Potwierdź swoją torzsamość.'
			message = render_to_string('acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			to_email = formularz.cleaned_data.get('email')
			# email = EmailMessage(
   #          	mail_subject, message, to=[to_email]
   #          )
			# email.send()
			send_mail(mail_subject, message, None, [to_email])
			return HttpResponse('Potwierdz swój adres emailowy w celu zakończenia rejestracji')

		# kontekst = {'formularz': formularz}

	else:
		formularz = SignUpForm()	

	return render(request, 'dodaj-architekta.html', {'formularz': formularz})

def activate(request, uidb64, token):
    # try:
    uid = urlsafe_base64_decode(uidb64).decode()
    user = UserModel._default_manager.get(pk=uid)
    # except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    #     # user = None
    print(account_activation_token.check_token(user, token))
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        print(request.user.is_authenticated)
        user.save()
        print(request.user.is_authenticated)
        login(request, user)
        # return redirect('home')
        return HttpResponse('Dziękujemy za potwierdzenie emaila. Jesteś zarejestrowany.')
    else:
        return HttpResponse('Link aktywacyjny jest nieważny!')	

def dodaj_projekt(request, *args, **kwargs):
	formularz = Dodaj_proj(request.POST, request.FILES)
	if formularz.is_valid():
		new_proj = formularz.save(commit=False)
		new_proj.architekt=request.user
		new_proj.save()
	
		return redirect('moje-projekty')

	kontekst = {'formularz': formularz}
	
	return render(request, 'dodaj-projekt.html', kontekst)

def update_projekt(request, pk):

	projekt = Projekt.objects.get(id=pk)
	formularz = Dodaj_proj(instance=projekt)

	if request.method == 'POST':
		formularz = Dodaj_proj(request.POST, instance=projekt)
		if formularz.is_valid():
			formularz.save()
			return redirect('moje-projekty')

	kontekst = {'formularz': formularz}
	
	return render(request, 'dodaj-projekt.html', kontekst)

def delete_projekt(request, pk):

	projekt = Projekt.objects.get(id=pk)

	if request.method == 'POST':
		projekt.delete()
		return redirect('moje-projekty')

	kontekst = {'projekt': projekt}
	
	return render(request, 'usun-projekt.html', kontekst)

def signin(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			form = AuthenticationForm(request.POST)
			return render(request, 'logowanie.html', {'form': form})
	else:
		form = AuthenticationForm()
		return render(request, 'logowanie.html', {'form': form})	

def signout(request):
    logout(request)
    return redirect('/')

class ProjektyByUserListView(LoginRequiredMixin, ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Projekt
    template_name ='user/projekty_by_user.html'
    paginate_by = 3
    login_url = '/konta/login/'
    redirect_field_name = '/konta/logged_out/'

    def get_queryset(self):
        return Projekt.objects.filter(architekt=self.request.user) 

