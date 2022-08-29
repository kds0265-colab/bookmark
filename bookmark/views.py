from django.shortcuts import render
from django.http import HttpResponse
# client 단에 어떻게 보여줄 것인가? 를 구현한다
# DB Table 내용을 어떻게 보여줄 것인가? 를 구현한다

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from django.urls import reverse

from .models import Bookmark


# 함수 형
def hello(request):
    return HttpResponse("hello, world. You're at the polls index.") 


# 클래스 형
class BookmarkListView(ListView):    # DB 테이블을 가져다가 Front에서 List 형태로 보여준다
    model = Bookmark                 # 모델 설정하기
    # 템플릿 이름은 "모델이름_list.html" 을 기본으로해서 내부적으로 설정된 거을 사용하면 된다다. 
    # 아님, 아래와 같이 사용자가 임의로 정해서 (bookmark_list2) 연결해 주면 된다. 
    template_name = 'bookmark/bookmark_list.html'    # 이거가 없어도 작동, why?
    paginate_by = 6     # 한 페이지에 보이는 데이터 row 를 정한다 
    
    
class BookmarkCreateView(CreateView):
    model = Bookmark                       # 어떤 모델(DB Table)의 입력을 받을 것인지 정하고
    fields = ['site_name','url']           # 그 테이블에서 어떤 fields 들을 입력받을 것인지 정하고
    success_url = reverse_lazy('list')     # 글ㅋ쓰기를 완료하고 이동할 페이질 정하고
    #template_name_suffix = '_create'       # 사용할 템플릿을 정하고 
    template_name = 'bookmark/bookmark_create.html'   # 템플릿 이름을 바로 지정한다
    

    
class BookmarkDetailView(DetailView):
    model = Bookmark 
    template_name = 'bookmark/bookmark_detail.html'
    
    
    
# default로   get_absolute_url을 설정해 두었다 (models.py 에서)  
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url'] 
    #success_url = reverse_lazy('list')
    template_name = 'bookmark/bookmark_update.html'
    
    
    
class BookmarkDeleteView(DeleteView):    
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name = 'bookmark/bookmark_confirm_delete.html'
    
    
    