from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging


logger = logging.getLogger(__name__)


@csrf_exempt
def endpoint(request):
    if request.method == 'POST':
        logger.info('POST request: {}'.format(request.POST))
        aws_type = request.META.get('x-amz-sns-message-type')
        logger.info('aws_type: {}'.format(aws_type))

        if aws_type == 'SubscriptionConfirmation' or aws_type == 'Notification':
            subscription_url = request.POST.get('SubscribeURL')
            logger.info('SubscribeURL: {}'.format(subscription_url))
    return HttpResponse('ok')