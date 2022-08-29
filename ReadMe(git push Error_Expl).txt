

폴더 설명
  (1) static 디렉토리
      css나 js 파일, 그리고 이미지 파일이 위치한다

      정적 파일도 템플릿 파일처럼 정해진 위치가 있다
	  
	  
	  


.gitignore 파일은
git에 업로드 시에 무시할, 굳이 필요 없는 파일 목록을 설정한다	  





[ github이 있는 폴더 파일 삭제 ]
폴더 : unnecessary
comment : 불필요한폴더

파일 : unnecessary.xlsx
comment : 불필요한폴더

git rm --cached -r unnessesary
git rm --cached -r unnessesary.xlsx 

이렇게만 해서 원격저장소에 있는 폴더와 파일이 즉각 삭제되는 것은 아니고 commit을 해주고, push를 해줘야 합니다

git commit -m "불필요한폴더"
git push -u origin main(나의 경우 master)



push 오류 메세지

[rejected]        master -> master (fetch first)
이유 : push 할 때 기존 데이터가 유실될거 같아서 막음 것임

강제로 푸시하기

git push origin +master   여기서 +는 master 에 붙어 있어야 한다


