<template>
    <section class="section-hero section-shaped my-0">
        <div class="shape shape-style-1 shape-primary">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
        <div class="container pt-lg-md">
            <div class="row justify-content-center">
                <div class="col-lg-5">
                    <card type="secondary" shadow
                          header-classes="bg-white pb-5"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                        <template>
                            <div class="text-muted text-center mb-3">
                                <small>Sign in</small>
                            </div>

                        </template>
                        <template>
                            <div class="text-center text-muted mb-4">
                                <small>CMC MSU AntiSpam</small>
                            </div>
                            <p v-if="incorrectAuth">Incorrect username or password entered {{a}}</p>
                            <form v-on:submit.prevent="login">
                                <base-input alternative
                                            class="mb-3"
                                            placeholder="Email"
                                            addon-left-icon="ni ni-email-83"
                                            name="username"
                                            v-model="username">
                                </base-input>
                                <base-input alternative
                                            type="password"
                                            placeholder="Password"
                                            addon-left-icon="ni ni-lock-circle-open"
                                            name="password"
                                            v-model="password">
                                </base-input>
                                <base-checkbox>
                                    Remember me
                                </base-checkbox>
                                <div class="text-center">
                                    <base-button native-type="submit"  type="primary" class="my-4">Sign In</base-button>
                                </div>
                            </form>
                        </template>
                    </card>
                    <div class="row mt-3">
                        <div class="col-6">
                            <a href="#" class="text-light">
                                <small>Forgot password?</small>
                            </a>
                        </div>
                        <div class="col-6 text-right">
                            <a href="#/registration" class="text-light">
                                <small>Create new account</small>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        username: '',
        password: '',
        a:'',
        incorrectAuth: false
      }
    },
    methods: {
        login () { 
            this.$store.dispatch('autentification/userLogin', {
            username: this.username,
            password: this.password
            })
            .then(() => {
            this.$router.push({ name: 'profile' })
            })
            .catch(err => {
            this.a = err
            console.log(err)
            this.incorrectAuth = true
            
            })
            }
        }
    
  }
</script>

<style>
</style>
