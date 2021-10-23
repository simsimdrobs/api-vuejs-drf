<template>
  <div class="create">
        <form class="input-group w-50 m-auto">
            <input class="form-control" required type="text" name="content" id="content" v-model="task.content" placeholder="content">
            <br><br>
            <select class="form-control" v-model="task.completion" name="completion" id="completion">
                <option disabled value="">Choose</option>
                <option v-for="(choice, i) in task.choices" :key="i">{{ choice }}</option>
            </select>
            <br><br>
            <button class="btn btn-success" @click="createTask()">create</button>
        </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'TaskCreate',
    data() {
        return {
            task: {
                content: '',
                choices: ['done', 'not done'],
                completion: ''
            }
        }
    },
    methods: {
        createTask() {
            axios.post('http://127.0.0.1:8000/api/tasks/',
            {
                content: this.task.content,
                completion: this.task.completion
            })
            .then(response => {
                console.log(response)
            })
        }
    },
}
</script>

<style>

</style>