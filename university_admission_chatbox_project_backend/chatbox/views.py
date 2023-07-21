from django.http import JsonResponse
from rest_framework.decorators import authentication_classes, api_view, permission_classes

from chatbox.chat import get_response


@api_view(['POST'])
def chatbot(request):
    data = request.data
    
    print(data)
    user_input = data.get('userInput', '').strip()
    
    if user_input:
        response = get_response(user_input)
        
        return JsonResponse({'response': response})
    
    return JsonResponse({'hello': 'helooo'})
