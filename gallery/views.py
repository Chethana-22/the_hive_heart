
import email
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import artist , painting ,Art,Photography,Person
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def HomePage(request):
    return render(request,"index.html")

def ContactPage(request):
    if request.method == 'POST':
        name_r= request.POST['first_name']
        email_r = request.POST['email']
        info=Person(request,email=email)
        info.save()
        messages.info(request,'Form submitted')
        return redirect('Home-Page')
    else:
        return render(request,'contact.html')
        

   
def AboutPage(request):
    return render(request,"about.html")

@login_required(login_url='/login/')
def ArtistPage(request):
    artist_all  = artist.objects.all()
    return render(request,"artists.html",{'Artists':artist_all})

def LoginPage(request):
    if request.method == 'POST':

        User_name = request.POST['Lusername']
        # Last_Name = request.POST['Last_Name']
        # Your_Email = request.POST['Your_Email']
        # Your_Phone = request.POST['Your_Phone']
        Password= request.POST['password']
         
        user=auth.authenticate(request,username=User_name,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('Home-Page')
        else:
            messages.info(request,'Inavlid credentials')
            return redirect('Login-Page')


    else:
        return render(request,'login.html')



def  SignUp(request):
    # form = UserCreationForm()

    if request.method == 'POST':
    #     form=UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    # context = {'form'.form}
   
        User_name = request.POST['Susername']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Password1= request.POST['password1']
        Password2= request.POST['password2']

        print(User_name)


        if Password1==Password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('Sign-Up')

            elif User.objects.filter(username=User_name).exists():
                messages.info(request,'username taken')
                return redirect('Sign-Up')

            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=User_name,email=email,password=Password1)
                user.save()
                print('user created')
                return redirect('Login-Page')
        else:
                messages.info(request,'Inavlid Password')
                return redirect('Home-Page')

    else:
        return render(request,'signup.html')

@login_required(login_url='/login/')
def Paintings(request,pk):
        Painting=painting.objects.filter(Artist__pk=pk)
        return render(request,'products.html',{'Paintings':Painting})

@login_required(login_url='/login/')
def All_Paintings(request):
        All_Painting=painting.objects.all()
        return render(request,'products.html',{'Paintings':All_Painting})

@login_required(login_url='/login/')
def GalleryPage(request):
         return render(request,'exhibition.html')
@login_required(login_url='/login/')
def GalleryArts(request):
    art = Art.objects.all()
    return render(request,'museum.html',{'Arts':art})
@login_required(login_url='/login/')
def GalleryPhotography(request):
    photo = Photography.objects.all()
    return render(request,'photo.html',{'Photography':photo})

def logout(request):
    auth.logout(request)
    return redirect('Home-Page')


         
         




