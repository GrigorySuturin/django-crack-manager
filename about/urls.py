from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('crack3/<int:c_id>/', views.index2, name='crack3'),
    path('videos/', views.videos, name='videos'),
    path('prikoli/', views.all_prikoli, name='all-jokes'),
    path('prikoli/<slug:post_slug>/', views.prikoli, name='jokes'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('category/<slug:cat_slug>', views.show_category, name='category'),
    path('tag/<slug:tag_slug>', views.show_tagpost, name='tag'),
]
