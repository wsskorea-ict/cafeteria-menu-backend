from django.db import connections
from django.db import OperationalError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
# @swagger_auto_schema(tags=['서버가 정상적으로 동작중인지 헬스체크를 수행합니다.'],
#                      responses={204: '서버가 정상적으로 동작중입니다.', 500: '서버가 정상적으로 동작하고 있지 않습니다.'})
def health(request):
    """
    서버가 정상적으로 동작중인지 확인합니다.

    ---
    API 문서가 정상적으로 생성되는지 확인합니다. 배포때는 외부에서 해당 URL로 접근할 수 없습니다.
    """
    connected = False

    try:
        conn = connections['default']

        cursor = conn.cursor()
        cursor.close()

    except OperationalError:
        connected = False

    else:
        connected = True

    finally:
        return Response(status=status.HTTP_204_NO_CONTENT if connected else status.HTTP_500_INTERNAL_SERVER_ERROR)
