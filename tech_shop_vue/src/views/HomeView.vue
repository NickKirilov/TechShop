<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to TechShop!
        </p>
        <p class="subtitle">
          Best quality for best price!
        </p>
      </div>
    </section>

    <div class="column is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <div class="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail" alt="product thumbnail">
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">{{ product.price }} lv.</p>

          View Details
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: [],
    }
  },
  components: {
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts(){
      axios
         .get('/api/v1/latest-products/')
         .then(response => {
           this.latestProducts = response.data
         })
         .catch(err => {
           console.log(err)
         })
    }
  }

}
</script>

<style scoped>
  .image {
    margin: -1.25rem -1.25rem 0 -1.25rem;
  }
</style>
