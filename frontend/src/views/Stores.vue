<template>
  <div>
    <div class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center profile-header"
        style="min-height: 600px; background-image: url(img/theme/img-1-1000x600.jpg); background-size: cover; background-position: center top;">
      <b-container fluid>
        <!-- Mask -->
        <span class="mask bg-gradient-success opacity-8"></span>

        <!-- Header container -->
        <b-container fluid>
          <b-row align-h="between">
            <b-col sm="6">
              <h1 class="display-1 text-white">{{store.name}}</h1>
              <base-button type="primary">Edit store</base-button>
              <base-button type="primary">new food</base-button>
            </b-col>

            <b-col sm="3">
              <stats-card title="Sales"
                  type="gradient-green"
                  :sub-title="nbSales"
                  icon="ni ni-money-coins"
                >
              </stats-card>
            </b-col>
            <b-col sm="3">
              <stats-card title="Foods"
                  type="gradient-green"
                  :sub-title="nbFoods"
                  icon="ni ni-money-coins"
                >
              </stats-card>
            </b-col>
          </b-row>
        </b-container>
      </b-container>
    </div>

    <b-container fluid class="mt--7">
      <!-- Foods -->
      <b-row>
          <b-col v-for="(item, index) in store.products" :key="index" xl="3" md="6" class="mb-5 mb-xl-0"> 
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
              <div>
                <span class="text-muted mr-2">category:</span>
                <span class="inline font-weight-700">{{item.category}}</span>
              </div>
              <h3 class="font-weight-700 text-right mt--4">${{item.price}}</h3>
            </b-card-text>

            <b-card-footer class="pb-0 pt-2 mb-0 text-center">
              <b-button href="javascript:;" variant="primary">Edit</b-button>
              <b-button href="javascript:;" variant="danger">Delete</b-button>
            </b-card-footer>            
          </b-card>
          </b-col>
      </b-row>
      <!-- End Foods -->
    </b-container>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: "stores",
    props: {
      storeURL: String,
    },
    data() {
      return {
        store: {},
        nbFoods: "0",
        nbSales: "0",
      }
    },
    mounted() {
      this.getStore();
    },
    methods: {
      async getStore() {

        const url = "http://127.0.0.1:8000/food/store/1/"

        await axios 
          .get(url)
          .then(response => {
            this.store = response.data;
            this.nbFoods = this.store.products.length.toString()
          })
          .catch(errors => {
            console.log(errors);
          })
      }
    }
  };
</script>