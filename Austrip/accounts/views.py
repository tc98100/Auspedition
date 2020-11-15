from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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

# @login_required
def aLike(request):
    print("lol");
    if request.POST.get('action')=="post":
        print("lol");
        result = ''
        id = int(request.POST.get('attraction_id'))
        attraction = get_object_or_404(Attraction, id=id)
        attraction.userLike.remove(request.user)
        attraction.likes -= 1
        result = attraction.likes
        attraction.save()
        # if attraction.userLike.filter(id=request.user.user_id).exists():
        #     attraction.userLike.remove(request.user)
        #     attraction.likes-=1
        #     result=attraction.likes
        #     attraction.save()
        # else:
        #     attraction.userLike.add(request.user)
        #     attraction.likes+=1
        #     result = attraction.likes
        #     attraction.save()

        return JsonRespnse({'result':result,})
