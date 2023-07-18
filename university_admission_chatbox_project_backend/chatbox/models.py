from django.db import models
from account.models import User


class ChatBotMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_input = models.CharField(max_length=255)
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
