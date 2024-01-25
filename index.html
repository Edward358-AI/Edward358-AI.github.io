<script setup>
  import { ref, computed, watch } from 'vue'

  const chars = 'abcdefghijklmnopqrstuvwxyz0123456789'.split('')
  function newId() {
    let newId = ""
    for (let i = 0; i < 7; i++) {
      newId += chars[Math.floor(Math.random() * chars.length)]
    }
    return newId
  }
  const newTodo = ref("")
  const todos = ref([{id: newId(), text: "Learn Vue.js", complete: false, editing: false}])
  if (Array.isArray(JSON.parse(localStorage.getItem("todos")))) {
    todos.value = JSON.parse(localStorage.getItem("todos"))
  }
  setInterval(() => {localStorage.setItem("todos", JSON.stringify(todos.value))}, 60)
  
  
  function addTodo() {
    newTodo.value.replace(/^\s+|\s+$/g, '') ? todos.value.push({id: newId(), text: newTodo.value, complete: false, editing: false}) : ""
    newTodo.value = ""
  }

  function removeTodo(todo) {
    todos.value = todos.value.filter((t) => t.id !== todo.id)
  }
  function isEmpty(obj) {
    for (var prop in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, prop)) {
        return false;
      }
    }
    return true
  }
</script>

<template>
  <h1>To-do List</h1>
  <p>Made by Edward Jiang</p>
  <form @submit.prevent="addTodo">
    <input type="text" class="form-control" v-model="newTodo" />
    <input type="submit" value="Add Todo" class="btn btn-light" />
  </form>
  <p style="font-size:1.2rem;" :class="isEmpty(todos) ? '' : 'd-none'">Hooray! You've finished everything on your todo list! Cheers :D</p>
  <div class="todo-container card" :class="isEmpty(todos) ? 'd-none' : ''">
    <ul class="list-group list-group-flush">
      <li class="list-group-item" v-for="todo in todos" :class="todo.complete ? 'bg-light' : ''">
        <span :class="todo.complete ? 'done' : ''">
          {{ todo.editing ? '' : todo.text }}
        <form @submit.prevent="todo.editing=false" class="inlineform" :class="todo.editing ? '' : 'd-none'">
          <input type="text" class="form-control" v-model="todo.text"/>
          <input type="submit" value="Update" class="btn btn-light" />
        </form>
        </span>
        <span class="options">
          <i class="bi bi-bookmark-check text-success" @click="todo.complete = !todo.complete"></i>
          <i class="bi bi-pencil-square text-muted" @click="todo.editing = !todo.editing"></i>
          <i class="bi bi-x-circle text-danger" @click="removeTodo(todo)"></i>
        </span>
      </li>
    </ul>
  </div>
</template>
