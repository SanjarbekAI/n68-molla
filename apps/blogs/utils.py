from datetime import timedelta

from django.utils import timezone

from apps.blogs.models import BlogViewModel


def check_blog_view(request, blog):
    # Get user IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        user_ip = x_forwarded_for.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')

    # Find last view of this blog by this IP
    last_view = BlogViewModel.objects.filter(
        user_ip=user_ip, blog=blog
    ).order_by('-created_at').first()

    # If never viewed OR last view was more than 7 days ago → create new record
    if not last_view or (timezone.now() - last_view.created_at) > timedelta(minutes=1):
        BlogViewModel.objects.create(user_ip=user_ip, blog=blog)
