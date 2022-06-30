[TOC]

[git site](https://git-scm.com/book/ko/v2)

[commit message](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)

[udacity commit style](http://udacity.github.io/git-styleguide/)



### **git 설정**

```bash
git config --list  :전체 config list 보기

# 전역 설정
git config --global user.name 'dabeen'  :이름설정
git config --global user.email 'elqla19@gmail.com'   :이메일설정

# 전역 설정된 name과 email 삭제
git config --unset --global user.name 
git config --unset --global user.email

# 전역 설정된 name과 email 확인
git config user.name 
git config user.email 
```

### **폴더 및 파일 생성**

```bash
mkdir 폴더명

cd 폴더명

touch a.txt

start a.txt

.gitignore파일 작성 시, 안올릴 파일명 적기
```

### **git 연결**

```bash
git init 

git remote add origin [레포지토리주소]

git remote -v   : 연결 확인

**또는**

git clone http ~

# git 지우기
rm -rf .git
```

### git log : 현재 commit 상태 파악

```bash
git log

git log —oneline
```

### **status**

```bash
git status   : 현재 add/commit 상태 파악
git show commitID   : 특정 커밋 확인

git diff 이전커밋ID  이후커밋ID  :commit 이력간의 차이를 출력
```

### **commit**

```bash
git commit -m ‘first_commit’

git commit -am ‘add_commit’

# 마지막 커밋이후 수정한게 없을때, 커밋 재정의
git commit --amend 
i - insert
title 작성
content 작성가능
esc
:wq
# 변경사항이 있을때 이전 커밋 덮어쓰기
# 기존에 a.txt가 commit 까지 되어있는 상황
touch b.txt
git add b.txt
git status

git commit --amend   ### 다만 커밋 자체가 재정의 되는 것이기에, 이전 커밋만을 볼 순 없게됨
```

### **add**

```bash
git add [파일명]

git add 폴더이름/

git add .    : 한번에 올리기 

git remote add origin http~  (이 repository로 파일 보내기. origin은 별명)

git remote -v                          (내가 연결한 링크 나오는지 확인)

git push -u origin master 

git push origin master
```

### **pull**

```bash
git pull 원격저장소 가져올 브랜치명  // git 서버에서 최신 코드 받아와서 merge
git pull origin master
```

### **unstaged**

```bash
git rm --cached [test.md] (add 취소 => 기존에 커밋이 안되있을경우)
```

### **file remove**

```bash
# 로컬 + 깃
git rm HelloWorld.java
git commit -m "Delete HelloWorld.java"

# 로컬유지 / 깃에서만 삭제
git rm --cached HelloJAVA.class
git commit -m "Delete HelloJAVA.class"
```

### **restore**

```bash
# 워킹트리 파일 복원
git restore <파일명>   # modified 파일을 수정 전으로 되돌림 (복구 불가) # add전의

# git add로 stage에 들어갔을때, unstaged하는법(add취소)  # 기존엔 git reset HEAD <파일명> 이였음
git restore --staged <파일명>    //git에 올라가있어도 그냥 add만 취소 시킬때
```

### **branch**

```bash
# 브랜치 상태 확인
git branch
git log --branches --graph

# 원격 branch 목록 조회
git branch
# 다른 브랜치로 이동
git switch <다른 브랜치 이름>

# 브랜치를 새로 생성과 동시에 이동
git switch -c <브랜치 이름>

# 브랜치 특정 커밋에서 만들어 이동
git switch -c <브랜치 이름> <커밋>

# 브랜치 삭제
git branch -d <브랜치 이름>     //병합된게 삭제되는거
git branch -D <브랜치 이름>     //강제삭제

# 브랜치명 변경
git branch -m master mymaster

# 브랜치 상태 확인
git branch --merged     //병합된 브랜치 확인
git branch --no-merged  //병합안된 브랜치 확인
```

### **merge (브랜치 합치기)**

```bash
git merge "가져올 브랜치명"    병합 이력이 남는다, rebase는 안남음

git merge branch_name // brance_name을 해당 브랜치에 병합
git merge --option branch_name

--ff    merge commit이 남지 않음, 병합할 브랜치의 커밋을 따라감
--no-ff **  merge commit이 남음, 병합할 브랜치와 합쳐짐 / default

#merge 취소 
git merge --abort
```

### **reset/revert**

- reset 권장x
- 쉽게 과거로 돌아갈 수 있지만, 커밋 내역이 사라진다.
- 협업시 commit 개수가 바뀌게 된다면 무조건 conflict가 남.

```bash
git log --oneline
# commit id 복사

# 커밋 전 상태(add)
git reset --soft [커밋id]   # add/ 커밋전, 애드된 상태로 만듦

# add 전 상태(working directory)
git reset --mixed [커밋id]  # unstaged 상태로 바꿈(add 전 / working directory로 돌려놓음) / 변경 이력은 모두 삭제하지만 변경 내용은 남아있음

# 돌아가고자하는 커밋으로 되돌아감
git reset --hard [커밋id]   # 기존커밋/ 커밋 이후의 변경 이력은 모두 삭제합니다.

# git reflog 로 복구
git reflog

git reset --hard [복구커밋id]
```

- revert  커밋삭제X  커밋 추가 O
- 즉, 과거로 돌아가는게 아니라 과거로 돌아간 상태(새커밋)를 만들면서 이동

```bash
git log --oneline
git revert 1eb059

# 1 2 3 중에 2번으로 돌아간다는건, 2번을 없었던 일로 만들고 싶다는 뜻
# 1 3 만 남음

a b c d
d 에서 a로 갈때
b로 감  # b가 없었던 과거로 돌림 (revert b)
a c d가 남음
# a b c d 에서 c로 가고 싶다면, d의 commit id를 사용해야 함
# a b c d 에서 a로 가고 싶으면 d c b 순으로 되돌리며 돌아가야 함
# 공백을 통해 여러 커밋을 한꺼번에 되돌리기 가능
# 1 2 3 중 1로 가고 싶을때, revert 2 3
$ git revert 7f6c24c 006dc87 3551584

# 범위 지정을 통해 여러 커밋을 한꺼번에 되돌리기 가능
$ git revert 3551584..7f6c24c

# 커밋 메시지 작성을 위한 편집기를 열지 않음 (자동으로 커밋 완료)
$ git revert --no-edit 7f6c24c

# 자동으로 커밋하지 않고, Staging Area에만 올림 (이후, git commit으로 수동 커밋)
# 이 옵션은 여러 커밋을 revert 할 때 하나의 커밋으로 묶는게 가능
$ git revert --no-commit 7f6c24c
```

### **git stash**

파일 변경 내역을 일시적으로 기록해 둔다.

```bash
# modified, staged 변경 내용 임시 저장
git stash

# stashed 조회
git stash list

# stash 내역 working directory로 추가
git stash pop

# stash file 제거
git stash drop
```

### git cherry-pick

다른 브랜치에 있는 커밋을 선택하여 내 브랜치에 적용시킨다.

```bash
# git cherry-pick [커밋 ID]

git cherry-pick weewr23
git cherry-pick 14sdf2d

# 

git cherry-pick weewr23 14sdf2d

# 연속적인 커밋일 경우
git cherry-pick weewr23..14sdf2d
```

### bash에서 기능 편하게 쓰기

```bash
code ~/.bashrc
---vscode---
alias jp="jupyter notebook"
alias sqlite3="winpty sqlite3"
alias run="python manage.py runserver"  # 띄어쓰기 주의
---ctrl_s---
source ~/.bashrc
```

