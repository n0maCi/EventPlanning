from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, DetailView
from web.forms import *
from .models import Events


@login_required
def profile_view(request):
    if request.POST:
        if 'add' in request.POST:
            check_title = request.POST.get('title_events')
            find_event = UserHasEvent.objects.filter(title_events=check_title) & UserHasEvent.objects.filter(web_buyer_id=request.user.id)
            print(find_event)
            try:
                print(find_event[0])
            except:
                print("err")
                if request.method == "POST":
                    form = NewEvent(request.POST)
                    if form.is_valid():
                        obj = form.save(commit=False)
                        obj.web_buyer_id = request.user.id
                        obj.save()
                        form.save_m2m()
        elif 'delete' in request.POST:
            if request.method == 'POST':
                data = request.POST.get('title_events')
                edit_db = Events.objects.all().filter(title=data).values_list("id") & Events.objects.filter(web_buyer_id=request.user.id).values_list("id")
                id_input = UserHasEvent.objects.filter(title_events=data).values_list("id") & UserHasEvent.objects.filter(web_buyer_id=request.user.id).values_list("id")
                print(id_input)
                try:
                    UserHasEvent.objects.filter(id=id_input[0][0]).delete()
                    for list in edit_db:
                        Events.objects.filter(id=list[0]).delete()
                except IndexError:
                    print('лошара')



    events1 = UserHasEvent.objects.all().filter(web_buyer_id=request.user.id)
    return render(request, 'web/profile.html', {'events1': events1})

@login_required
def add_event_view(request, title = None, name = None, id_title = None, username = None):
    get_id_user = Buyer.objects.all().filter(username=username).values_list("id")[0][0]
    print(get_id_user)
    owner_id = UserHasEvent.objects.all().filter(title_events=title).values_list("web_buyer_id")[0][0]
    guest_id = request.user.id
    print(owner_id)
    print(guest_id)
    if get_id_user != guest_id:
        return HttpResponseBadRequest("Error 404")

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("err")

    print(id_title)
    edit_db = Events.objects.filter(title=title) & Events.objects.filter(name=name)
    edit_db.values_list("id")
    try:
        print(edit_db.values_list("id")[0][0])
        Events.objects.filter(id=id_title).delete()
    except IndexError:
        print('Лох')

    records = Events.objects.all().filter(web_buyer_id=request.user.id).order_by('start_at') & Events.objects.all().filter(title=title).order_by('start_at')
    print(records)
    return render(request, 'web/add.html', {'records': records, 'title': title})


def event_view(request, title, username=None):
    get_id_user = Buyer.objects.all().filter(username=username).values_list("id")[0][0]
    records = Events.objects.all().filter(title=title).order_by('start_at') & Events.objects.all().filter(web_buyer_id=get_id_user).order_by('start_at')
    return render(request, 'web/event.html', {'records': records, 'title': title})

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("web:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)