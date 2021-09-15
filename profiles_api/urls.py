from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()

#only need to provide base_name if don't define queryset in ViewSet class or want to override existing name of queryset
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfilesViewSet)
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]