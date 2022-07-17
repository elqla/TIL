[TOC]

# [Redux with nomardcoders](https://nomadcoders.co/redux-for-beginners/lobby)

## createStore

```js
const reducer = () => {};
const store = createStore(reducer);
```

1. create store

   - store: data 저장

2. reducer

   - reducer: function, data modify

     

## Actions

`store를 수정하는 유일한 방법`

`second parameter, or argument`

[do not mutate]

```js
const friends = ['dal']
friends.push('lynn')   // do not mutate  // return new one
```

1. createStore로 store를 만듦
2. action 은 object `{type: "abc"}`
3. action에 message  넣어서 store에 dispatch 로 보냄
4. countmodifier가 reducer로, data를 수정함
5. action을 보내서, count modifier와 communication

```js
import { createStore } from "redux";

const countModifier = (count = 0, action) => {
  if (action.type==="ADD"){
      return count + 1;
  }else if(action.type==="MINUS"){
      return count - 1;
  }else{
    return count;
  }
};
const countStore = createStore(countModifier);
countStore.dispatch({type: "ADD"});
console.log(countStore.getState());
```



## Subscriptions 

```js
import { createStore } from "redux";

const add = document.querySelector('#add')
const minus = document.querySelector('#minus')
const number = document.querySelector('span')

number.innerText = 0;

const countModifier = (count = 0, action) => {
  if (action.type==="ADD"){
      return count + 1;
  }else if(action.type==="MINUS"){
      return count - 1;
  }else{
    return count;
  }
};


const countStore = createStore(countModifier);  //store 정의

const onChange = () =>{
  number.innerText = countStore.getState();   //store.getState();
}
countStore.subscribe(onChange);   //store내의 state가 변경되었을 때, 함수 실행 // `구독`

const handleAdd = ()=>{
  countStore.dispatch({type:"ADD"})
}
add.addEventListener("click", handleAdd)
minus.addEventListener("click", () => countStore.dispatch({type:"MINUS"}))

```



## Recap Refactor

- `action` 사용 시, `if-else` 사용하지 않음
- use `switch` (`action.type` with `case`)
- const로 문자를 정의하기
  - 이유: 오타를 쉽게 찾기 위해 (잘못쓰면  undefined)

 ```js
 const ADD = "ADD";
 const MINUS = "MINUS";
 
 const countModifier = (count = 0, action) => {
   switch(action.type){
     case ADD:
       return count + 1;
     case MINUS:
       return count -1;
     default:
       return count;
   }
 };
 ```





# PURE REDUX

```js
import { createStore } from "redux";
const form = document.querySelector("form");
const input = document.querySelector("input");
const ul = document.querySelector("ul");
const ADD_TODO = "ADD_TODO";
const DELETE_TODO = "DELETE_TODO";

const addToDo = text => {
  return {
    type: ADD_TODO,
    text
  };
};

const deleteToDo = id => {
  return {
    type: DELETE_TODO,
    id
  };
};

const reducer = (state = [], action) => {
  switch (action.type) {
    case ADD_TODO:
        const newToDoObj = { text: action.text, id: Date.now() };
        return [newToDoObj, ...state];
    case DELETE_TODO:
        // array새로 만들어주기 위해 filter 사용
        const cleaned = state.filter(toDo => toDo.id !== action.id);
        return cleaned;
    default:
      return state;
  }
};
const store = createStore(reducer);

store.subscribe(() => console.log(store.getState()));

const dispatchAddToDo = text => {
  store.dispatch(addToDo(text));
};

const dispatchDeleteToDo = e => {
    const id = parseInt(e.target.parentNode.id);   //HTML로부터 받아오는 id 변환
    store.dispatch(deleteToDo(id));
};

const paintToDos = () => {
  const toDos = store.getState();
  ul.innerHTML = "";
  toDos.forEach(toDo => {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.innerText = "DEL";
    btn.addEventListener("click", dispatchDeleteToDo);
    li.id = toDo.id;
    li.innerText = toDo.text;
    li.appendChild(btn);
    ul.appendChild(li);
  });
};

store.subscribe(paintToDos);

const onSubmit = e => {
  e.preventDefault();
  const toDo = input.value;
  input.value = "";
  dispatchAddToDo(toDo);
};

form.addEventListener("submit", onSubmit);
```





