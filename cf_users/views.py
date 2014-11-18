from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cf_users.models import CFUser
from django.core.validators import validate_email
from django import forms

def index(request):
  user_list = CFUser.objects.order_by('last_name')[:50]
  context = {'user_list': user_list}
  return render(request, 'cf_users/index.html', context)

def detail(request, user_id):
    user = get_object_or_404(CFUser, pk=user_id)
    context = {'user': user}
    return render(request, 'cf_users/detail.html', context)

def results(request):
    errors = []

    if request.method == "POST":
      try:
        validate_email(request.POST.get("email", ""))
      except forms.ValidationError:
        errors.append("invalid email")
      if not request.POST.get('first', ''):
        errors.append("no first name")
      if not request.POST.get('last', ''):
        errors.append("no last name")
      if errors:
        errors = ', '.join(errors)
        context = {'errors': errors}
        return render(request, 'cf_users/create_user.html', context)

    fname = request.POST['first']
    lname = request.POST['last']
    email = request.POST['email']
    q = CFUser(first_name = fname, last_name = lname, user_email = email)
    q.save()
    return HttpResponse(index(request))

def create_user(request):
    return render(request, 'cf_users/create_user.html')

def edit_user(request, user_id):
    user = get_object_or_404(CFUser, pk=user_id)
    context = {'user': user}
    return render(request, 'cf_users/edit_user.html', context)

def edit_results(request, user_id):
    user = get_object_or_404(CFUser, pk=user_id)
    user.first_name = request.POST['first']
    user.last_name = request.POST['last']
    user.user_email = request.POST['email']
    user.save()
    return HttpResponse(index(request))

def delete_user(request, user_id):
    user = get_object_or_404(CFUser, pk=user_id)
    user.delete()
    return HttpResponse(index(request))
