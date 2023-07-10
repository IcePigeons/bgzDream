from json import encoder

from django.http import JsonResponse


def success_response(data):
    # 创建包含成功数据的字典
    success_data = {'data': data, 'message': '执行成功', 'code': 200}
    # 返回JsonResponse对象
    return JsonResponse(success_data, status=200)


def error_response(msg):
    # 创建包含错误信息的字典
    error_data = {'data': None, 'message': msg, 'code': 500}
    # 返回JsonResponse对象
    return JsonResponse(error_data, status=500)
