from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

def blog_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts, 'current_page': 'blog_list'})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    content_html = markdown.markdown(
    post.content,
    extensions=[
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',  # Adds support for Markdown tables
        CodeHiliteExtension(linenums=False),
        'markdown.extensions.toc',  # Generates a Table of Contents if needed
    ]
    )
    return render(request, 'blog/blog_detail.html', {'post': post, 'content_html': content_html, 'current_page': 'blog_detail'})
