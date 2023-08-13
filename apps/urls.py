from django.urls import path, include
from . import views
from .viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hero', HeroViewSet)
router.register('member', MemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/phone/<str:phone>/', get_member_by_phone),
    path('', views.home, name='home'),
    path('member/', views.member_index, name='member-index'),
    path('member/add/', views.member_add, name='member-add'),
    path('member/view/<int:_id>/', views.member_update, name='member-view'),
    path('member/delete/<int:_id>/', views.member_delete, name='member-delete'),
    path('setting/hero/', views.hero_index, name='hero-index'),
    path('setting/hero/add/', views.hero_add, name='hero-add'),
    path('setting/hero/update/<int:_id>/', views.hero_update, name='hero-update'),
    path('setting/hero/delete/<int:_id>/', views.hero_delete, name='hero-delete'),
    path('icon/', views.icon, name='icon'),
    path('profile/', views.profile, name='profile'),
    path('tables/', views.table, name='tables'),
]
