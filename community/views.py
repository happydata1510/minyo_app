from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    """게시글 목록 페이지"""
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 10)  # 페이지당 10개 게시글
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'posts': posts,
    }
    return render(request, 'community/list.html', context)

def post_detail(request, post_id):
    """게시글 상세 페이지"""
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'community/detail.html', context)

@login_required
def post_create(request):
    """게시글 작성 페이지"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '게시글이 작성되었습니다.')
            return redirect('community:detail', post_id=post.id)
    else:
        form = PostForm()
    
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)

@login_required
def post_edit(request, post_id):
    """게시글 수정 페이지"""
    post = get_object_or_404(Post, id=post_id)
    
    # 작성자만 수정 가능
    if post.author != request.user:
        messages.error(request, '게시글을 수정할 권한이 없습니다.')
        return redirect('community:detail', post_id=post.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '게시글이 수정되었습니다.')
            return redirect('community:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'community/edit.html', context)

@login_required
def post_delete(request, post_id):
    """게시글 삭제"""
    post = get_object_or_404(Post, id=post_id)
    
    # 작성자만 삭제 가능
    if post.author != request.user:
        messages.error(request, '게시글을 삭제할 권한이 없습니다.')
        return redirect('community:detail', post_id=post.id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('community:list')
    
    return redirect('community:detail', post_id=post.id)

@login_required
def add_comment(request, post_id):
    """댓글 추가"""
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, '댓글이 작성되었습니다.')
    
    return redirect('community:detail', post_id=post.id)

@login_required
def delete_comment(request, comment_id):
    """댓글 삭제"""
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    
    # 작성자만 삭제 가능
    if comment.author != request.user:
        messages.error(request, '댓글을 삭제할 권한이 없습니다.')
        return redirect('community:detail', post_id=post_id)
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, '댓글이 삭제되었습니다.')
    
    return redirect('community:detail', post_id=post_id)
