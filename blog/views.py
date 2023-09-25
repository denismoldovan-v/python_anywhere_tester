from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request):
	blog_count = Blog.objects.count()
	blog_content = Blog.objects.order_by('-date')
	return render(request, 'blog/blog.html', {'blog_cs' : blog_content, 'count' : blog_count})

def detail(request, blog_id):
	
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html', {'blog' : blog})
