<template>
  <div class="task">
      <div class="table">
        <table class="w-50 m-auto">
            <thead>
                <td>TASK</td>
                <td>ACCOMPLISHED?</td>
            </thead>
            <tr>
                <td>{{ task.content }}</td>
                <td>{{ task.completion }}</td>
            </tr>
        </table>
      </div>
      <br><br>
      <button class="btn btn-primary" @click="updateTask()">Update Task</button>
      <router-link class="m-4 btn btn-secondary" :to="{'name': 'task-list'}">Back to List</router-link>
      <br><br><br>
      <task-update :task="task" v-if="update"/>
  </div>
</template>

<script>
import axios from 'axios'
import TaskUpdate from '../components/TaskUpdate.vue'
export default {
    name: 'TaskDetail',
    components: {TaskUpdate},
    data() {
        return {
            task: {
                id: '',
                content: '',
                completion: null
            },
            update: false
        }
    },
    methods: {
        getTask() {
            let index = this.$route.params.id
            axios.get(`http://127.0.0.1:8000/api/tasks/${index}/`)
            .then(response => {
                this.task.id = response.data.id
                this.task.content = response.data.content
                this.task.completion = response.data.completion
                console.log(response)
            })
        },
        updateTask() {
            this.update = !this.update
            console.log(this.update)
        }
    },
    mounted() {
        this.getTask()
    },
}
</script>

<style>

</style>