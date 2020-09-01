from django.urls import path
from trackerapp import views as v

urlpatterns = [
    path('', v.index, name='homepage'),
    path('login/', v.login_view, name='login_view'),
    path('logout/', v.logout_view, name='logout_view'),
    path('register/', v.register_view, name='register_view'),
    path('create/', v.create_ticket_view, name='create_ticket'),
    path('assign/<int:ticket_id>/', v.assign_ticket, name="assign_ticket"),
    path('complete/<int:ticket_id>/', v.complete_ticket, name="complete_ticket"),
    path('return/<int:ticket_id>/', v.return_ticket, name="return_ticket"),
    path('reopen/<int:ticket_id>/', v.reopen_ticket, name="reopen_ticket"),
    path('invalid/<int:ticket_id>/', v.invalid_ticket, name="invalid_ticket"),
    path('ticket/<int:ticket_id>/edit/', v.ticket_edit_view, name='edit_ticket'),
    path('ticket/<int:ticket_id>/', v.ticket_detail_view, name='ticket_detail'),
    path('user/<int:user_id>/', v.user_detail_view, name='user_detail'),
]
