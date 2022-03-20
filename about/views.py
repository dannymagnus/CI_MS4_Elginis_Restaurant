from django.shortcuts import render
from .models import About, Chef, Reason, Comment
from .forms import CommentForm
from django.views import generic


# Create your views here.

def about(request):
    about = About.objects.all()
    chefs = Chef.objects.all()
    reasons = Reason.objects.all()
    
    comments = Comment.objects.filter(approved=True).order_by("-created_on")
    
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.save()

    
    context = {
        'about': about,
        'chefs':chefs,
        'reasons': reasons,
        'comment_form':comment_form,
        'comments': comments,
        }
    return render(request, 'about.html', context)

