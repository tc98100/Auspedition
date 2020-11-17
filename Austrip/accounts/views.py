from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from main.models import Attraction
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main/')
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

#
# @login_required(login_url='login_user')
# def like_post(request):
#     post = Attraction.objects.get(attraction_id=request.POST.get('attraction_id'))
#     attraction = get_object_or_404(Attraction,attraction_id=request.POST.get('attraction_id'))
#     post.likes+=20
#     post.save()

@ login_required
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()

        return JsonResponse({'result': result, })
