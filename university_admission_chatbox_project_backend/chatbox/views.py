from django.http import JsonResponse
from chatbox.chat import get_response


def chatbot(request):
    if request.method == 'POST':
        data = request.POST
        user_input = data.get('user_input', '').strip()
        
        if user_input:
            response = get_response(user_input)
            
            return JsonResponse({'response': response})
    
    return JsonResponse({})
