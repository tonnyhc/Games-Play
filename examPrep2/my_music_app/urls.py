"""

•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page
"""
from django.urls import path, include

from examPrep2.my_music_app.views import index, details_album, delete_album, add_album, edit_album, details_profile, \
    delete_profile

urlpatterns = (
    path('', index, name='home page'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='details album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album')
    ])),
    path('profile/', include([
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
)