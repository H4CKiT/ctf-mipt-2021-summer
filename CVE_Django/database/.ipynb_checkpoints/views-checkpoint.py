from django.shortcuts import render
from .forms import UserForm
from database.models import Questions

def index(request):
    latest_question_list = Questions.objects.order_by('question_text')
    if request.method == 'POST':
        name = request.POST.get("order").strip()
        if name:
            latest_question_list = latest_question_list.order_by(name)
    userform = UserForm()
    latest_question_list = latest_question_list[:5]
    data = {
        "latest_question_list": latest_question_list,
        "form": userform
    }
    return render(request, "some_index.html", context=data)