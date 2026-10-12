# from django.shortcuts import get_object_or_404, render
# from .models import Course


# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, "courseapp/course_list.html", {"courses": courses})


# def course_detail(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     return render(request, "courseapp/course_details.html", {"course": course})


from django.views.generic import ListView, DetailView
from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = "courseapp/course_list.html"
    context_object_name = "courses"


class CourseDetailView(DetailView):
    model = Course
    template_name = "courseapp/course_details.html"
    context_object_name = "course"
