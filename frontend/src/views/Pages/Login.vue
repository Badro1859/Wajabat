<template>
  <div>
    <!-- Header -->
    <div class="header bg-gradient-success py-7 py-lg-8 pt-lg-9">
      <div class="separator separator-bottom separator-skew zindex-100">
        <svg x="0" y="0" viewBox="0 0 2560 100" preserveAspectRatio="none" version="1.1"
             xmlns="http://www.w3.org/2000/svg">
          <polygon class="fill-default" points="2560 0 2560 100 0 100"></polygon>
        </svg>
      </div>
    </div>
    
    <!-- Page content -->
    <b-container class="mt--8 pb-5">
      <b-row class="justify-content-center">
        <b-col lg="5" md="7">

          <b-card no-body class="bg-secondary border-0 mb-0">
            <b-card-body class="bg-transparent pt-5 pb-0">
              <h1 class="text-center text-muted mb-5">Sign In</h1>
              
              <validation-observer v-slot="{handleSubmit}" ref="formValidator">
                <b-form role="form" @submit.prevent="handleSubmit(onSubmit)">
                  <base-input alternative
                              class="mb-3"
                              name="username"
                              :rules="{required: true}"
                              prepend-icon="ni ni-email-83"
                              placeholder="usrename"
                              v-model="username">
                  </base-input>

                  <base-input alternative
                              class="mb-3"
                              name="password"
                              :rules="{required: true}"
                              prepend-icon="ni ni-lock-circle-open"
                              type="password"
                              placeholder="Password"
                              v-model="password">
                  </base-input>

                  <b-form-checkbox v-model="rememberMe">Remember me</b-form-checkbox>
                  
                  <div class="text-center">
                    <base-button type="primary" native-type="submit" class="my-4">Sign in</base-button>
                  </div>
                </b-form>
              </validation-observer>
            </b-card-body>
            
            <b-card-footer class="bg-transparent">
              <div class="text-muted text-center mb-3"><small>Or sign in with</small></div>
              <div class="btn-wrapper text-center">
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon"><img src="img/icons/common/github.svg"></span>
                  <span class="btn-inner--text">Github</span>
                </a>
                <a href="#" class="btn btn-neutral btn-icon">
                  <span class="btn-inner--icon"><img src="img/icons/common/google.svg"></span>
                  <span class="btn-inner--text">Google</span>
                </a>
              </div>
            </b-card-footer>
          </b-card>

          <b-row class="mt-3">
            <b-col cols="6">
              <router-link to="/dashboard" class="text-light"><small>Forgot password?</small></router-link>
            </b-col>
            <b-col cols="6" class="text-right">
              <router-link to="/register" class="text-light"><small>Create new account</small></router-link>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password: '',
        rememberMe: false,
        errors: []
      };
    },
    methods: {
      async onSubmit() {
        // this will be called only after form is valid. You can do api call here to login
        
        const formData = {
          username: this.username,
          password: this.password
        }

        //// clear old login informations
        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token")

        await axios 
          .post('http://127.0.0.1:8000/food/auth/token/login/', formData)
          .then(response => {
            // console.log('response :', response.data)
            // get token from response data
            const token = response.data.auth_token 

            // save token in axios headers for later requests
            axios.defaults.headers.common["Authorization"] = "Token " + token 

            // save token in store 
            this.$store.commit('setToken', token, )

            // save token in local storage for later use in other login
            localStorage.setItem('token', token)

            // // redirect to home page
            const toPath = this.$route.query.to || '/home'
            this.$router.push(toPath)

            // console.log('token : ', token);
            // console.log('path : ', toPath);
          })
          .catch(error => {
            if (error.response) {
              for(const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else {
              this.errors.push('Something went wrong. Please try again')
              console.log(JSON.stringify(error))
            }
            console.log(this.errors);
          })
      }
    }
  };
</script>
