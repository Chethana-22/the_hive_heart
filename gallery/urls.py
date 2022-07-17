from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePage,name="Home-Page"),
    path('contact/',ContactPage,name="Contact-Page"),
    path('about/',AboutPage,name="About-Page"),
    path('artists/',ArtistPage,name="Artist-Page"),
    path('signup/',SignUp,name='Sign-Up'),
    path('login/',LoginPage,name="Login-Page"),
    path('paintings/<int:pk>',Paintings,name="Painting-Page"),
    path('all_paintings/',All_Paintings,name="AllPainting-Page"),
    path('gallery/',GalleryPage,name="Gallery-Page"),
    path('gallery3D/',GalleryArts,name="3DArts-Page"),
    path('Photography/',GalleryPhotography,name="Photography-Page"),
    path('logout/',logout,name="Logout-Page")  
]
