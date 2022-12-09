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
      <!-- Table -->
      <b-row class="justify-content-center">
        <b-col lg="8" md="10" >
          <b-card no-body class="bg-secondary border-0">
            <b-card-body class="px-lg-5 pt-lg-5">
              <h1 class="text-center text-muted mb-5">Sign Up</h1>

              <validation-observer v-slot="{handleSubmit}" ref="formValidator">
                <b-form role="form" @submit.prevent="handleSubmit(onSubmit)">
                  
                  <b-row>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="Username"
                              name="Name"
                              :rules="{required: true}"
                              v-model="model.username">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-email-83"
                              placeholder="Email"
                              name="Email"
                              :rules="{required: true, email: true}"
                              v-model="model.email">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="First name"
                              name="first_name"
                              v-model="model.first_name">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="Last name"
                              name="last_name"
                              v-model="model.last_name">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="Address"
                              name="address"
                              v-model="model.address">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="City"
                              name="city"
                              v-model="model.city">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="Postal Code"
                              name="postal_code"
                              v-model="model.postal_code">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-hat-3"
                              placeholder="About"
                              name="about"
                              v-model="model.postal_code">
                      </base-input>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-lock-circle-open"
                              placeholder="password"
                              type="password"
                              name="Password"
                              :rules="{required: true, min: 6}"
                              v-model="model.password">
                      </base-input>
                    </b-col>
                    <b-col lg="6">
                      <base-input alternative
                              class="mb-3"
                              prepend-icon="ni ni-lock-circle-open"
                              placeholder="password again"
                              type="password"
                              name="Password"
                              :rules="{required: true, min: 6}"
                              v-model="password2">
                      </base-input>
                    </b-col>
                  </b-row>
                  <div class="text-muted font-italic mt--3">
                    <small class="text-danger font-weight-700 passError"></small>
                  </div>
                  
                  <!-- <b-row class=" pl-2 mt-4">
                    <b-col cols="12">
                      <base-input :rules="{ required: { allowFalse: false } }" name=Privacy Policy>
                        <b-form-checkbox>
                          <span class="text-muted ml--3">I agree with the <a href="#!">Privacy Policy</a></span>
                        </b-form-checkbox>
                      </base-input>
                    </b-col>
                  </b-row> -->

                  <div class="text-center">
                    <b-button type="submit" variant="primary" class="mt-0">Create account</b-button>
                  </div>
                </b-form>
              </validation-observer>
            </b-card-body>

            <b-card-footer class="bg-transparent">
              <div class="text-muted text-center mt-0 mb-2"><small>Or sign up with</small></div>
              <div class="text-center">
                <a href="#" class="btn btn-neutral btn-icon mr-4">
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
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios';

  export default {
    name: 'register',
    data() {
      return {
        model: {
          username: '',
          email: '',
          password: '',
          first_name: '',
          last_name: '',
          address: '',
          city: '',
          postal_code: '',
          about: ''
        },
        password2: '',
        wrongPass: '',
        errors: [],
      }
    },
    methods: {
      validPassword() {
        if (this.password2 != this.model.password) {
          document.getElementById('passError').textContent = 'the two password not equal';
          return false;
        }
        return true;
      },  
      async onSubmit() {
        // this will be called only after form is valid. You can do an api call here to register users
        if (this.validPassword) {

          //// clear old login informations
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.removeItem("token")

          console.log('axios started')
          // send request to backend 
          await axios 
            .post('http://127.0.0.1:8000/food/users/', this.model)
            .then(response => {
              console.log('register success')

              this.$router.push('/login');
            })
            .catch(errors => {
              if (errors.response) {
                console.log(errors.response.data)
              } else {
                console.log('wrong !!')
              }
            })
        }
      }
    }

  };
</script>
<style></style>
