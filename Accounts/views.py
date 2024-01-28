from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from Accounts.models import CustomUser
from order.models import Order

def sign_up(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')  
        Email = request.POST.get('Email')  
        number = request.POST.get('number')  
        Address = request.POST.get('Address')
        city = request.POST.get('city')  
        password = request.POST.get('Password')  

        user = CustomUser.objects.create(
            firstName=firstName,
            lastName=lastName,
            username=username,
            Email=Email,
            number=number,
            Address=Address,
            city= city
        )
        user.set_password(password)
        user.save()
        return redirect ('/')
    return render(request, 'sign-up.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Check the login type selected (username or email)
            login_type = request.POST.get('login_type')
            if login_type == 'email':
                username_or_email = form.cleaned_data.get('username')
            else:
                username_or_email = form.cleaned_data.get('username')

            # Authenticate the user based on the login type
            user = None
            if login_type == 'email':
                # Authenticate by email
                user = CustomUser.objects.filter(email=username_or_email).first()
            else:
                # Authenticate by username
                user = form.get_user()

            if user is not None:
                login(request, user)
                return redirect('profile')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    orders = Order.objects.filter(user=user)  # Retrieve the user's order history

    context = {
        'user': user,
        'orders': orders,
    }

    return render(request, 'profile.html', context)
