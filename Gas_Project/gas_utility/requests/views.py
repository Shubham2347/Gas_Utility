from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  # Assign the logged-in user
            service_request.save()
            return redirect('view_request', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'requests/create_request.html', {'form': form})

@login_required
def view_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'requests/view_request.html', {'service_request': service_request})

@login_required
def track_request(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'requests/track_request.html', {'service_requests': service_requests})
