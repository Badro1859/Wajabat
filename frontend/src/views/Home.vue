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

    
    <b-container fluid class="mt--7">
      <!--Product-->
      <b-row>
        <b-col xl="3" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            title="Tachos Chawarma"
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              <span>category:</span> fastfood $120
            </b-card-text>

            <b-button href="javascript:;" variant="primary">Add to card</b-button>
          </b-card>
        </b-col>

        <b-col xl="3" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            title="Tachos Chawarma"
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              <span>category:</span> fastfood $120
            </b-card-text>

            <b-button href="javascript:;" variant="primary">Add to card</b-button>
          </b-card>
        </b-col>

        <b-col xl="3" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            title="Tachos Chawarma"
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              <span>category:</span> fastfood $120
            </b-card-text>

            <b-button href="javascript:;" variant="primary">Add to card</b-button>
          </b-card>
        </b-col>

        <b-col xl="3" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            title="Tachos Chawarma"
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              <span>category:</span> fastfood $120
            </b-card-text>

            <b-button href="javascript:;" variant="primary">Add to card</b-button>
          </b-card>
        </b-col>

        <b-col xl="3" md="6" class="mb-5 mb-xl-0"> 
          <b-card
            title="Tachos Chawarma"
            img-src="img/theme/img-1-1000x600.jpg"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>
              <span>category:</span> fastfood $120
            </b-card-text>

            <b-button href="javascript:;" variant="primary">Add to card</b-button>
          </b-card>
        </b-col>

      </b-row>
      <!-- End Product-->

    </b-container>
  </div>
</template>

<script>
  // Components
  import BaseProgress from '@/components/BaseProgress';
  import StatsCard from '@/components/Cards/StatsCard';
  import BaseHeader from '@/components/BaseHeader';


  export default {
    name: 'dashboard',
    components: {
      BaseProgress,
      StatsCard,
      BaseHeader,
    },
  };
</script>

<style>
</style>
