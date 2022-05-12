### todo_app 구현

## todoform

```vue
<template>
  <div>
    <input type="text" @keyup.enter="createTodo" id="input1">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>

export default {
  name:'TodoForm',
  methods:{
    createTodo(event){
      const todoTitle = document.querySelector('#input1').value.trim()
      // const todoTitle = event.target.value.trim()
      const todoItem = {
        title: todoTitle,
        isCompleted:false,
        date: new Date().getTime()
      }
      if(todoTitle){
        this.$store.dispatch('createTodo', todoItem)
      }
      event.target.value = ''
      document.querySelector('#input1').value = ''
    }
  }
}
</script>
```

## todolist

```vue
<template>
  <div>
    <todo-list-item v-for="todo in todos"
    :key="todo.date"
    :todo="todo"></todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'

export default {
  name:'TodoList',
  components:{
    TodoListItem,
  },
  computed:{
    todos(){
      return this.$store.state.todos
    }
  }
}
</script>
```

## todolistitem

```vue
<template>
  <div>
    <span @click="updateTodo(todo)" :class="{'is-completed':todo.isCompleted}">
    {{todo.title}}
    </span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name:'TodoListItem',
  props:{
    todo:Object,
  },
  methods:{
    deleteTodo(){
      this.$store.dispatch('deleteTodo', this.todo)
    },
    ...mapActions(['updateTodo',])
  }
}
</script>

<style scoped>
span{
  cursor: pointer;
}
.is-completed{
  text-decoration: line-through;
}
</style>
```

## app

```vue
<template>
  <div id="app">
    <h1>Todo List</h1>
    <p>All Todos:{{allTodos}}</p>
    <p>Completed Todo:{{completedTodos}}</p>
    <p>unCompleted Todo:{{uncompletedTodos}}</p>
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoForm,TodoList
  },
  computed:{
    ...mapGetters([
      'allTodos', 'completedTodos'
    ]),
    uncompletedTodos(){
      return this.allTodos-this.completedTodos
    }
  }
}
</script>
```

## index.js

```js
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState()
  ],
  state: {//data
    todos:[
      {'title':'todo', 'isCompleted':false, 'date':12}
    ]
  },
  getters: {//computed
    allTodos(state){
      return state.todos.length
    },
    completedTodos(state){
      return state.todos.filter(todo=>{
        return todo.isCompleted
      }).length
    }
  },
  mutations: {//change
    CREATE_TODO(state, todoItem){
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem){
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx, 1)
    },
    UPDATE_TODO(state, todoItem){
      state.todos = state.todos.map(todo=>{
        if(todo === todoItem){
          return {
            ...todo,
            isCompleted : !todoItem.isCompleted
          }
        }
        else{
          return todo
        }
      })
    }
  },
  actions: {//methods
    createTodo(context, todoItem){
      context.commit('CREATE_TODO', todoItem)
    },
    deleteTodo(context, todoItem){
      context.commit('DELETE_TODO', todoItem)
    },
    updateTodo({commit}, todoItem){
      commit('UPDATE_TODO', todoItem)
    }
  },
})

```

