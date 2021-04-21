import Vue from 'vue';
import Vuex from 'vuex';
import { getAPI } from './axios-api';
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);
export default new Vuex.Store({
    plugins: [createPersistedState()],
            state: {
                username:'',
                accessToken: null,
                refreshToken: null,
                APIData: ''
            },
            mutations: {
                updateStorage (state, { access, token }) {
                state.accessToken = token
                },

                updateUsername (state, { access, username }) {
                    state.username = username
                    },

                destroyToken (state) {
                state.accessToken = null
                state.refreshToken = null
                }
            },
            getters: {
                loggedIn (state) {
                return state.accessToken != null
                },
                username (state){
                    return state.username;
                }
            },
            actions: {
                userLogout (context) {
                if (context.getters.loggedIn) {
                    context.commit('destroyToken')
                }
                },
                userLogin (context, usercredentials) {
                   
                return new Promise((resolve, reject) => {
                    getAPI.post('/rest-auth/login/', {
                        headers: {},
                    username: usercredentials.username,
                    password: usercredentials.password
                    })
                    .then(response => {
                        context.commit('updateStorage', { token: response.data.key}) 
                        context.commit('updateUsername', {username: response.data.user.username})
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
                })
                },

                userRegister (context, usercredentials) {
                   
                    return new Promise((resolve, reject) => {
                        getAPI.post('/rest-auth/registration/', {
                            headers: {},
                        username: usercredentials.username,
                        email: usercredentials.email,
                        password1: usercredentials.password1,
                        password2: usercredentials.password2,
                        })
                        .then(response => {
                            context.commit('updateStorage', { token: response.data.key}) 
                            resolve()
                        })
                        .catch(err => {
                            reject(err)
                        })
                    })
                    }
            }
    })