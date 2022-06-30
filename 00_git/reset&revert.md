## git reset

**명령어**

```bash
$ git reset [옵션] <커밋 ID>
```

- **시계를 마치 과거로 돌리는 듯한 행위**로써, 특정 커밋 상태로 되돌아갑니다.
- 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓아 놨던 커밋들은 전부 사라집니다.

```
a b c d
d에서 a로 가려고 하면
a로 감
b, c 커밋 XX -> option 제공
```

**옵션**

- `옵션`은 아래와 같이 세 종류가 있으며, 생략 시 `--mixed`가 기본 값입니다.

```bash
$ git log --oneline
# 복사
$ git reset --soft 커밋id   # 커밋전, 애드된 상태로 만듦
$ git reset --mixed 커밋id  # unstage 상태로 바꿈(add 전 / working directory로 돌려놓음)
$ git reset --hard 커밋id   # tracked된 파일들 working directory에서 삭제
```

```bash
$ git reflog
# 커밋 id 복사
$ git reset --hard 복구_커밋id
```

---



## git revert

- ~~reset은 커밋내역이 사라지므로, 협업시 권장되지 않음~~
- revert는 특정 사건을 없었던 일로 만듦
- 이전 커밋을 유지하고, 취소했다는 커밋을 생성함
- `history가 남는다.`

```bash
$ git log --oneline
$ git revert 1eb059
```

```bash
a b c d
d 에서 a로 갈때
b로 감  # b가 없었던 과거로 돌림 (revert b)
a c d가 남음
```



> **[중요]**
>
> `git reset`과 비슷하다는 이유로 다음 사항이 혼동될 수 있습니다. 
>
> - `git reset --hard 5sd2f42`라고 작성하면 5sd2f42라는 커밋`으로` 돌아간다는 뜻입니다.
>
> - `git revert 5sd2f42`라고 작성하면 5sd2f42라는 커밋`을` 되돌린다는 뜻입니다.



> **[참고사항]**
>
> ```bash
> # 공백을 통해 여러 커밋을 한꺼번에 되돌리기 가능
> $ git revert 7f6c24c 006dc87 3551584
> 
> # 범위 지정을 통해 여러 커밋을 한꺼번에 되돌리기 가능
> $ git revert 3551584..7f6c24c
> 
> # 커밋 메시지 작성을 위한 편집기를 열지 않음 (자동으로 커밋 완료)
> $ git revert --no-edit 7f6c24c
> 
> # 자동으로 커밋하지 않고, Staging Area에만 올림 (이후, git commit으로 수동 커밋)
> # 이 옵션은 여러 커밋을 revert 할 때 하나의 커밋으로 묶는게 가능
> $ git revert --no-commit 7f6c24c
> ```

