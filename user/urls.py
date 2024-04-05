from django.urls import path
from .views import UserListView,UserCreateView,UserRetrieveView,UserUpdateView,UserDeleteView,LoginView,LogoutView

urlpatterns = [
    path('',UserListView.as_view()),
    path('create/',UserCreateView.as_view()),
    path('<int:pk>/read/',UserRetrieveView.as_view()),
    path('<int:pk>/update/',UserUpdateView.as_view()),
    path('<int:pk>/delete/',UserDeleteView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view())


]