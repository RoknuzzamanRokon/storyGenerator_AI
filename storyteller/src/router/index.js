import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
      path: "/",
      name: "New",
      component: () => import("../views/New.vue"),
      meta: { title: "Create Story" },
    },
    {
      path: "/Creates",
      name: "Creates",
      component: () => import("../views/Up.vue"),
      meta: { title: "Create Story" },
    },
    {
      path: "/Main",
      name: "Home",
      component: () => import("../views/HomeView.vue"),
      meta: { title: "Welcome" },
    },
 
    {
      path: "/Create",
      name: "Create",
      component: () => import("../views/Create.vue"),
      meta: { title: "Create Story" },
    },
  ],
});
router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  next();
});
export default router;
