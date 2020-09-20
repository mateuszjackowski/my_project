from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import TestForm, CreateUserForm, ExecutorForm
from .filters import TestFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    ctx ={'form': form}
    return render(request, 'accounts/register.html', ctx)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user-page')
        else:
            messages.info(request, 'Username or password is incorrect')
    ctg ={}
    return render(request, 'accounts/login.html', ctg)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    tests = Test.objects.all()
    executors = Executor.objects.all()
    total_executors = executors.count()
    total_tests = tests.count()
    tested = tests.filter(status='Tested').count()
    in_research = tests.filter(status='In Research').count()
    ctx = {'tests': tests,
           'executors': executors,
           'total_tests': total_tests,
           'tested': tested,
           'in_research': in_research}
    return render(request, 'accounts/dashboard.html', ctx)

@login_required(login_url='login')
@allowed_users(allowed_roles=['executor', 'admin'])
def userPage(request):
    tests = request.user.executor.test_set.all()
    total_tests = tests.count()
    tested = tests.filter(status='Tested').count()
    in_research = tests.filter(status='In Research').count()
    ctx = {'tests': tests,
           'total_tests': total_tests,
           'tested': tested,
           'executor': request.user.executor,
           'in_research': in_research}
    return render(request, 'accounts/user.html', ctx)

@login_required(login_url='login')
@allowed_users(allowed_roles=['executor', 'admin'])
def accountSettings(request):
    executor = request.user.executor
    form = ExecutorForm(instance=executor)
    if request.method == 'POST':
        form = ExecutorForm(request.POST, request.FILES, instance=executor)
        if form.is_valid():
            form.save()
    ctx = {'form': form}
    return render(request, 'accounts/account_settings.html', ctx)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def samples(request):
    samples = Sample.objects.all()
    ctx = {'samples': samples}
    return render(request, 'accounts/samples.html', ctx)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def executor(request, pk):
    executor = Executor.objects.get(id=pk)
    tests = executor.test_set.all()
    test_count = tests.count()
    myFilter = TestFilter(request.GET, queryset=tests)
    tests = myFilter.qs
    ctx = {'executor': executor,
           'tests': tests,
           'test_count': test_count,
           'myFilter': myFilter}
    return render(request, 'accounts/executor.html', ctx)

@login_required(login_url='login')
def createTest(request, pk):
    TestFormSet = inlineformset_factory(Executor, Test, fields=('sample', 'status'), extra=10)
    executor = Executor.objects.get(id=pk)
    formset = TestFormSet(queryset=Test.objects.none(), instance=executor)
    # form = TestForm(initial={'executor' : executor})
    if request.method == 'POST':
        # form = TestForm(request.POST)
        formset = TestFormSet(request.POST, instance=executor)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    ctx = {'formset': formset}
    return render( request, 'accounts/test_form.html', ctx)

@login_required(login_url='login')
def updateTest(request, pk):
    test = Test.objects.get(id=pk)
    form = TestForm(instance=test)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('home')
    ctx = {'form': form}
    return render(request, 'accounts/test_form.html', ctx)

@login_required(login_url='login')
@admin_only
def deleteTest(request, pk):
    test = Test.objects.get(id=pk)
    if request.method == 'POST':
        test.delete()
        return redirect('home')
    ctx = {'test': test}
    return render( request, 'accounts/delete.html', ctx)