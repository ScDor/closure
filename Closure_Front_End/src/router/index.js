import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Settings from '../views/Settings.vue'
import CourseImport from '../views/CourseImport.vue'
import { routeGuard } from '@/auth/index.js'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings,
    beforeEnter: routeGuard
  },
  {
    path: '/scrape',
    name: 'Scrape',
    component: CourseImport,
    beforeEnter: routeGuard
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