# REACT REDUX

## Provider

-  Provider 컴포넌트를 사용하여 리액트 앱에 store 연동하기

```js
//index.js
import { Provider } from 'react-redux'
import store from './store'


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <>
    <Provider store={store} >
        <App />
    </Provider>
    </>
);
```



## useSelector, useDispatch

- 기존: redux state로 부터 data가져오기  |  dispatch로 store 혹은 redux에 메시지 전달

  ```js
  store.getState();
  ```

- ~~connect 는 components를 store에 연결시켜줌~~ (기존)
  - state, dispatch 두개의 arguments를 가짐

---

- useSelector()

  - selector함수를 사용하여 Redux store state의 데이터를 가져올 수 있습니다.

    ```js
    //home.js
    import React, { useState } from 'react'
    import { useSelector, useDispatch } from 'react-redux/es/exports';
    import { actionCreators } from "../store"
    
    
    const Home = () => {  //store에 접근하기 때문에, 따로 props로 정보를 받지 않도록 한다.
      const [text, setText] = useState("");
      const toDos = useSelector(state => state);   //useSelector로 store에 접근한다.
      const dispatch = useDispatch();             //useDispatch로 store에 접근한다.
      function onChange(e){
        setText(e.target.value);
      };
      const onSubmit = (event) => {
        event.preventDefault();
        dispatch(actionCreators.addToDo(text));
        setText("");
      };
      return (
        <>
          <h1>Todo</h1>
          <form onSubmit={onSubmit}>
            <input type="text" value={text} onChange={onChange}/>
            <button>add</button>
            {/* <ul>{JSON.stringify(toDos)}</ul> */}
            <ul>{toDos.map(toDo=> <ToDo {...toDo}/>)}</ul>
            {/* prop으로 all todo 내려주기 */}
          </form>
        </>
      )
    }
    export default Home
    
    
    
    //store.js
    export const actionCreators = {
      addToDo,
      deleteToDo
    };
    export default store;
    ```

    

- {}를 통해 props로 파라미터를 넘겨준다. 

- payload: 파라미터 안의 객체

```js
//todos.js
import React from "react";
import { Provider } from "react-redux";
import { actionCreators } from "../store"
import { Link } from "react-router-dom";
import { useDispatch } from 'react-redux/es/exports';

const ToDo = ({text, id}) => {
    const dispatch = useDispatch();
    const onClick = () => {
        dispatch(actionCreators.deleteToDo(id));
    };
    return (
    <>
      <li>
      <Link to={`/${id}`}>{text}</Link>
      <button onClick={onClick}>DEL</button>
      </li>
    </>
  );
}

export default ToDo
```

```js
//detail.js
import React from 'react'
import { useParams } from 'react-router'
import { useSelector} from 'react-redux';

const Detail = () => {
  const toDos = useSelector((state)=>state);
  // const id = useParams();  `useParams();`를 통해 link로 넘어온 id 확인 가능 
  //클릭된 리스트의 아이디값을 가져옴
  const myId = useParams().id;
  //아이디 같은것을 찾아냄
  const toDo = toDos.find((toDo) => toDo.id === parseInt(myId));
  return (
    <>
    {toDo?.text}
    Created at: {toDo?.id}
    </>
  )
}

export default Detail
```



# Redux toolkit

## createAction("type")

