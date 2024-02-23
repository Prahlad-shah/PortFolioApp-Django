from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', )