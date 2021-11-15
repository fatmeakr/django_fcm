from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _


def error_404(request, exception):
    message = _('Page not Found.')
    response = JsonResponse(data={'message': message, 'code': 404})
    response.status_code = 404
    return response


def error_500(request):
    message = _('There is a problem here.')
    response = JsonResponse(data={'message': message, 'code': 500})
    response.status_code = 500
    return response
