import Vue from 'vue'
import Router from 'vue-router'

// Containers
const Dashboard = () => import('@/components/dashboard/Dashboard')
const Home = () => import('@/components/interactwel/Home')
const Community = () => import('@/components/interactwel/Community')
const Members = () => import('@/components/interactwel/community/Members')
const Events = () => import('@/components/interactwel/community/Events')
const Groups = () => import('@/components/interactwel/community/Groups')
const Visualization = () => import('@/components/interactwel/Visualization')
const Plan = () => import('@/components/interactwel/visualization/Plan')
//const Project = () => import('@/components/interactwel/visualization/Project')
const Plans = () => import('@/components/interactwel/Plans')
const Projects = () => import('@/components/interactwel/Projects')
const CreateProject = () => import('@/components/interactwel/project/CreateProject')
const MyProjects = () => import('@/components/interactwel/project/MyProjects')
const SuggestedProjects = () => import('@/components/interactwel/project/SuggestedProjects')
const ExploreProjects = () => import('@/components/interactwel/project/ExploreProjects')
const PlansOverview = () => import('@/components/interactwel/plans/Overview')
const Feedback = () => import('@/components/interactwel/plans/Feedback')

Vue.use(Router)

export default new Router({
  mode: 'hash', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'open active',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/',
      redirect: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      children: [
          {
              path: 'dashboard',
              name: 'dashboard',
              component: Dashboard
          }
      ]
    },
    {
        path: '/home',
        //redirect: '/pages/404',
        name: 'Home',
        component: Home,
    },
    {
        path: '/visualization/:projectId',
        //redirect: '/pages/404',
        name: 'Visualization',
        component: Visualization,
        children: [
            {
                path: ':planId',
                name: 'Plan',
                component: Plan
            }
            ]
    },
    {
        path: '/plans/:projectId',
        //redirect: '/pages/404',
        redirect: '/plans/:projectId/overview',
        name: 'Plans',
        component: Plans,
        children: [
            {
                path: 'overview',
                name: 'PlansOverview',
                component: PlansOverview
            },
            {
                path: 'feedback/:planId',
                name: 'Feedback',
                component: Feedback
            },
        ]
    },
    {
        path: '/projects',
        //redirect: '/pages/404',
        redirect: '/projects/my-projects',
        name: 'Projects',
        component: Projects,
        children: [
            {
                path: 'create-project',
                name: 'CreateProject',
                component: CreateProject
            },
            {
                path: 'my-projects',
                name: 'MyProjects',
                component: MyProjects
            },
            {
                path: 'suggested-projects',
                name: 'SuggestedProjects',
                component: SuggestedProjects
            },
            {
                path: 'explore-projects',
                name: 'ExploreProjects',
                component: ExploreProjects
            }
        ]
    },
    {
        path: '/community',
        //redirect: '/pages/404',
        name: 'Community',
        redirect: '/community/members',
        component: Community,
        children: [
            {
                path: 'members',
                name: 'Members',
                component: Members
            },
            {
                path: 'events',
                name: 'Events',
                component: Events
            },
            {
                path: 'groups',
                name: 'Groups',
                component: Groups
            },
        ]
    },
  ]
})
