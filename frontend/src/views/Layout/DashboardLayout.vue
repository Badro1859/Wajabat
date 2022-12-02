<template>
  <div class="wrapper">
    <notifications></notifications>

    <side-bar>
      <template slot="links">
        <sidebar-item
          :link="{
            name: 'Home',
            path: '/home',
            icon: 'ni ni-tv-2 text-primary',
          }"
        >
        </sidebar-item>

        <sidebar-item
            :link="{
              name: 'Stores',
              path: '/stores',
              icon: 'ni ni-planet text-blue'
            }"
          >
        </sidebar-item>

        <sidebar-item
            :link="{
              name: 'Profile',
              path: '/profile',
              icon: 'ni ni-planet text-blue'
            }"
          >
        </sidebar-item>

        <sidebar-item
            :link="{
              name: 'My Stores',
              path: '/mystores',
              icon: 'ni ni-planet text-blue'
            }"
          >
        </sidebar-item>

        <sidebar-item
            :link="{
              name: 'My Order',
              path: '/order',
              icon: 'ni ni-planet text-blue'
            }"
          >
        </sidebar-item>
      </template>

      <template slot="links-after">
        <hr class="my-3">
        <h6 class="navbar-heading p-0 text-muted">categories</h6>

        <b-nav class="navbar-nav mb-md-3">
          <b-nav-item href="https://www.creative-tim.com/learning-lab/bootstrap-vue/quick-start/argon-dashboard">
            <i class="ni ni-spaceship"></i>
            <b-nav-text class="p-0">Category 01</b-nav-text>
          </b-nav-item>

          <b-nav-item href="https://www.creative-tim.com/learning-lab/bootstrap-vue/colors/argon-dashboard">
              <i class="ni ni-palette"></i>
              <b-nav-text class="p-0">Category 01</b-nav-text>
          </b-nav-item>

          <b-nav-item href="https://www.creative-tim.com/learning-lab/bootstrap-vue/avatar/argon-dashboard">
              <i class="ni ni-ui-04"></i>
              <b-nav-text class="p-0">Category 01</b-nav-text>
          </b-nav-item>
        </b-nav>
      </template>
    </side-bar>

    <div class="main-content">
      <dashboard-navbar :type="$route.meta.navbarType"></dashboard-navbar>

      <div @click="$sidebar.displaySidebar(false)">
        <main-content></main-content>
      </div>

      <content-footer v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>
<script>
  /* eslint-disable no-new */
  import PerfectScrollbar from 'perfect-scrollbar';
  import 'perfect-scrollbar/css/perfect-scrollbar.css';

  function hasElement(className) {
    return document.getElementsByClassName(className).length > 0;
  }

  function initScrollbar(className) {
    if (hasElement(className)) {
      new PerfectScrollbar(`.${className}`);
    } else {
      // try to init it later in case this component is loaded async
      setTimeout(() => {
        initScrollbar(className);
      }, 100);
    }
  }

  import DashboardNavbar from './DashboardNavbar.vue';
  import ContentFooter from './ContentFooter.vue';
  import MainContent from './Content.vue';
  import SideBar from '@/components/SidebarPlugin/SideBar.vue';
  import SidebarItem from '@/components/SidebarPlugin/SidebarItem.vue';

  export default {
    components: {
      DashboardNavbar,
      ContentFooter,
      MainContent,
      SideBar,
      SidebarItem,
    },
    methods: {
      initScrollbar() {
        let isWindows = navigator.platform.startsWith('Win');
        if (isWindows) {
          initScrollbar('sidenav');
        }
      }
    },
    mounted() {
      this.initScrollbar()
    }
  };
</script>

<style lang="scss">
</style>
