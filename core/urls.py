
from django.contrib import admin
from django.urls import path
from AppMymoney.views import *
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", index, name="index"),
    path ("login/", Login, name="login"),
    path ("register/", Register, name="register"),
    path ("profil/", Profil, name="profil"),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
    ]