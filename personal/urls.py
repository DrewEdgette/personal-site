from django.contrib import admin
from django.urls import path, include
from personal.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
