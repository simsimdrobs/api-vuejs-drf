<template>
  <div class="tasks">
      <div class="table">
          <table class="w-50 m-auto">
              <thead>
                  <td>TASK</td>
                  <td>ACCOMPLISHED?</td>
              </thead>
              <tr v-for="task in tasks" :key="task.id">
                  <td>{{ task.content }}</td>
                  <td>{{ task.completion }}</td>
                  <td><router-link class="btn btn-secondary" :to="{'name': 'task-detail', 'params': {'id': task.id}}">See Task</router-link></td>
                  <td><button class="btn btn-danger" @click="deleteTask(task.id)">Delete Task</button></td>
              </tr>
          </table>
      </div>
      <br><br>
      <button class="btn btn-primary" @click="addTask()">Add a Task</button>
      <br><br>
      <task-create v-if="create"/>
  </div>
</template>

<script>
import axios from 'axios'
import TaskCreate from '../components/TaskCreate.vue'
export default {
    name: 'TaskList',
    components: {TaskCreate},
    data() {
        return {
            tasks: [],
            create: false
        }
    },
    methods: {
        getTaskList() {
            axios.get('http://127.0.0.1:8000/api/tasks/')
            .then(response => {
                this.tasks = response.data
                console.log(response)
            })
        },
        addTask() {
            this.create = !this.create
            console.log(this.create)
        },
        deleteTask(id) {
            if (confirm("Are you sure you want to delete the task?")) {
                axios.delete(`http://127.0.0.1:8000/api/tasks/${id}/`)
                .then(response => {
                    window.location.reload()
                    console.log(response)
                })
            }
        }
        
    },
    mounted() {
        this.getTaskList()
    },
}
</script>

<style>

</style>