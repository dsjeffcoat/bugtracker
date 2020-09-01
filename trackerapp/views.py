from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from myusers.models import CustomUser
from myusers.forms import SignupForm, LoginForm
from .models import BugTicket, UserProfile
from .forms import CreateTicket
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

@login_required
def index(request):
    # all_tickets = BugTicket.objects.all()
    new_tickets = BugTicket.objects.filter(
        status='New')
    progress_tickets = BugTicket.objects.filter(
        status='In Progress')
    completed_tickets = BugTicket.objects.filter(
        status='Done')
    invalid_tickets = BugTicket.objects.filter(
        status='Invalid')
    return render(request, 'index.html', {'new': new_tickets, 'progress': progress_tickets, 'completed': completed_tickets, 'invalid': invalid_tickets})


@login_required
def user_detail_view(request, user_id):
    my_user = CustomUser.objects.filter(id=user_id).first()
    user_tickets_submitted = BugTicket.objects.filter(submitted_by=user_id)
    user_tickets_assigned = BugTicket.objects.filter(assigned_to=user_id)
    user_tickets_completed = BugTicket.objects.filter(completed_by=user_id)
    return render(request, 'user_detail.html', {'user': my_user, 'submitted': user_tickets_submitted, 'assigned': user_tickets_assigned, 'finished': user_tickets_completed})


@login_required
def ticket_detail_view(request, ticket_id):
    ticket = BugTicket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail.html', {'ticket': ticket})


@login_required
@staff_member_required
def register_view(request):
    try:
        profile = request.user.username
    except CustomUser.DoesNotExist:
        profile = CustomUser(username=request.user)

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(username=data.get(
                'username'), password=data.get('password'))
            account = form.save(commit=False)
            account.user = new_user
            account.save()
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'register_form.html', {'form': form})


@login_required
def create_ticket_view(request):
    if request.method == 'POST':
        form = CreateTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BugTicket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                submitted_by=request.user,
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = CreateTicket()
    return render(request, 'create_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                'username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'login_page.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

# Editing Views


@login_required
def ticket_edit_view(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = CreateTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
        return HttpResponseRedirect(reverse('ticket_detail', args=[ticket.id]))

    data = {
        'title': ticket.title,
        'description': ticket.description
    }
    form = CreateTicket(initial=data)
    return render(request, 'edit_ticket.html', {'form': form})


@login_required
def assign_ticket(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    ticket.status = 'In Progress'
    ticket.assigned_to = request.user
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[ticket.id]))


@login_required
def complete_ticket(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    ticket.status = 'Done'
    ticket.assigned_to = None
    ticket.completed_by = request.user
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[ticket.id]))


@login_required
def return_ticket(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    ticket.status = 'New'
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[ticket.id]))


@login_required
def reopen_ticket(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    ticket.status = 'In Progress'
    ticket.assigned_to = request.user
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[ticket.id]))


@login_required
def invalid_ticket(request, ticket_id):
    ticket = BugTicket.objects.get(id=ticket_id)
    ticket.status = 'Invalid'
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[ticket.id]))
