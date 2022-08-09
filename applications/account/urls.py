from applications.account.views import RegisterApiView, ActivationApiView, ChangePasswordApiView, \
    ForgotPasswordCompleteApiView, ForgotPasswordApiView, LogOutApiView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('active/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordCompleteApiView.as_view()),


]