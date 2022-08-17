from django.urls import path
from .views import BikeListView, BikeDetailView, BikeCreateView, BikeUpdateView, BikeDeleteView

urlpatterns = [
    path('bike/', BikeListView.as_view(), name='bike_list'),
    path('bike/<int:pk>/', BikeDetailView.as_view(), name='bike_detail'),
    path('bike/create/', BikeCreateView.as_view(), name='bike_create'),
    path('bike/<int:pk>/update/', BikeUpdateView.as_view(), name='bike_update'),
    path('bike/<int:pk>/delete/', BikeDeleteView.as_view(), name='bike_delete'),
]