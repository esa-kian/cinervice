<template>
  <div>
    <div class="main">
      <div class="title">
        بر اساس سرویس انتخابی ، ممکن است به موارد زیر نیاز داشته باشید.
      </div>
      <div class="cards">
        <img
          v-if="loading"
          class="loading"
          src="../../assets/loading.svg"
          alt="loading"
        />
        <div v-for="product in products" :key="product.id" class="card">
          <button @click.prevent="setProducts(product.id)" class="add-cart">
            <div v-if="selected_products.length > 0">
              <div v-for="id in selected_products" :key="id">
                <div v-if="id === product.id">حذف</div>
                <div v-else-if="id !== product.id"></div>
                <div v-else>افزودن به درخواست</div>
              </div>
            </div>
            <div v-else>افزودن به درخواست</div>
            <span id="add"></span>
          </button>
          <div
            class="image"
            :style="{
              'background-image': 'url(' + product.picture + ')',
            }"
          ></div>
          <div class="title">{{ product.title }}</div>
          <div class="price">{{ parseInt(product.price) }} تومان</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "StepSeven",
  mounted() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
      Axios.get(this.$hostname + "/products?skills=" + localStorage.skills)
        .then((resp) => {
          this.loading = false;
          this.products = resp.data.products;
        })
        .catch((err) => {
          console.log(err, "can not fetch products");
        });
    },
    setProducts(product) {
      let products_local = [];

      const index = this.selected_products.indexOf(product);

      if (index !== -1) {
        this.selected_products.splice(index, 1);
        products_local.splice(index, 1);
      } else {
        this.selected_products.push(product);
        products_local.push(product);
      }
      localStorage.setItem("products", this.selected_products);
    },
  },
  data() {
    return {
      products: null,
      selected_products: [],
      loading: true,
    };
  },
};
</script>

<style scoped>
.cards {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: scroll;
  max-width: 590px;
  padding-bottom: 20px;
}
.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  height: 233px;
  width: 290px;
  min-width: 290px;
  margin-top: 20px;
  margin-left: 10px;
  font-size: 14px;
  transition: 0.4s ease;
}
img.loading {
  width: 100px;
  height: 100px;
  margin: 0 auto;
}
.card:hover {
  background-color: rgba(0, 0, 0, 0.1);
  transition: 0.4s ease;
}
.card:hover .image,
.card:hover .price,
.card:hover .title {
  filter: blur(1.5px) brightness(90%);
  transition: 0.4s ease;
}
button.add-cart {
  opacity: 0;
  position: absolute;
  z-index: 999;
  transition: 0.4s ease;
  background-color: #fff;
  border: 2px solid #5c438a;
  margin: 0 15px;
  width: 30%;
  outline: none;
  cursor: pointer;
  justify-content: center;
  border-radius: 5px;
  color: #5c438a;
  font-size: 14px;
  font-weight: 500;
  padding: 10px 15px;
  font-family: IRANsans;
}
button:hover {
  background-color: #5c438a;
  color: #fff;
  transition: 0.4s ease;
}
.card:hover button {
  opacity: 1;
  transition: 0.4s ease;
}
.card .image {
  background-image: url("../../assets/taj.jpg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  width: 100%;
  height: 130px;
  transition: 0.4s ease;
}
.price {
  margin-top: 10px;
  font-weight: bold;
}
@media screen and (max-width: 540px) {
  .title {
    font-size: 1rem;
  }
  .card .title {
    text-align: center;
    font-size: 0.9rem;
  }
}
</style>