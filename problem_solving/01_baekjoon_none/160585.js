//ctrl alt n

// ["OOO", "...", "XXX"]
// ["...", ".X.", "..."]
// ["...", "...", "..."]
function solution(board) {
  var answer = 1;
  var newBoard = [];
  for (let i = 0; i < 3; i++) {
    newBoard.push([...board[i]]);
  }

  let cntO = 0;
  let cntX = 0;
  newBoard.forEach((element) => {
    // console.log(element);
    element.forEach((element) => {
      if (element === "O") {
        cntO += 1;
      } else if (element === "X") {
        cntX += 1;
      }
    });
  });
  if (cntX > cntO) {
    answer = 0;
  }
  // else if (cntO > 0 && cntO === cntX) {
  //   answer = 0;
  // }
  if (answer === 1) {
    let start = "";
    let spaceCnt = 0;
    newBoard.forEach((element, idx) => {
      console.log(idx);
      element.forEach((element) => {
        if (element === "O") {
        }
      });
    });
  }
  return answer;
}

console.log(solution(["O.X", ".O.", "..X"]));
