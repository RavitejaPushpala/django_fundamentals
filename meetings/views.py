from django.shortcuts import redirect, render, get_object_or_404
from django.forms import modelform_factory

from meetings.models import Meeting, Room

# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, template_name="meetings/details.html", context={"meeting": meeting})

def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, template_name="meetings/rooms_list.html", context={"rooms": rooms})

MeetingForm = modelform_factory(Meeting, exclude=[])
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, template_name="meetings/new.html", context={"form": form})

def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, template_name="meetings/edit.html", context={"form": form})

def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("welcome")
    else:
        return render(request, template_name="meetings/confirm_delete.html", context={"meeting": meeting})