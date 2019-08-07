import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Scheduler from '@/components/Scheduler'
import About from '@/components/About'
import NotFound from '@/components/NotFound'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/scheduler',
      name: 'Scheduler',
      component: Scheduler
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
