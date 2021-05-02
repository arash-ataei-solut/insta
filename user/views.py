from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from user.forms import RegistrationForm
from user.models import Profile


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class Login(LoginView):
    success_url = reverse_lazy('user-list')


class UserListView(ListView):
    template_name = 'user_list.html'

    def get_queryset(self):
        queryset = Profile.objects.all()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(user__username__icontains=q)
        return queryset


class ProfileView(DetailView):
    template_name = 'profile.html'
    model = Profile


class FollowView(LoginRequiredMixin, View):

    def get(self, request, pk):
        if pk != request.user.pk:
            user = request.user
            profile = user.profile
            user_follow = get_object_or_404(Profile, pk=pk)
            profile.following.add(user_follow)
        return HttpResponseRedirect(reverse('profile', kwargs={'pk': pk}))


class UnfollowView(LoginRequiredMixin, View):

    def get(self, request, pk):
        if pk != request.user.pk:
            user = request.user
            profile = user.profile
            user_follow = get_object_or_404(Profile, pk=pk)
            profile.following.remove(user_follow)
        return HttpResponseRedirect(reverse('profile', kwargs={'pk': pk}))


class FollowingListView(LoginRequiredMixin, ListView):
    template_name = 'following.html'

    def get_queryset(self):
        return self.request.user.profile.following.all()


class FollowerListView(LoginRequiredMixin, ListView):
    template_name = 'follower.html'

    def get_queryset(self):
        return self.request.user.profile.follower.all()
