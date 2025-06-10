from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from bs4 import BeautifulSoup

def blog_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts, 'current_page': 'blog_list'})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    
    # Convert Markdown to HTML
    content_html = markdown.markdown(
        post.content,
        extensions=[
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables',
            CodeHiliteExtension(linenums=False),
            'markdown.extensions.toc',
        ]
    )
    
    # Add target="_blank" and rel="noopener noreferrer" to all links
    soup = BeautifulSoup(content_html, "html.parser")
    for a in soup.find_all("a"):
        a.attrs["target"] = "_blank"
        a.attrs["rel"] = "noopener noreferrer"
    
    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'content_html': str(soup),
        'current_page': 'blog_detail'
    })