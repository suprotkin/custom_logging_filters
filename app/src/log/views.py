import json
import logging

from django.http import JsonResponse
from django.views import View

from src.common.redis_client import redis_client

logger = logging.getLogger(__name__)


class LogView(View):
    def get(self, request):
        logger.info('GET: Hello, World!')
        return JsonResponse({'message': 'Hello, World!'})

    def post(self, request):
        message = request.POST.get('message')
        logger.info(f'POST: {message}')
        return JsonResponse({'message': message})


class LogFilterView(View):
    def get(self, request):
        # import pydevd_pycharm
        # pydevd_pycharm.settrace('192.168.0.102', port=6664, stdoutToServer=True, stderrToServer=True)

        logger.info('GET: Get log filter')
        log_filter = redis_client.get('log_filter')
        return JsonResponse({'filter': log_filter})

    def post(self, request):
        logger.info('POST: Set log filter')
        post = request.POST
        data = json.loads(request.body)
        log_filter = data.get('log_filter')
        redis_client.set('log_filter', log_filter)
        return JsonResponse({'message': 'Log filter set!'})

    def delete(self, request):
        logger.info('DELETE: Clear log filter')
        redis_client.delete('log_filter')
        return JsonResponse({'message': 'Log filter cleared!'})
