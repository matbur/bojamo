from django import forms

from .models import Priority, Status, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password',
                  'permissions', 'url', 'description', 'active']
        widgets = {'password': forms.PasswordInput()}


class UserRegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password']
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        form = self.cleaned_data
        if form['password'] != form['repeat_password']:
            self.errors['password'] = 'Repeated password is invalid!'
        if User.objects.filter(email=form['email']):
            self.errors['email'] = 'This email adress is in use!'
        if User.objects.filter(username=form['username']):
            self.errors['login'] = 'This login already exists!'
        if len(self.errors) == 0:
            self._success = "Registration successfull!"
        return self.cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username', 'password'}
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        form = self.cleaned_data
        if not User.objects.filter(username=form['username'], password=form['password']):
            self.errors['authentication'] = 'Username or password is invalid!'
        return self.cleaned_data


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = ['name']
