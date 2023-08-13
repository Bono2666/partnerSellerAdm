from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from apps.forms import *
from apps.models import *


@login_required(login_url='/login/')
def home(request):
    context = {
        'segment': 'index',
    }
    return render(request, 'home/index.html', context)


@login_required(login_url='/login/')
def hero_index(request):
    hero = Hero.objects.all()
    context = {
        'hero': hero,
        'segment': 'hero',
        'crud': 'index',
    }
    return render(request, 'home/hero_index.html', context)


@login_required(login_url='/login/')
def hero_add(request):
    if request.POST:
        form = FormHero(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hero-index'))
        else:
            context = {
                'form': form,
                'crud': 'add',
            }
            return render(request, 'home/hero_add.html', context)
    else:
        form = FormHero()
        context = {
            'form': form,
            'crud': 'add',
        }
        return render(request, 'home/hero_add.html', context)


# Update Hero
@login_required(login_url='/login/')
def hero_update(request, _id):
    hero = Hero.objects.get(id=_id)
    if request.POST:
        form = FormHero(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hero-index'))
    else:
        form = FormHero(instance=hero)
        context = {
            'form': form,
            'data': hero,
            'crud': 'update',
        }
        return render(request, 'home/hero_update.html', context)


# Delete Hero
@login_required(login_url='/login/')
def hero_delete(request, _id):
    hero = Hero.objects.get(id=_id)
    hero.delete()
    return HttpResponseRedirect(reverse('hero-index'))


@login_required(login_url='/login/')
def member_index(request):
    member = Members.objects.all()
    context = {
        'members': member,
        'segment': 'member',
        'crud': 'index',
    }
    return render(request, 'home/member_index.html', context)


@login_required(login_url='/login/')
def member_add(request):
    if request.POST:
        form = FormMember(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member-index'))
        else:
            error = form.errors
            context = {
                'form': form,
                'message': error,
            }
            return render(request, 'home/member_add.html', context)
    else:
        form = FormMember()
        context = {
            'form': form,
            'crud': 'add',
            'segment': 'member',
        }
        return render(request, 'home/member_add.html', context)


# Update Member
@login_required(login_url='/login/')
def member_update(request, _id):
    member = Members.objects.get(id=_id)
    if request.POST:
        form = FormMember(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member-index'))
    else:
        form = FormMember(instance=member)
        context = {
            'form': form,
            'data': member,
            'segment': 'member',
            'crud': 'update',
        }
        return render(request, 'home/member_view.html', context)


# Delete Member
@login_required(login_url='/login/')
def member_delete(request, _id):
    member = Members.objects.get(id=_id)
    member.delete()
    return HttpResponseRedirect(reverse('member-index'))


@login_required(login_url='/login/')
def icon(request):
    return render(request, 'home/icons.html')


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'home/profile.html')


@login_required(login_url='/login/')
def table(request):
    return render(request, 'home/tables.html')
