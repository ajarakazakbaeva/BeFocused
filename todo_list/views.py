from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView

from .models import Goal
from django.shortcuts import render, get_object_or_404
from .forms import GoalForm, GoalFilterForm
from django.shortcuts import redirect


class UserRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('goal_list')
    def form_valid(self, form):
        result = super(UserRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
        password=cd['password1'])
        login(self.request, user)
        return result

def goal_list(request):
    user = request.user
    form = GoalFilterForm(request.GET)
    if not form.is_valid():
        goals = Goal.objects.filter(created_date__lte=timezone.now(), author=user).order_by('created_date')
    is_completed = form.cleaned_data.get('is_completed')
    if is_completed=='True':
        print('True')
        goals = Goal.objects.filter(created_date__lte=timezone.now(), author=user, is_completed = True).order_by('created_date')
    else:
        print('False')
        goals = Goal.objects.filter(created_date__lte=timezone.now(), author=user, is_completed = False).order_by('created_date')

    return render(request, 'todo_list/goal_list.html', {'goals': goals, 'form':form, 'welcome_text': 'My Goals'})



def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'todo_list/goal_detail.html', {'goal': goal, 'welcome_text':'My Goals'})

def goal_new(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.author = request.user
            goal.created_date = timezone.now()
            goal.save()
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalForm()
    return render(request, 'todo_list/goal_edit.html', {'form': form, 'welcome_text':'My Goals'})

def goal_edit(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.author = request.user
            goal.published_date = timezone.now()
            goal.save()
            return redirect('goal_detail', pk=goal.pk)
    else:
        form = GoalForm(instance=goal)
    return render(request, 'todo_list/goal_edit.html', {'form': form, 'welcome_text':'My Goals'})

def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.delete()
    return redirect('goal_list')

def about(request):
    user = request.user
    welcome_text = 'Get Started'
    if user.is_authenticated:
        goal_qs = Goal.objects.filter(author=user)
        if len(goal_qs)>0:
            welcome_text = 'My Goals'
    return render(request, 'todo_list/about.html', {'welcome_text':welcome_text})