from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging


logger = logging.getLogger('django')


@csrf_exempt
def endpoint(request):
    if request.method == 'POST':
        logger.info('POST request: {}'.format(request.POST))
        logger.info('META request: {}'.format(request.META))
        logger.info('request: {}'.format(request))
        aws_type = request.META.get('HTTP_X_AMZ_SNS_MESSAGE_TYPE')
        logger.info('aws_type: {}'.format(aws_type))

        if aws_type == 'SubscriptionConfirmation' or aws_type == 'Notification':
            subscription_url = request.POST.get('SubscribeURL')
            logger.info('SubscribeURL: {}'.format(subscription_url))
    return HttpResponse('ok')