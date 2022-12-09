<template>
  <div>
    <div class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center profile-header"
        style="min-height: 600px; background-image: url(img/theme/img-1-1000x600.jpg); background-size: cover; background-position: center top;">
      <b-container fluid>
        <!-- Mask -->
        <span class="mask bg-gradient-success opacity-7"></span>
        <!-- Header container -->
        <b-container fluid class="d-flex align-items-center">
          <b-row >
            <b-col v-if="$store.state.isAuthenticated" lg="7" md="10">
              <h1 class="display-2 text-white">Hello, {{user.username}}</h1>
              <p class="text-white mt-0 mb-5">This is your profile page. You can see the progress you've made with your
                work and manage your projects or assigned tasks</p>
            </b-col>
            <b-col v-else>
              <h2 class="display-3 text-white">Hello friend, please login or sinup</h2>
              <router-link v-bind:to="`/login`" class="btn btn-primary">login</router-link>
              <router-link v-bind:to="`/register`" class="btn btn-primary">register</router-link>
            </b-col>
          </b-row>
        </b-container>
      </b-container>
    </div>

    <b-container v-if="$store.state.isAuthenticated" fluid class="mt--9">
      <b-row>
        <b-col xl="4" class="order-xl-2 mb-5">
          <user-card :user="user"></user-card>
        </b-col>
        <b-col id="edit" xl="8" class="order-xl-1">
          <edit-profile-form :user="user"></edit-profile-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script lang="js">
  import axios from 'axios';

  import EditProfileForm from './UserProfile/EditProfileForm.vue';
  import UserCard from './UserProfile/UserCard.vue';

  export default {
    components: {
      EditProfileForm,
      UserCard,
    },
    data() {
      return {
        user: {}
      }
    },
    mounted() {
      if (this.$store.state.isAuthenticated){
        this.initalisation()
      }
    },
    methods: {
      async initalisation() {
        
        const url = 'http://127.0.0.1:8000/food/users/'
        await axios
          .get(url)
          .then(response => {
            this.user = response.data[0];
          })
          .catch(errors => {
            console.log(errors)
          })
      },
    },
  };
</script>
<style>
</style>
