from django.http import HttpResponse


def endpoint(request):
    if request.method == 'POST':
        print('endpoint post')
        print(request.POST)
    else:
        print('endpoint get')
    return HttpResponse('ok')