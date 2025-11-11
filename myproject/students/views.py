from django.http import JsonResponse, HttpResponseNotFound
from .models import Student
from django.views.decorators.http import require_GET

@require_GET
def get_all_students(request):
    qs = Student.objects.all().values('id','name','age')
    return JsonResponse(list(qs), safe=False)

@require_GET
def get_student_by_id(request, student_id):
    try:
        s = Student.objects.values('id','name','age').get(id=student_id)
        return JsonResponse(s)
    except Student.DoesNotExist:
        return HttpResponseNotFound({'error': 'student not found'})

@require_GET
def filter_age_gte_20(request):
    qs = Student.objects.filter(age__gte=20).values('id','name','age')
    return JsonResponse(list(qs), safe=False)

@require_GET
def filter_age_lte_25(request):
    qs = Student.objects.filter(age__lte=25).values('id','name','age')
    return JsonResponse(list(qs), safe=False)

@require_GET
def order_by_name(request):
    qs = Student.objects.order_by('name').values('id','name','age')
    return JsonResponse(list(qs), safe=False)

@require_GET
def get_unique_ages(request):
    ages = Student.objects.values_list('age', flat=True).distinct()
    return JsonResponse(list(ages), safe=False)

@require_GET
def count_students(request):
    total = Student.objects.count()
    return JsonResponse({'total': total})
