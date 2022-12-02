<template>
  <div>
    <base-header class="mb-5 pb-6 pt-5 pt-md-8 bg-gradient-success text-center">
      <h2 class="text-white mt-0 mb-3">Hi, create your own store here ...</h2>
      <a href="#!" class="btn btn-info mb-5">new store</a>
    </base-header>

    <b-container fluid class="mt--7">
      <!--Product-->
      <b-row>
        <b-col xl="4" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text class="text-center">
              <h2>Mehdi Food</h2> 
              <h4 class="mt-0 text-muted"> foods: 25</h4>
            </b-card-text>

            <b-card-footer class="pb-0 pt-2 mb-0 text-center">
              <b-button href="javascript:;" variant="primary">Show</b-button>
            </b-card-footer>
          </b-card>
        </b-col>

        <b-col xl="4" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text class="text-center">
              <h2>Mehdi Food</h2> 
              <h4 class="mt-0 text-muted"> foods: 25</h4>
            </b-card-text>

            <b-card-footer class="pb-0 pt-2 mb-0 text-center">
              <b-button href="javascript:;" variant="primary">Show</b-button>
            </b-card-footer>
          </b-card>
        </b-col>
        
        <b-col xl="4" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text class="text-center">
              <h2>Mehdi Food</h2> 
              <h4 class="mt-0 text-muted"> foods: 25</h4>
            </b-card-text>

            <b-card-footer class="pb-0 pt-2 mb-0 text-center">
              <b-button href="javascript:;" variant="primary">Show</b-button>
            </b-card-footer>
          </b-card>
        </b-col>
      </b-row>
      <!-- End Product-->
    </b-container>
  </div>
</template>

<script>
  import BaseHeader from '@/components/BaseHeader'
  export default {
    name: "stores",
    components: {
      BaseHeader,
    }
  };
</script>