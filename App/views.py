from django.shortcuts import render
from .models import Chat, Group
# Create your views here.
def index(request,group_name):
    group = Group.objects.filter(name=group_name).first()
    print("Group ....",group_name)
    chats = []
    if group:
        chats = Group.objects.filter(name = group_name)
    else:
        group = Group.objects.create(name = group_name)
        group.save()
    return render(request , 'Index.html',
                      {'groupname':group_name,
                       'chats':chats})