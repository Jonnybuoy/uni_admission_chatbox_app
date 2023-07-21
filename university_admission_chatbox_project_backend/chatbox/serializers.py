from rest_framework import serializers

from account.serializers import UserSerializer

from .models import ChatBotMessage


class ChatBotMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = ChatBotMessage
        fields = ['id', 'user', 'user_input', 'bot_response', 'timestamp']
