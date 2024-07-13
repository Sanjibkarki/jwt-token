from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .forms import LoginForm
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        
        request.session['refresh'] = data['refresh']
        return Response(data)
    
class Index(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,"index.html")

class students(APIView):
    authentication_classes =[JWTAuthentication]
    def get(self,request):
        return Response({
            "name":"sanjeeb"
        })
        


def Login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")
        return render(request, "login.html", {"form": form, "errors": form.errors})
def Logout(request):
    logout(request)
    return redirect('login')
    

