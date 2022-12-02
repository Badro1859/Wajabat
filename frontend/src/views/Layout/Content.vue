<template>
  <div class="content">
    <FadeTransition :duration="200" origin="center top" mode="out-in">
      <!-- your content here -->
      <router-view></router-view>
    </FadeTransition>
  </div>
</template>

<script>
import { FadeTransition } from 'vue2-transitions';
export default {
  name: 'main-content',
  components: {
    FadeTransition
  }
};
</script>

<style></style>
