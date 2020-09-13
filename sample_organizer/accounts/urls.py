from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.accountSettings, name="account"),
    path('samples/', views.samples, name="samples"),
    path('executor/<str:pk>/', views.executor, name="executor"),
    path('create_test/<str:pk>/', views.createTest, name="create_test"),
    path('update_test/<str:pk>/', views.updateTest, name="update_test"),
    path('delete_test/<str:pk>/', views.deleteTest, name="delete_test"),
    path('reset_password_sent/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
]