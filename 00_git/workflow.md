# 저장소의 소유권이 있는 경우(feature branch workflow)

### 기존 push  message --     git push origin master

- branchname 에 있을때

## git push origin branchname

pull request로 쌓이고, master -병합완료 - 병합 완료된 브랜치 삭제

- master로 욺겨서 pull 받고, 기존 branch 지움

- 새로운 기능 추가 위해 또 다시 branch생성 및 과정 반복



```bash
# 다른 브랜치로 이동
$ git switch <다른 브랜치 이름>

# 브랜치를 새로 생성과 동시에 이동
$ git switch -c <브랜치 이름>
```

```bash
git push origin 브랜치 이름

- push한 사람이 open request열어서 write메세지 쓰고 create pull request
- repo 소유자한테 compare&merge뜸   pull request확인 / 문제없다면 mergerpull request, or close..
- 들어가보면 상태 확인가능 , files changed에  각 행 번호 앞에 + 눌러서 review쓸 수 있고, finish review. !
- conversation
- commitsuggestion 에서 바로 review받은거 commit 할 수 있음
```

```bash
git switch master
git pull origin master
git branch
git branch -d feature/login
```



# 저장소의 소유권이 없는 경우(fork & pull model)

- open source
- 원본-----fork----> 복제---clone----> User  (원본도 연결해야함)
- `git remote add upstream 원본url`  - branch에서 작업
- 기능 구현 후 복제본에 push하고, pull request를 원본에 보냄
- 원본에서 병합하면
- `git pull upstream master`
- 로컬 브랜치 삭제



```bash
git에서 fork버튼 클릭
- 복제한거 clone 받기
git remote -v
git remote add upstream [원본저장소주소 URL !!..]
git remote -v

git switch -c [branch name]
git push origin  [branchname]
- 내꺼에서 pull request만들고 원본 user에서 pull request가 뜸 !  -- 위와 동일

git switch master
git pull upstream master  # 원본에서 pull 받아야 함
```


