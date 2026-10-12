# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.course_list, name="courselist"),
#     path("courses/<int:pk>", views.course_detail, name="coursedetail"),
# ]

from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.course_list, name="courselist"),
#     path("courses/", views.course_list, name="courses"),
#     path("courses/<int:pk>/", views.course_detail, name="coursedetail"),
# ]

urlpatterns = [
    path("", views.CourseListView.as_view(), name="courselist"),
    path("courses/", views.CourseListView.as_view(), name="courses"),
    path("courses/<int:pk>", views.CourseDetailView.as_view(), name="coursedetail"),
]
