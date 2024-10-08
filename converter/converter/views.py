from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import requests

class CurrencyViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=["GET"], detail=False)
    def rate(self, request, *args, **kwargs):
        val_from = request.query_params.get('from')
        val_to = request.query_params.get('to')
        value = request.query_params.get('value')

        if not val_from or not val_to or not value:
            return Response({'error': 'Missing required parameters'}, status=400)

        api_key = '20e3c7f654c3c0da2c8d920c08721d31'
        url = 'http://api.currencylayer.com/live'

        params = {
            'access_key': api_key,
            'currencies': val_to,
            'source': val_from,
            'format': 1
        }

        response = requests.get(url, params=params)

        if response.json()['success'] == True:
            data = response.json()
            name = val_from + val_to
            return Response(data={'res': round(data['quotes'][name]*int(value), 2)})

        return Response({'error': 'Currency API request failed'}, status=response.status_code)
