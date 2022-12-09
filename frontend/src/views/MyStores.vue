<template>
  <div>
    <base-header class="mb-5 pb-6 pt-5 pt-md-8 bg-gradient-success text-center">
      <h2 class="text-white mt-0 mb-3">Hi, create your own store here ...</h2>
      <base-button type="default" class="mb-3" @click="modals.form = true">new store</base-button>
    </base-header>

    <b-container fluid class="mt--7">
      <!--Product-->
      <b-row>
        <b-col v-for="item in stores" :key="item.id" xl="4" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text class="text-center">
              <h2>{{item.name}}</h2> 
              <h4 class="mt-0 text-muted"> foods: 2</h4>
            </b-card-text>

            <b-card-footer class="pb-0 pt-2 mb-0 text-center">
              <b-button href="javascript:;" variant="primary">Show</b-button>
            </b-card-footer>
          </b-card>
        </b-col>
      </b-row>
      <!-- End Product-->
    </b-container>

    <!--Form modal
    <modal :show.sync="modals.form"
          size="sm"
          body-classes="p-0">
      <card type="secondary"
            header-classes="bg-transparent pb-5"
            body-classes="px-lg-5 py-lg-5"
            class="border-0 mb-0">

        <template slot="header">
          <div class="text-muted text-center mt-2 mb-3">
            <small>Sign in with</small>
          </div>
          <div class="btn-wrapper text-center">
            <base-button type="neutral" icon>
              <span class="btn-inner--icon"><img src="img/icons/common/github.svg"></span>
              <span class="btn-inner--text">Github</span>
            </base-button>
            <base-button type="neutral" icon>
              <span class="btn-inner--icon"><img src="img/icons/common/google.svg"></span>
              <span class="btn-inner--text">Google</span>
            </base-button>
          </div>
        </template>

        <template>
          <div class="text-center text-muted mb-4">
            <small>Or sign in with credentials</small>
          </div>
          <b-form role="form">
            <base-input alternative
                        v-model="formModal.email"
                        class="mb-3"
                        placeholder="Email"
                        prepend-icon="ni ni-email-83">
            </base-input>
            <base-input alternative
                        v-model="formModal.password"
                        type="password"
                        placeholder="Password"
                        prepend-icon="ni ni-lock-circle-open">
            </base-input>
            <b-form-checkbox v-model="formModal.remember">
              Remember me
            </b-form-checkbox>
            <div class="text-center">
              <base-button type="primary" class="my-4">Sign In</base-button>
            </div>
          </b-form>
        </template>
      </card>
    </modal>-->
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: "stores",
    data () {
      return {
        stores: {}
      }
    },
    mounted() {
      this.getStores();
    },
    methods: {
      async getStores() {
        const url =  "http://127.0.0.1:8000/food/store/";
        await axios
          .get(url)
          .then(response => {
            this.stores = response.data;
            console.log(response.data)
          })
          .catch(errors => {
            console.log(errors);
          })
      }
    }
  };
</script>