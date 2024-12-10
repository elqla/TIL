### 연결된 레포지토리 변경

```
git remote -v

git remote remove origin

git remote add  origin https~/

```

### 용량 찼을 경우

> 크기가 큰 파일을 여러개 올려두어 clone이 되지 않아 .git file안의 커밋로그에서 images/ 폴더를 찾아 지워주었다.

```
ERROR
GH001: Large files detected. You may want to try Git Large File Storage
```

```
ls
git filter-branch --tree-filter 'rm -rf images/' HEAD
git push origin -u master
```

https://dalibornasevic.com/posts/2-permanently-remove-files-and-folders-from-a-git-repository 



### git 잘못올렸을때

```
git rm --cached -r .idea/
```



