
from django.urls import path
from . import views
urlpatterns = [

    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="trackerstatus"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>/",views.products,name="products"),
    path("checkout/",views.checkout,name="checkout"),

]
