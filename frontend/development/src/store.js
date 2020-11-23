 
import Vue from 'vue';
import Vuex from 'vuex';
import { getAPI } from './axios-api';

Vue.use(Vuex);
export default new Vuex.Store({
    modules: {
        autentification: {
            namespaced: true,

            state: {
                accessToken: null,
                refreshToken: null,
                APIData: ''
            },
            mutations: {
                updateStorage (state, { access, refresh }) {
                state.accessToken = access
                state.refreshToken = refresh
                },
                destroyToken (state) {s
                state.accessToken = null
                state.refreshToken = null
                }
            },
            getters: {
                loggedIn (state) {
                return state.accessToken != null
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
                    getAPI.post('/api-token/', {
                    username: usercredentials.username,
                    password: usercredentials.password
                    })
                    .then(response => {
                        context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh }) 
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
                })
                }
            }
        },

        LearnSets: {
            namespaced: true,

            state: {
                VolumeInbox: 5,
                VolumeSpam: 5
            },
            mutations: {
                updateStorage (state, {VolumeInbox, VolumeSpam}) {
                state.VolumeInbox = VolumeInbox
                state.VolumeSpam = VolumeSpam
                }
            },
            actions: {
                getData (context) {
                return new Promise((resolve, reject) => {
                    getAPI.get('profile/get/')
                    .then(response => {
                        context.commit('updateStorage', { VolumeInbox: response.data.VolumeInbox, VolumeSpam: response.data.VolumeSpam}) 
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
                })
                }
            }
        }

    }
    })