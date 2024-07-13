from django.urls import path,include
from .views import Index,Login,Logout,MyTokenObtainPairView,students
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', Index.as_view(),name="index"),
    path('login',Login,name="login"),
    path('logout',Logout,name="logout"),
    path('api/',students.as_view()),
    
]