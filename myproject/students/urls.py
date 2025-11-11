from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_students, name='students-all'),
    path('id/<int:student_id>/', views.get_student_by_id, name='student-by-id'),
    path('filter/age-gte-20/', views.filter_age_gte_20, name='age-gte-20'),
    path('filter/age-lte-25/', views.filter_age_lte_25, name='age-lte-25'),
    path('order/name/', views.order_by_name, name='order-by-name'),
    path('unique/ages/', views.get_unique_ages, name='unique-ages'),
    path('count/', views.count_students, name='count-students'),
]
