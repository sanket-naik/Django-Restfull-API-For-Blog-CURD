from django.urls import path
from . views import BlogViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',BlogViewSet, base_name='Blogs')
urlpatterns=router.urls

# urlpatterns = [
#     path('',views.BlogList.as_view()),
#     path('<int:pk>/',views.BlogDetail.as_view())
# ]
