from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Post, Category

# Create your views here.
def list_of_post_by_category(request, category_slug):
	categories = Category.objects.all()
	post = Post.objects.filter(status='published')
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		post = post.filter(category=category)
	template = 'blog/categories.html'
	context = {'categories': categories, 'post': post, 'category': category}
	return render(request, 'blog/categories.html', {'categories': categories, 'post': post, 'category': category})

def list_of_post(request):
	post = Post.objects.filter(status='published')
	template = 'blog/home.html'
	context = {'post': post}
	return render(request, template, context)

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	template = 'blog/blog.html'
	context = {'post': post}
	return render(request, template, context)

def add_comment(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('blog:post_detail', slug=post.slug)
	else:
		form = CommentForm()
	template = 'blog/add_comment.html'
	context = {'form': form}
	return render(request, template, context)

def december_2017(request):
	template = 'blog/december_2017.html'
	post = Post.objects.filter(status='published')
	context = {'post': post}
	return render(request, template, context)

def about(request):
	template = 'blog/about.html'
	return render(request, template)