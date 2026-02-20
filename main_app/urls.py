from django.urls import path
from . import views #Import views to connect routes to view functions

# render take first request from the function declaration 
# next it takes the template to renderr similar to ejs res.render
urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
]