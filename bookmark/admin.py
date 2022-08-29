# 4 단계
# 뷰를 만들면서 확인하는 작업을 할 때 미리 입력된 데이터가 필요하기도 하다. 이 때 편리하다
 
from django.contrib import admin

# Register your models here.
from .models import Bookmark

admin.site.register(Bookmark)