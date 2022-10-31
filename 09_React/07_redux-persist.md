# redux - persist

리덕스의 Store는 앱을 종료하면 저장되어 있던 모든 상태가 없어진다.

이에 redux-persist를 이용해 로컬 스토리지에 저장한다.

https://edvins.io/how-to-use-redux-persist-with-redux-toolkit

https://yarnpkg.com/package/redux-persist

[counter로 연습하기](https://medium.com/humanscape-tech/redux-persist-알아보기-2077c9e566d9)

# install

```bash
npm install redux-persist
# localStorage에 저장
import storage from 'redux-persist/lib/storage'
# session Storage에 저장
import storageSession from 'redux-persist/lib/storage/session
```





- src/app/store.js

```js
import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';

//s
import storage from 'redux-persist/lib/storage';
import { combineReducers } from 'redux';
import { persistReducer } from 'redux-persist';
import thunk from 'redux-thunk';
//e

//s
const reducers = combineReducers({
  counter: counterReducer,
});

const persistConfig = {
  key: 'root',
  storage,
};

const persistedReducer = persistReducer(persistConfig, reducers);


//export default configureStore({
//  reducer: {
//    counter: counterReducer,
//  },
//});

const store = configureStore({
  reducer: persistedReducer,
  devTools: process.env.NODE_ENV !== 'production',
  middleware: [thunk],
});

export default store;

//e
```

- src/index.js
- `PersistGate`지속 상태가 검색되어 redux에 저장될 때까지 앱 UI 렌더링을 지연합니다.

```js
import store from './app/store';
import { Provider } from 'react-redux';
//s
import { PersistGate } from 'redux-persist/integration/react';
import { persistStore } from 'redux-persist';

let persistor = persistStore(store);

//e


ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
       <PersistGate loading={null} persistor={persistor}>////////s e
        <App />
      </PersistGate>               /////s e
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

```

