from  django.urls import path
from Blog import views
from django.conf.urls.static import static
from django.conf import settings
from .views import BlogDetailView
from django.views.static import serve


urlpatterns = [
    
    path('/<slug:slug>',BlogDetailView.as_view(),name='blogs_detail'),
    path('register/',views.Register),
    path('login/',views.Login),
    path('',views.blogs),
    path('addblogs/',views.Add_blogs),
    path('logout/',views.Logout),
    path('search/',views.search),
    path(r'^media/(?P<path>.*)$' ,serve,{'document_root':settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
