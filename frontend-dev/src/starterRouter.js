import Vue from "vue";
import Router from "vue-router";
import Header from "./layout/AppHeader";
import Footer from "./layout/AppFooter";

const Login = () => import("./views/Login.vue")
const Register = () => import('./views/Register.vue')

const Profile = () => import('./views/Profile.vue')

const Components = () => import('./views/Components.vue')
const Hero = () => import('./views/components/Hero.vue')

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "login",
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


  ]
});
