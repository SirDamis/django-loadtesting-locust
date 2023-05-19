import multiprocessing, time
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def square_numbers(request):
    squares = {num: num**2 for num in range(1, 1000001)}
    return JsonResponse(squares)

@require_http_methods(["GET"])
def add_two_numbers(request):
    time.sleep(5) # Illustrate a long running task being performed

    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    result = a + b

    return JsonResponse({'result': result})