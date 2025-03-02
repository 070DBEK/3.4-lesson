from django.urls import path
from .views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView, AuthorBooksListView


urlpatterns = [
    path('', AuthorListCreateView.as_view(), name='author-list-create'),
    path('<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),
    path('<int:author_id>/books/', AuthorBooksListView.as_view(), name='author-books'),
]