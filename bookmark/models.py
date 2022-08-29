# 1 단계
#모델은 데이터베이스 사용을 쉽게하기 위해 사용하는 도구
#App을 시작했으면 제일 처음으로 DB에 테이블을 만드다. 
 
from django.db import models
from django.urls import reverse



class Bookmark(models.Model):
    site_name = models.CharField(max_length=100) 
    url = models.URLField('Site URL')
    
    def __str__(self):
        #객체를 출력할 때 나타낼 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url
        
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
