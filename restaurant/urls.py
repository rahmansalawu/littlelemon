from django.urls import path, include
from . import views
from .views import bookingview, UserViewSet,userview ,Goons , BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'goons', Goons, basename='goons')
router.register(r'tables', BookingViewSet, basename='tables')
#urlpatterns = router.urls

urlpatterns = [
    path('', views.index, name="index"),
    path('booking/', bookingview.as_view(), name="booking"),
    path('users/', userview.as_view(), name="users"),
    path('', include(router.urls)),
    path('api-token-auth/',obtain_auth_token)
    #path('goons/', Goons.as_view(), name="goons")
]
