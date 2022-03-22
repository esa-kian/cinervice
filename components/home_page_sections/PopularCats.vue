<template>
  <div class="body">
    <div
      v-for="category in categories"
      :key="category.proficiency.id"
      class="cat-card"
      @click.prevent="
        newRequest(category.proficiency.id, category.proficiency.title)
      "
    >
      <div class="icon" :id="'cat_' + category.proficiency.id"></div>
      <div class="title">{{ category.proficiency.title }}</div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "PopularCats",
  mounted() {
    this.fetchPopularCats();
  },
  methods: {
    fetchPopularCats() {
      Axios.get(this.$hostname + "/popular-categories")
        .then((resp) => {
          this.categories = resp.data.cats;
        })
        .catch((err) => {
          console.log(err, "can not fetch categories");
        });
    },
    newRequest(category_id, category_title) {
      localStorage.setItem("proficiency", category_id);
      localStorage.setItem("proficiency_title", category_title);
      this.$router.push("/new_request");
    },
  },
  data() {
    return {
      categories: [],
    };
  },
};
</script>

<style scoped>
.body {
  width: 100%;
  max-width: 100%;
  flex-wrap: wrap;
  padding-top: 20px;
  display: flex;
  align-content: center;
  flex-direction: row;
  justify-content: space-between;
}

.body .cat-card {
  display: flex;
  margin: 10px 0.1rem;
  flex-direction: column;
  justify-content: space-between;
}

.cat-card .icon {
  background-size: 100px;
  background-repeat: no-repeat;
  background-position: center;
  border: 2px solid transparent;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-content: center;
  padding: 4.5rem;
  border-radius: 10px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  cursor: pointer;
  transition: 0.2s ease;
}

.icon:hover {
  border: 2px solid #5c438a;
  background-size: 120px;
  transition: 0.2s ease;
}

.cat-card .title {
  display: flex;
  justify-content: center;
  margin-top: 10px;
  text-align: center;
  font-size: 14px;
  font-weight: 500;
}
#cat_1 {
  background-image: url("../../assets/Categories/Covid_test.svg");
}
#cat_2 {
  background-image: url("../../assets/Categories/Delivery.svg");
}
#cat_3 {
  background-image: url("../../assets/Categories/Gardening.svg");
}
#cat_4 {
  background-image: url("../../assets/Categories/Electricity.svg");
}
#cat_5 {
  background-image: url("../../assets/Categories/Nursery.svg");
}
#cat_6 {
  background-image: url("../../assets/Categories/Barber_shop.svg");
}
#cat_7 {
  background-image: url("../../assets/Categories/HR.svg");
}
#cat_8 {
  background-image: url("../../assets/Categories/Machanic.svg");
}
#cat_9 {
  background-image: url("../../assets/Categories/Digital_Devices.svg");
}
#cat_10 {
  background-image: url("../../assets/Categories/Health.svg");
}
#cat_11 {
  background-image: url("../../assets/Categories/Pet.svg");
}
#cat_12 {
  background-image: url("../../assets/Categories/Safety.svg");
}
#cat_13 {
  background-image: url("../../assets/Categories/Insurance.svg");
}
#cat_14 {
  background-image: url("../../assets/Categories/Sirens.svg");
}
#cat_15 {
  background-image: url("../../assets/Categories/PC.svg");
}
#cat_16 {
  background-image: url("../../assets/Categories/Sweing_Machine.svg");
}
#cat_17 {
  background-image: url("../../assets/Categories/Renovation.svg");
}
#cat_18 {
  background-image: url("../../assets/Categories/Beauty_salon.svg");
}
#cat_19 {
  background-image: url("../../assets/Categories/HotCold.svg");
}
#cat_20 {
  background-image: url("../../assets/Categories/Wash.svg");
}
#cat_21 {
  background-image: url("../../assets/Categories/Hooman.svg");
}
#cat_22 {
  background-image: url("../../assets/Categories/Carwash.svg");
}
#cat_23 {
  background-image: url("../../assets/Categories/Plumbing.svg");
}
#cat_24 {
  background-image: url("../../assets/Categories/Event.svg");
}
#cat_25 {
  background-image: url("../../assets/Categories/Law.svg");
}
#cat_26 {
  background-image: url("../../assets/Categories/Therapy.svg");
}
#cat_27 {
  background-image: url("../../assets/Categories/Furniture.svg");
}
#cat_28 {
  background-image: url("../../assets/Categories/Cleaning.svg");
}

@media screen and (min-width: 540px) and (max-width: 768px) {
  .body .cat-card {
    margin: 10px 1rem;
  }
}
</style>