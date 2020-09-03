import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: () => import('@/views/IntroPage.vue'),
  },
  {
    path: '/login',
    component: () => import('@/views/LoginPage.vue'),
  },
  {
    path: '/student',
    component: () => import('@/views/student/StudentPage.vue'),
  },
  {
    path: '/student/courses/:id/attendance/',
    component: () => import('@/views/student/StudentAttendancePage.vue'),
  },
  {
    path: '/professor',
    component: () => import('@/views/professor/ProfessorPage.vue'),
  },
  {
    path: '/professor/courses/:id',
    component: () => import('@/views/professor/ProfessorMenuPage.vue'),
  },
  {
    path: '/professor/courses/:id/students',
    component: () => import('@/views/professor/ProfessorAttendancePage.vue'),
  },
  {
    path: '/professor/courses/:courseId/students/:studentId/attendances',
    component: () =>
      import('@/views/professor/ProfessorDetailAttendancePage.vue'),
  },
  {
    path: '/professor/courses/:courseId/seats',
    component: () => import('@/views/professor/ProfessorSeatsPage.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
