from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from licenses.models import License

@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                            ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    licenses = profile.licenses.all()

    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'licenses': licenses,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html' , context)
