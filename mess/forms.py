
from django.forms import ModelForm
from mess.models import Message


# class MessageForm(forms.Form):
#     text = forms.CharField(max_length=255)
#
#     def save(self):
#         new_message = Message.object.create(text=self.cleaned_data['text'])
#         return new_message

# class MessageForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ('text',)

class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ('text',)