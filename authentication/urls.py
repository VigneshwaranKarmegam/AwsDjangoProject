from authentication.views import RegisterView, LoginWithUserDetail
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register', RegisterView.as_view(), name='auth_register'),
    
    #this is the login we need to customize the TokenObtainPairView and use our own
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login', LoginWithUserDetail.as_view(), name='token_obtain_pair'),   # login api
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]