<template>
  <b-card no-body class="card-profile" alt="Image placeholder" img-top>
    <b-row class="justify-content-center">
      <b-col lg="3" class="order-lg-2">
        <div class="card-profile-image">
          <a href="#">
            <b-img src="img/theme/img-1-1000x900.jpg" rounded="circle" />
          </a>
        </div>
      </b-col>
    </b-row>


    <b-card-body class="pt-0 mt-5">
      <b-row>
        <b-col >
          <div class="card-profile-stats d-flex justify-content-center mt-md-5">
            <div>
              <span class="heading">22</span>
              <span class="description">Stores</span>
            </div>
            <div>
              <span class="heading">10</span>
              <span class="description">Sales</span>
            </div>
            <div>
              <span class="heading">89</span>
              <span class="description">Comments</span>
            </div>
          </div>
        </b-col>
      </b-row>

      <div class="text-center">
        <h5 class="h3">
          {{user.username}}<span class="font-weight-light">, 27</span>
        </h5>
        <div class="h5 font-weight-300">
          <i class="ni location_pin mr-2"></i>ALger, Algeria
        </div>

        <hr class="my-4">
      </div>
    </b-card-body>
  </b-card>
</template>

<script>
export default {
  props: {
    user: Object,

  }
};
</script>
<style></style>
