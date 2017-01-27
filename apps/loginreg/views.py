from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt

# Create your views here.

# request / index has to be first
def index(request):
    if 'online' not in request.session:
        request.session['online'] = False
    return render(request, "loginreg/index.html")

def bingo(request):
    if request.session['online']:
        return render(request, "loginreg/bingo.html")
        print "No bueno"
        return redirect(reverse('user_bingo'))

def login(request):
    user = User.objects.login(request.POST['email'],request.POST['password'])
    if user['em1']:
        messages.add_message(request, messages.INFO, "email, please?")
    if user['em2']:
        messages.add_message(request, messages.INFO, "no password, no love")
    if user['no_problem']:
        validate = User.objects.filter(email=request.POST['email'])
        if validate:
            print "user checks out"
            password = request.POST['password'].encode('utf-8')
            pwhash = validate[0].pw_hash.encode('utf-8')
            pw_validate = bcrypt.hashpw(password,pwhash)
            if pw_validate == validate[0].pw_hash:
                request.session['online']= True
                return redirect(reverse('user_bingo'))
        messages.add_message(request, messages.INFO, "You have a problem with either email or pw")
    return redirect(reverse('user_index'))

def logout(request):
    request.session['online'] = False
    return redirect(reverse('user_index'))

def register(request):
    user = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['confirm_pw'])
    if user['em1']:
        messages.add_message(request, messages.INFO, "no email, no love")
    if user['em2']:
        messages.add_message(request, messages.INFO, "that email looks fishy")
    if user['em3']:
        messages.add_message(request, messages.INFO, "First name must be 2 characters or longer")
    if user['em4']:
        messages.add_message(request, messages.INFO, "Last name must be 2 characters or longer")
    if user['em5']:
        messages.add_message(request, messages.INFO, "pw length should be longer than 8 characters")
    if user['em6']:
        messages.add_message(request, messages.INFO, "pw doesn't add up")
    if user['no_problem']:
        print "THIS IS THE DROID YOU ARE LOOKING FOR"
        password = request.POST['password'].encode('utf-8')
        pwhash = bcrypt.hashpw(password, bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'], pw_hash=pwhash)
        print User.objects.all()
        request.session['online']=True
        request.session['first_name'] = request.POST['first_name']
        return redirect(reverse('user_bingo'))
    return redirect(reverse('user_index'))


# def show(request):
#     print(request.method)
#     return render(request, "loginreg/show_users.html")
