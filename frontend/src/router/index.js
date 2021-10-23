import { createRouter, createWebHistory } from 'vue-router'
import TaskList from '../views/TaskList'
import TaskDetail from '../views/TaskDetail'

const routes = [
  {
    path: '/',
    alias: '/tasks',
    name: 'task-list',
    component: TaskList
  },
  {
    path: '/tasks/:id',
    name: 'task-detail',
    component: TaskDetail
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