```js
import { createStore } from "redux";
import { createAction } from "@reduxjs/toolkit";


const addToDo = createAction("ADD");  //createAction("type")
const deleteToDo = createAction("DELETE");

// console.log(addToDo())  GET(type and payload)

const reducer = (state = [], action) => {
  switch (action.type) {
    case addToDo.type:
      //action은 action.text가 없으므로, payload로 받는다.
      return [{ text: action.payload, id: Date.now() }, ...state];
    case deleteToDo.type:
      return state.filter(toDo => toDo.id !== action.payload);
    default:
      return state;
  }
};
  
const store = createStore(reducer);
export const actionCreators = {
  addToDo,
  deleteToDo
};
export default store;
```



## createReducer

we dont need switch-case, mutate new-state anymore

1. mutate state    with  push 
2. return new state 

```js
import { createStore } from "redux";
import { createReducer, createAction } from "@reduxjs/toolkit";


const addToDo = createAction("ADD");  //createAction("type")
const deleteToDo = createAction("DELETE");

// console.log(addToDo())  GET(type and payload)

// const reducer = (state = [], action) => {
//   switch (action.type) {
//     case addToDo.type:
//       //action은 action.text가 없으므로, payload로 받는다.
//       return [{ text: action.payload, id: Date.now() }, ...state];
//     case deleteToDo.type:
//       return state.filter(toDo => toDo.id !== action.payload);
//     default:
//       return state;
//   }
// };
  

//state를 mutate하기 쉽게 해줌
const reducer = createReducer([], {
  //[action]: (state, action) => {}

  [addToDo]: (state, action) => {
    //mutate sate
    //새로운 state를 만드는 대신, push 하는 방식을 사용한다.
    state.push({ text: action.payload, id: Date.now() })
  },

  [deleteToDo]: (state, action) =>
   //return new state
   //filter return new array
    state.filter(toDo => toDo.id !== action.payload)
})

const store = createStore(reducer);
export const actionCreators = {
  addToDo,
  deleteToDo
};
export default store;
```



## configureStore

[redux deveploper tool chrome extension](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?hl=ko)
toolkit을 사용하지 않아도 쓸 수 있음

createStore(reducer) 대신 configureStore({reducer})로 크롬 확장자를 사용할 수 있다. 

```js
import { configureStore } from '@reduxjs/toolkit'
// import rootReducer from './reducers'
// const store = createStore(reducer);
const store = configureStore({ reducer })
//const store = configureStore({ reducer: rootReducer })
```



## createSlice



```js
//store.js

import {createSlice } from "@reduxjs/toolkit";
import { configureStore } from '@reduxjs/toolkit'


const toDos = createSlice({
  name:'toDosReducer',
  initialState:[],
  reducers:{
    add: (state, action) => {
      state.push({ text: action.payload, id: Date.now() })
    },
    remove: (state, action) =>
      state.filter(toDo => toDo.id !== action.payload)
    }
});


//todos의 reducer를 export해서 store의 reducer를 재설정한다.
/////////////위의 slice로 부터 reducer를 받는다.///////////////////////
const store = configureStore({ reducer:toDos.reducer })

// console.log(toDos.actions);
// action으로 제공
export const { add, remove } = toDos.actions

export default store;
```

```js
//edit Todo.js and Home.js
import { remove } from "../store"

const ToDo = ({text, id}) => {
    const dispatch = useDispatch();
    const onClick = () => {
        dispatch(remove(id));
    };

export default ToDo
```

[참고]

```js
2개 이상의 reducer를 사용해야 하는 경우
const allReducer = combineReducers({
//여기에 관리할 리듀서 다 써주면 됨
//ex)
//user,
//textlist
})
const store = configureStore({reducer: allReducer});

그리고 데이터가 배열인 경우에는 map으로 꺼낼 때 useSelector로 꺼내온 데이터를 변수로 지정하고 
콘솔찍어보면 combineReducers에서 적어놓은 리듀서 이름으로 배열이 만들어져 있음.
const data = useSelector(state => state)로 빼왔으면
data.리듀서이름.map 으로 꺼내기
```

