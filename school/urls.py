from django.urls import path
from .views import *

urlpatterns = [
    path('parent/<int:pk>/', ParentDetail.as_view(), name='parent details'),
    path('parent/', ParentList.as_view(), name='parent list'),
    path('contribution/<int:pk>/', ContributionDetail.as_view(), name = 'contribution details'),
    path('contribution/', ContributionList.as_view(), name = 'contribution list'),
]
