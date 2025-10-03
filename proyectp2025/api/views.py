from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class VistaProtegida(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': '¡Acceso autorizado!',
            'user': request.user.username,
            'email': request.user.email
        })