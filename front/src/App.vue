<template>
  <div>
    <Navbar />

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }"> 
    <div class="lds-dual-ring"> </div>
    </div>
    
    <section class="section">
      <router-view/>
    </section>
  </div>  
</template>


<script>
import axios from 'axios'

  import Navbar from '@/components/layout/Navbar'
  export default {
    name: 'App',
    components: {
      Navbar
    },

    beforeCreate() {
      this.$store.commit('initializeStore')

      if (this.$store.state.token) {
        axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
      } else {
        axios.defaults.headers.common['Authorization'] = ""

      }
    }
}
</script>
<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
</style>
