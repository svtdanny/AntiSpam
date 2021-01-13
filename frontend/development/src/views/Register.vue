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
        <div class="container pt-lg-md">
            <div class="row justify-content-center">
                <div class="col-lg-5">
                    <card type="secondary" shadow
                          header-classes="bg-white pb-5"
                          body-classes="px-lg-5 py-lg-5"
                          class="border-0">
                        <template>
                            <div class="text-muted text-center mb-3">
                                <h5>Регистрация</h5>
                            </div>
                        </template>
                        <template>
                            <div class="text-center text-muted mb-4">
                                <small>Antispam MSU</small>
                                <br>
                            </div>
                            
                            <form role="form" v-on:submit.prevent="register">
                                <small>{{regErrors.username}}</small>
                                <base-input alternative
                                            class="mb-3"
                                            placeholder="Login"
                                            addon-left-icon="ni ni-circle-08"
                                            v-model="username">
                                </base-input>
                                <small>{{regErrors.email}}</small>
                                <base-input alternative
                                            class="mb-3"
                                            placeholder="Email"
                                            addon-left-icon="ni ni-email-83"
                                            v-model="email">
                                </base-input>
                                <small>{{regErrors.password1}}</small>
                                <base-input alternative
                                            type="password"
                                            placeholder="Password"
                                            addon-left-icon="ni ni-lock-circle-open"
                                            v-model="password1">
                                </base-input>
                                <small>{{regErrors.password2}}</small>
                                <base-input alternative
                                            type="password"
                                            placeholder="Password"
                                            addon-left-icon="ni ni-lock-circle-open"
                                            v-model="password2">
                                </base-input>
                                
                                <p v-if="incorrectReg">{{regErrors.non_field_errors}}</p>
                                
                                
                                
                                <div class="text-muted font-italic">
                                    <small v-show="false">password strength:
                                        <span class="text-success font-weight-700">strong</span>
                                    </small>
                                </div>
                                <base-checkbox v-show="false">
                                    <span>I agree with the
                                        <a href="#">Privacy Policy</a>
                                    </span>
                                </base-checkbox>
                                <div class="text-center">
                                    <base-button native-type="submit" type="primary" class="my-3" size=sm>Создать аккаунт</base-button>
                                    <base-button tag="a" href="#/" type="secondary" class="my-3" size=sm> Назад </base-button>
                                </div>
         
                            </form>
                        </template>
                    </card>
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
        email: '',
        password1: '',
        password2:'',
        incorrectReg: false,



        regErrors:{
          username: '',
          email: '',
          password1: '',
          password2: '',  
          non_field_errors: '',
        },
      }
    },
    methods: {
        register () { 
            this.$store.dispatch('userRegister', {
            username: this.username,
            email: this.email,
            password1: this.password1,
            password2: this.password2,
            })
            .then(() => {
            this.$router.push({ name: 'login' })
            })
            .catch(err => {
            
            for (var key in err.response.data){
                this.regErrors[key] = err.response.data[key][0];
            }

      
            console.log(err.non_field_errors)

            this.baseErr = err.non_field_errors;
            console.log(err)
            this.incorrectReg = true
            
            })
            }
        }
    
  }
</script>
<style>
</style>
