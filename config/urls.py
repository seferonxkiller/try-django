from config import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('article.urls',namespace='articles')),
    path('blog/',include('blog.urls',namespace='blogs')),
    path('account/',include('account.urls',namespace='auth')),
    path('recipes/', include('recipes.urls', namespace='recipes')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

