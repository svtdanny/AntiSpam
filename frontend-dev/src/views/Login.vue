<template>
       <section class="section section-shaped section-lg my-0">
        <div class="shape shape-style-1 bg-gradient-default">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
          <br>
            <br>
            <br>
        <div class="container pt-lg-md">
            <div class="row justify-content-center">
                <div class="col-lg-5">
                    <card type="secondary" shadow
                          header-classes="bg-white pb-5"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                        <template>
                            <div class="text-muted text-center mb-3">
                                <h5>Личный кабинет</h5>
                            </div>

                        </template>
                        <template>
                            <div class="text-center text-muted mb-4">
                                <small>Antispam MSU</small>
                                <br>
                            </div>
                            <p v-if="incorrectAuth">Incorrect username or password entered {{a}}</p>
                            <form v-on:submit.prevent="login">
                                <base-input alternative
                                            class="mb-3"
                                            placeholder="login"
                                            addon-left-icon="ni ni-circle-08"
                                            name="login"
                                            v-model="username">
                                </base-input>
                                <base-input alternative
                                            type="password"
                                            placeholder="Password"
                                            addon-left-icon="ni ni-lock-circle-open"
                                            name="password"
                                            v-model="password">
                                </base-input>
                                <base-checkbox v-show="false">
                                    Remember me
                                </base-checkbox>
                                <div class="text-center">
                                    <base-button native-type="submit"  type="primary" class="my-4">Войти</base-button>
                                </div>
                            </form>
                        </template>
                    </card>
                    <div class="row mt-3">
                        <div class="col-6" >
                            <a href="#" class="text-light">
                                <small v-show="false">Forgot password?</small>
                            </a>
                        </div>
                        <div class="col-6 text-right">
                            <a href="#/registration">
                                <h6  class="text-light">Создать новый аккаунт</h6>
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
            this.$store.dispatch('userLogin', {
            username: this.username,
            password: this.password
            })
            .then(() => {
            this.$router.push({ name: 'profile' })
            })
            .catch(err => {
            this.a = err.non_field_errors
            console.log(err)
            this.incorrectAuth = true
            
            })
            }
        }
    
  }
</script>

<style>
</style>
