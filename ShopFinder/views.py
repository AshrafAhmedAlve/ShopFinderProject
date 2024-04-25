from django.shortcuts import render, redirect,HttpResponse
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')

def ShopFinder(request):
    return render(request, "index.html")

def signinOptions(request):
    return render(request, "signinOptions.html")


def SignIn(request):
     if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/userdashboard/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")      
     return render(request, 'SignIn.html')


def SignUp(request):
     if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/signin/')
         
         
         
     return render(request, "signup.html")


def AboutUs(request):
    return render(request, "aboutus.html")

def UserDashboard(request):
    return render(request, "userdashboard.html")

def ShopOwnerDashboard(request):
    return render(request, "shopownerdashboard.html")



def shop_listing(request):
    # Assume you have some logic here to fetch shop data from your database
    shops = Shop.objects.all()
    
     
    return render(request, 'shop_listing.html', {'shops': shops})



from .forms import ShopForm

def create_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Shop Owner Dashboard')  # Redirect to a success URL
    else:
        form = ShopForm()
    return render(request, 'create_shop.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Shop
from .forms import ShopForm

def update_shop(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_details', shop_id=shop_id)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'update_shop.html', {'form': form, 'shop': shop})

def shop_details(request, shop_id):
    shop = Shop.objects.get(pk=shop_id)
    return render(request, 'shop_details.html', {'shop': shop})






