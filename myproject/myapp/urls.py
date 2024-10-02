# myapp/urls.py
from django.urls import path
from .views import question_1_view, question_2_view, test_signal  # Also import test_signal
from . import views


urlpatterns = [
    path('question-1/', views.question_1_view, name='question_1'),  # Ensure this view is defined
    path('question-2/', views.question_2_view, name='question_2'),  # Ensure this view is defined
    path('test-signal/', views.test_signal, name='test_signal'), 
    path('question-3/', views.question_3_view, name='question_3'),
    path('custom-classes/', views.custom_classes_view, name='custom_classes'),

]