<template>
  <hooper
    :centerMode="true"
    :rtl="true"
    :itemsToShow="1"
    :infiniteScroll="true"
    :wheelControl="false"
    :autoPlay="true"
    :playSpeed="3000"
  >
    <slide v-for="technician in technicians" :key="technician.id">
      <div class="cart">
        <div class="detail">
          <div class="name">
            {{ technician.first_name + " " + technician.last_name }}
          </div>
          <div class="skill">{{ technician.proficiency }}</div>
          <div class="rate">
            <div class="point">{{ technician.rate.substring(0, 3) }}</div>
            <div class="votes">(از {{ technician.votes }} رأی)</div>
          </div>
        </div>
        <div
          class="photo"
          :style="{
            'background-image':
              'url(' + public_route + technician.profile_picture + ')',
          }"
        ></div>
      </div>
    </slide>

    <hooper-navigation slot="hooper-addons"></hooper-navigation>
    <hooper-pagination slot="hooper-addons"></hooper-pagination>
  </hooper>
</template>

<script>
import Axios from "axios";
import {
  Hooper,
  Slide,
  Progress as HooperProgress,
  Pagination as HooperPagination,
  Navigation as HooperNavigation,
} from "hooper";
import "hooper/dist/hooper.css";

export default {
  name: "Slider",
  components: {
    Hooper,
    Slide,
    HooperPagination,
    HooperNavigation,
  },
  mounted() {
    this.fetchTechnicians();
  },
  methods: {
    fetchTechnicians() {
      Axios.get(this.$hostname + "/vip-technicians")
        .then((resp) => {
          this.technicians = resp.data.technicians;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      public_route: this.$public_backend,
      technicians: [],
    };
  },
};
</script>
<style scoped>
.hooper {
  width: 43% !important;
  height: 280px !important;
}

.hooper-pagination {
  bottom: -33px;
}
.photo {
  background-image: url("../../assets/Home/service_man.png");
  background-position: left;
  background-repeat: no-repeat;
  background-size: contain;
  width: 50%;
  height: 100%;
}
.cart {
  border-radius: 20px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  width: 100% !important;
  height: 100%;
  display: flex;
  justify-content: space-between;
}
.detail {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 50%;
}
.detail .name {
  font-size: 1.2rem;
  font-weight: bold;
}
.detail .skill {
  font-size: 1.1rem;
}
.detail .rate {
  display: flex;
  background-image: url("../../assets/panel/stars/fill.svg");
  background-position: right;
  background-repeat: no-repeat;
  background-size: contain;
  padding-right: 13%;
}
.detail .point {
  font-size: 0.9rem;
}
.detail .votes {
  font-size: 0.8rem;
  color: rgba(0, 0, 0, 0.5);
}


@media screen and (max-width: 540px) {
  .hooper {
    width: 100% !important;
  }
  .hooper-pagination {
    bottom: -23px;
  }
}
</style>