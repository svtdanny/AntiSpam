import Vue from "vue";
import Router from "vue-router";
import Header from "./layout/AppHeader";
import Footer from "./layout/AppFooter";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";
import Profile from "./views/Profile.vue";

import Components from "./views/Components.vue"

import Hero from "./views/components/Hero.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "sign-in",
      components: {
        default: Login,
        footer: Footer
      }
    },

    {
      path: "/registration",
      name: "registration",
      components: {
        default: Register,
        footer: Footer
      }
    },

    {
      path: "/profile",
      name:"profile",
      components: {
        default: Profile,
        footer: Footer
      }
    },

    {
      path: '/hero',
      name:'hero',
      components: {
        default: Hero,
      }
    },

    {
      path: '/Components',
      name:'hero',
      components: {
        default: Components,
      }
    }

  ]
});
