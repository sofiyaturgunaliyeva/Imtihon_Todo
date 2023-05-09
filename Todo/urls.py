
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlar/', hamma_studentlar),
    path('rejalar/', hamma_rejalar),
    path('bajarilmagan/', bajarilmagan_r),
    path('uchinchi_k/', uchinchi_kurs),
    path('reja_ochir/<int:son>/', reja_ochir),
]
