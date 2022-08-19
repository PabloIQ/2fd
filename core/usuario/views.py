from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from usuario.models import CustmUser

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'main.html')

def auth_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            code_user = f"{user.username}: {user.code}"
            #Enviar SMS
            print('code_user: ', code_user)
            return redirect('verify-view')
    return render(request, 'auth.html')

def verify_view(request):
    print('-----verify_view')
    pk = request.session.get('pk')
    print('pk: ', type(pk))
    if pk:
        user = CustmUser.objects.get(pk=pk)
        code = user.code
        if request.method == 'POST':
            num = request.POST.get('number')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('home-view')
            else:
                return redirect('login-view')
    return render(request, 'verify.html')

def logout_view(request):
    logout(request)
    return redirect('login-view')