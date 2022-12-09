<template>
  <div>
    <base-header class="pb-6 pb-8 pt-5 pt-md-8 bg-gradient-success">
      <!-- Card stats -->
      <b-row>
        <b-col xl="4" md="6">
          <stats-card title="Total foods"
                      type="gradient-red"
                      sub-title="350,897"
                      icon="ni ni-active-40"
                      class="mb-4">
          </stats-card>
        </b-col>
        <b-col xl="4" md="6">
          <stats-card title="Total stores"
                      type="gradient-orange"
                      sub-title="2,356"
                      icon="ni ni-chart-pie-35"
                      class="mb-4">
          </stats-card>
        </b-col>
        <b-col xl="4" md="6">
          <stats-card title="Sales"
                      type="gradient-green"
                      sub-title="924"
                      icon="ni ni-money-coins"
                      class="mb-4">
          </stats-card>
        </b-col>
      </b-row>
      <!-- End Card stats -->
    </base-header>

    <!--Products-->
    <b-container fluid class="mt--7">
      <b-row>
        <b-col v-for="item in products" :key="item.id"  xl="3" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            :title="item.name"
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>

              <div class="text-muted font-italic mt--3">
                <span>category:</span> <span class="inline font-weight-700">{{item.category}}</span>
              </div>
              <h3 class="font-weight-700 text-right mt--4">${{item.price}}</h3>
            </b-card-text>

            <b-card-footer class="pb-0 pt-2 mb-0 text-center">
              <b-button href="javascript:;" variant="primary">Add to card</b-button>
            </b-card-footer>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
    <!-- End Products-->
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'dashboard',
    data() {
      return {
        products: {}
      }
    },
    mounted() {
      this.getAllProducts();
    },
    methods: {
      async getAllProducts() {

        const url = 'http://127.0.0.1:8000/food/products/';

        await axios
          .get(url)
          .then(response => {
            this.products = response.data;
            console.log(this.products);
          })
          .catch(errors => {
            console.log(errors);
          })

      }
    }
  };
</script>

<style>
</style>
