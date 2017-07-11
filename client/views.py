from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.contrib.auth.decorators import login_required
from .models import UserType, Challenge
from .forms import ChallengeForm
# Create your views here.


@login_required
def user(request):
    response = {'user': request.user.username}
    t = UserType.objects.filter(user__exact=request.user)
    for q in t:
        ch = q.group
        break
    response['group'] = ch
    if ch == 'MEMBER':
        challenges = Challenge.objects.all()
        response['challenges'] = challenges
    if ch == 'ADMIN':
        if request.method == 'POST':
            challenge_data = ChallengeForm(request.POST)
            if challenge_data.is_valid():
                challenge = Challenge()
                challenge.name = challenge_data.cleaned_data['name']
                challenge.start_date = challenge_data.cleaned_data['start_date']
                challenge.end_date = challenge_data.cleaned_data['end_date']
                challenge.coordinator = challenge_data.cleaned_data['coordinator']
                challenge.description = challenge_data.cleaned_data['description']
                challenge.save()
                UserType.objects.filter(user__exact=challenge.coordinator).update(group='COORDI')
                return HttpResponseRedirect('/user/')
        challenges = Challenge.objects.all()
        response['challenges'] = challenges
        response['challenge_form'] = ChallengeForm()
    if ch == 'COORDI':
        challenges = Challenge.objects.filter(coordinator__exact=request.user)
        response['challenges'] = challenges
    return render(request, 'user.html', response)


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user/')
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            t = UserType(user=user, group='MEMBER')
            t.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = forms.UserCreationForm()
        return render(request, 'signup.html', {'form': form})
