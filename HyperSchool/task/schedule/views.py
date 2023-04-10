from django.shortcuts import render, redirect
from .forms import SearchForm, ApplicationForm, NewUserForm
from .models import Course, Teacher, Student
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


class CourseListView(ListView):
    model = Course
    template_name = 'main.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Course.objects.all()

        if query is not None:
            queryset = queryset.filter(Q(title__icontains=query))
            return queryset
        return queryset


class CourseDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(id=kwargs['pk'])
        teachers = Teacher.objects.all()
        students = Student.objects.all()
        return render(request, 'course_details.html', {'course': course, 'teachers': teachers, 'students': students})


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_details.html'


class SignUpView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = ApplicationForm()
        return render(request, 'add_course.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'add_course.html', {'form': form})


class UserSignUpView(TemplateView):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = NewUserForm()
        return render(request=request, template_name="signup.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration Successful")
            return redirect("main")
        messages.error(request, "Registration Unsuccessful")
        return render(request=request, template_name="signup.html", context={"form": form})


class UserLoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, template_name="login.html", context={'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main")
            messages.error(request, "Invalid Login")
            return render(request, template_name="login.html", context={'form': form})
        messages.error(request, "Invalid Login")
        return render(request, template_name="login.html", context={'form': form})
