from django.urls import path
from . import views

urlpatterns = [
    path('schedule/main/', views.CourseListView.as_view(), name='main'),
    path('schedule/course_details/<int:pk>', views.CourseDetailView.as_view(), name='course_details'),
    path('schedule/teacher_details/<int:pk>', views.TeacherDetailView.as_view(), name='teacher_details'),
    path('schedule/add_course/', views.SignUpView.as_view(), name='add_course'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
]
