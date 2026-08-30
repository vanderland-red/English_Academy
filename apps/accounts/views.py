from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm

class UserDashboardView(View):

    def get(self, request):
        return render(request, 'user/dashboard.html')


class UserRegisterView(View):

    form_class = UserRegisterForm
    template_name = 'user/register.html'

    # درخواست GET
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # در خواست POST
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()

            messages.success(request,'ثبت نام با موفقیت انجام شد.')

            return redirect('user:dashboard')
        else:

            if form.errors.get('username'):
                messages.error(request, form.errors['username'][0])

            if form.errors.get('phone'):
                messages.error(request, form.errors['phone'][0])

            if form.errors.get('email'):
                messages.error(request, form.errors['email'][0])

            if form.errors.get('password'):
                messages.error(request, form.errors['password'][0])

            if form.non_field_errors():
                messages.error(request, form.non_field_errors()[0])

        return render(request, self.template_name,{'form': form})



class UserLoginView(View):

    def get(self, request):
        form = UserLoginForm()

        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            login(request, form.user)

            messages.success(request,'با موفقیت وارد حساب کاربری شدید')
            return redirect('user:dashboard')
        
        else :


            if form.non_field_errors():
                messages.error(request, form.non_field_errors()[0])

        return render(request, 'user/login.html', {'form': form})




#==================
# User Logout
#==================
class UserLogoutView(View):

    def get(self, request):
        logout(request)

        messages.success(request, 'با موفقیت از حساب کاربری خود خارج شدید')
        return redirect('/')