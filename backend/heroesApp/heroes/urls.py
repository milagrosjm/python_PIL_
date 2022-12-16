from django.urls import path
from heroes.views import HeroApiView, CreateHeroApiView, DetailHeroApiView
urlpatterns = [
    path('heroes-list/', HeroApiView.as_view(), name='heroes_list'),
    path('create-hero/', CreateHeroApiView.as_view(), name='create'),
    path('detail-hero/<int:pk>/', DetailHeroApiView.as_view(), name='detail'),
]