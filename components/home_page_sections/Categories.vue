<template>
  <div class="container">
    <Navbar />

    <div class="cats">
      <div class="head">
        <div class="title">سرویس مورد نظر خود را جستجو کنید.</div>
        <div class="search">
          <form class="search">
            <div class="form-group">
              <div class="filter-search">
                <select class="filter-search">
                  <option
                    v-for="city in cities"
                    :key="city.id"
                    :value="city.id"
                  >
                    {{ city.title }}
                  </option>
                </select>
              </div>
              <input
                type="text"
                placeholder="جستجو در دسته‌بندی‌ها ، مانند : کولر"
                v-model="keyword"
                @input="search(keyword)"
              />
              <button @click.prevent="search(keyword)">جستجو</button>
            </div>
          </form>
        </div>
      </div>
      <div v-if="!loading" class="cat-cards">
        <div
          @click.prevent="newRequest(category.id, category.title)"
          v-for="category in categories"
          :key="category.id"
          class="cat-card"
        >
          <div class="icon" :id="'cat_' + category.id"></div>
          <div class="title">{{ category.title }}</div>
        </div>
      </div>
      <div v-else>
        <img class="loading" src="../../assets/loading.svg" alt="loading" />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "../Navbar";
import Footer from "../Footer";

export default {
  name: "Categories",
  components: {
    Navbar,
    Footer,
  },
  mounted() {
    this.fetchCities();
    this.fetchAllCategories();
  },
  methods: {
    fetchAllCategories() {
      Axios.get(this.$hostname + "/proficiencies")
        .then((resp) => {
          this.loading = false;
          this.categories = resp.data.proficiencies;
        })
        .catch((err) => {
          console.log(err, "can not fetch account data");
        });
    },
    newRequest(category_id, category_title) {
      localStorage.setItem("proficiency", category_id);
      localStorage.setItem("proficiency_title", category_title);
      this.$router.push("/new_request");
    },
    search(keyword) {
      this.loading = true;

      if (keyword) {
        Axios.get(this.$hostname + "/search-skills?keyword=" + keyword)
          .then((resp) => {
            this.loading = false;
            this.categories = resp.data.categories;
          })
          .catch((err) => {
            console.log(err, "can not fetch data");
          });
      } else {
        this.fetchAllCategories();
      }
    },
    fetchCities() {
      Axios.get(this.$hostname + "/cities")
        .then((resp) => {
          this.cities = resp.data.cities;
        })
        .catch((err) => {
          console.log(err, "can not fetch cities");
        });
    },
  },
  data() {
    return {
      categories: [],
      loading: true,
      cities: null,
      keyword: null,
    };
  },
};
</script>

<style scoped>
@import url("bootstrap/dist/css/bootstrap.css");
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  padding: 0;
  background-color: #f8f5fc;
  height: auto;
}
img.loading {
  width: 70px;
  height: 70px;
  margin: 200px auto;
}
.cats {
  width: 100%;
  padding: 110px 10% 50px 10%;
  margin: 0px 0px 0px 0px;
  height: auto;
}
.head {
  display: flex;
  justify-content: space-between;
}
.form-group {
  display: flex;
  padding: 0;
  margin-bottom: 0;
}
.head .title,
.head .search {
  display: flex;
}

.head .title {
  font-size: 1.5rem;
  font-weight: 500;
  color: #5c438a;
}

.head .search {
  border-radius: 5px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
}

div.filter-search {
  border-left: 1px solid #5c438a;
  display: flex;
  margin: 0 20px;
  padding-left: 18px;
}
select.filter-search {
  outline: none;
  appearance: none;
  border: none;
  background-image: url("../../assets/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-y: 20px;
  background-size: 10px;
  cursor: pointer;
  background-color: #fff;
  font-size: 18px;
  font-weight: 300;
  font-family: IRANSans;
  width: 80px;
}
select option {
  background: #fff;
  color: #5c438a;
  width: 100%;
}

form.search .form-group input {
  outline: none;
  border: none;
  width: 280px;
  opacity: 0.8;
}

form.search .form-group button {
  outline: none;
  border: none;
  background-color: #5c438a;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  padding-left: 25px;
  padding-right: 25px;
}

a {
  text-decoration: none !important;
  font-size: 16px;
  font-weight: 500;
  color: #000000;
  opacity: 0.8;
}
a:hover {
  text-decoration: underline !important;
  color: #5c438a !important;
  opacity: 1;
}
.cat-cards {
  width: 100%;
  max-width: 100%;
  display: flex;
  flex-wrap: wrap;
  margin: auto;
  margin-top: 46px;
}

.cat-card {
  display: flex;
  margin: 20px 1%;
  flex-direction: column;
  justify-content: space-between;
}

.cat-card .icon {
  background-size: 100px 100px;
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
  transition: 0.2s ease;
  cursor: pointer;
}

.icon:hover {
  border: 2px solid #5c438a;
  background-size: 110px 110px;
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
  .cats {
    padding: 90px 4% 20px 4%;
  }
  .head {
    flex-direction: column;
  }
  div.search {
    margin-top: 20px;
    width: 45%;
  }
  div.filter-search {
    margin: 0 10px;
    padding-left: 12px;
  }
  select.filter-search {
    background-position-y: 10px;
    font-size: 0.9rem;
    width: 40px;
  }
  form.search .form-group input {
    width: 70%;
  }
  input::placeholder {
    font-size: 0.7rem;
  }
  form.search .form-group button {
    font-size: 0.9rem;
    padding-left: 15px;
    padding-right: 15px;
  }
  .cat-cards {
    justify-content: center;
  }
}
@media screen and (max-width: 540px) {
  .cats {
    padding: 90px 4% 30px 4%;
  }
  .head {
    flex-direction: column;
  }
  .head .title {
    font-size: 1.1rem;
  }
  div.search {
    margin-top: 20px;
  }
  div.filter-search {
    margin: 0 10px;
    padding-left: 12px;
  }
  select.filter-search {
    background-position-y: 10px;
    font-size: 0.9rem;
    width: 40px;
  }
  form.search .form-group input {
    width: 70%;
  }
  input::placeholder {
    font-size: 0.7rem;
  }
  form.search .form-group button {
    font-size: 0.9rem;
    padding-left: 15px;
    padding-right: 15px;
  }
  .cat-cards {
    justify-content: center;
  }
}
</style>