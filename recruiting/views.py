from django.http import HttpResponse
from django.core.mail import send_mail


def endpoint(request):
    if request.method == 'POST':
        aws_type = request.META.get('x-amz-sns-message-type')
        if aws_type == 'SubscriptionConfirmation' or aws_type == 'Notification':
            subscription_url = request.POST.get('SubscribeURL')
            send_mail('Subscription URL', subscription_url, 'a.popovychenko@gmail.com',
                      ['a.popovychenko@gmail.com'], fail_silently=False)
    return HttpResponse('ok')