<template>
  <div class="update">
        <form class="input-group w-50 m-auto">
            <input class="form-control" required type="text" name="content" id="content" v-model="task.content" placeholder="content">
            <select class="form-control" v-model="task.completion" name="completion" id="completion">
                <option disabled value="">Choose</option>
                <option v-for="(choice, i) in choices" :key="i">{{ choice }}</option>
            </select>
            <button class="btn btn-success" @click="updateTask(task.id)">update</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'TaskUpdate',
    props: {
        task: {
            id: Number,
            content: String,
            completion: String
        }
    },
    data() {
        return {
            choices: ['done', 'not done']
        }
    },
    methods: {
        getTask(id) {
            axios.get(`http://127.0.0.1:8000/api/tasks/${id}/`)
            .then(response => {
                this.task.content = response.data.content
                this.task.completion = response.data.completion
                console.log(response)
            })
        },
        updateTask(id) {
            axios.put(`http://127.0.0.1:8000/api/tasks/${id}/`,
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