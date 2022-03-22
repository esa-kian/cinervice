<template>
  <div class="body">
    <v-card
      v-for="product in products"
      :key="product._id"
      :loading="loading"
      class="mx-auto my-12"
      max-width="374"
    >
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>

      <v-img height="250" :src="public_url + 'productImage.jpg'"></v-img>

      <v-card-title>{{ product.name }}</v-card-title>

      <v-card-text>
        <v-row align="center" class="mx-0">
          <v-rating
            :value="5"
            color="amber"
            dense
            half-increments
            readonly
            size="18"
          ></v-rating>

          <div class="grey--text ms-4">موجودی: {{ product.number }}</div>
        </v-row>

        <div class="my-4 text-subtitle-1">
          <s> {{ product.price }}تومان </s> •
          {{ product.priceWithDiscount }}تومان
        </div>

        <div>
          {{ product.description }}
        </div>
      </v-card-text>

      <v-divider class="mx-4"></v-divider>

      <v-card-title
        >فروشنده:
        {{
          product.seller.firstName + " " + product.seller.lastName
        }}</v-card-title
      >

      <v-card-actions>
        <v-btn
          color="deep-purple lighten-2"
          text
          @click="reserve(product._id, true)"
        >
          <v-icon dark> mdi-cart </v-icon>
          افزودن به سبد خرید
        </v-btn>
        <v-btn
          color="deep-purple lighten-2"
          text
          @click="reserve(product._id, false)"
        >
          <v-icon dark> mdi-delete </v-icon>
          حذف از سبد خرید
        </v-btn>
      </v-card-actions>
      <v-card-actions>
        <v-btn
          color="deep-purple lighten-2"
          text
          @click="quantity(product._id, true)"
        >
          تعداد <v-icon dark> mdi-plus </v-icon>
        </v-btn>
        <v-btn
          color="deep-purple lighten-2"
          text
          @click="quantity(product._id, false)"
        >
          <v-icon dark> mdi-minus </v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>


<script>
export default {
  data: () => ({
    loading: false,
    selection: 1,
    products: [],
    public_url: "",
  }),
  mounted() {
    this.fetch();
    this.public_url = this.$public_url;
  },
  methods: {
    fetch() {
      this.$http
        .get(this.$hostname + "/products")
        .then((resp) => {
          console.log(resp.data);
          this.products = resp.data.items;
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    reserve(product, action) {
      this.loading = true;
      let data = {
        operation: action,
        number: 1,
        product: product,
      };
      this.$http
        .post(
          this.$hostname + "/customer/editproductfromcart",
          data,
          this.$config
        )
        .then((resp) => {
          console.log(resp);
          this.fetch();
        })
        .catch((err) => {
          console.log(err.response);
        });
      setTimeout(() => (this.loading = false), 2000);
    },
    quantity(product, action) {
      this.loading = true;

      this.$http
        .put(
          this.$hostname +
            "/customer/changequantity?id=" +
            product +
            "&operation=" +
            action,
          this.$config
        )
        .then((resp) => {
          console.log(resp.data);
          this.fetch();
        })
        .catch((err) => {
          console.log(err.response);
        });
      setTimeout(() => (this.loading = false), 2000);
    },
  },
};
</script>
<style scoped>
.body {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: flex-start;
  width: 100%;
}
</style>