from .models import User
from django.db.models import Q

def authenticate(request,username=None,password=None):
    try:
        password_check = None
        user_none = None
        user = User.objects.get(Q(phone_number__iexact=username)|Q(email__iexact=username)) 
        if user is not None:
            if user.check_password(password):
                return user
                print('line10')
            else:
                print('line11')
                password_check = "Password you entered is wrong"
                return password_check
        else:
            print('line13')
            user_none = True
            return user_none
            raise forms.ValidationError('User does not exists')
    except:
        pass