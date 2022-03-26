# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

# Internal:
from .models import About, Chef, Reason, Comment
from .forms import CommentForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def about(request):
    """
    A view to show restaurant bio,
    reasons to dine, chef images and bio,
    and comments
    Args:
        request (object): HTTP request object and or form object.
    Returns:
        Render of items page with context
    """
    about = About.objects.all()
    chefs = Chef.objects.all()
    reasons = Reason.objects.all()
    comments = Comment.objects.filter(
        approved=True
        ).order_by(
            "-created_on"
        )
    comment_form = CommentForm()
    commented = False
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.save()
            commented = True
        else:
            comment_form = CommentForm()
    context = {
        'about': about,
        'chefs': chefs,
        'reasons': reasons,
        'comment_form': comment_form,
        'comments': comments,
        'commented': commented,
        }
    return render(request, 'about.html', context)


def delete_item(request, comment_id):
    """
    A view delete comments
    Args:
        request (object): HTTP request object.
        comment_id: the unique numeric identifier of the comment to be deleted
    Returns:
        Redirect to about page with comment removed
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('/about/')
    context = {'comment': comment}
    return render(request, 'delete_comment.html', context)
