<template>
  <div>
    <div v-if="!loading">
      <div class="order" v-for="order in cancel_orders.reverse()" :key="order.id">
        <a :href="'/order/canceled/' + order.id">
          <div class="row-one">
            <div class="title">{{ order.proficiency.title }}</div>

            <div class="price">{{ parseInt(order.budget) }} تومان</div>
          </div>
          <div class="row-two">
            <div class="date">
              {{
                momentJ(order.start_at)
                  .locale("fa")
                  .format("dddd D jMMMM YYYY ساعت HH:mm")
              }}
            </div>
          </div>
        </a>
      </div>
    </div>
    <div v-else>
      <img class="loading" src="../../../../assets/loading.svg" alt="loading" />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "CanceledTab",
  mounted() {
    this.fetchOrders();
  },
  methods: {
    fetchOrders() {
      Axios.get(this.$hostname + "/canceled-orders", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.cancel_orders = resp.data.orders;
        })
        .catch((err) => {
          console.log(err, "can not fetch canceled orders");
        });
    },
  },
  data() {
    return {
      cancel_orders: [],
      loading: true,
      momentJ: momentJ,
    };
  },
};
</script>

<style scoped>
img.loading {
  width: 70px;
  height: 70px;
  margin: 0 auto;
}
a {
  text-decoration: none;
  color: #2c3e50;
}
.order {
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  margin-bottom: 10px;
  border: 2px solid transparent;
  height: 120px;
  transition: 0.4s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: 18px;
  cursor: pointer;
}
.order:hover {
  border: 2px solid #5c438a;
  transition: 0.4s ease;
}
.order .row-one,
.order .row-two {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.order .row-one .title {
  color: #5c438a;
  font-size: 22px;
}
.order .row-two .date {
  background-image: url("../../../../assets/Tasks/Event.svg");
  background-repeat: no-repeat;
  background-size: 20px;
  background-position: right;
  padding-right: 33px;
}
@media screen and (max-width: 540px) {
  .order {
    padding: 10px;
    height: 100px;
    font-size: 0.9rem;
  }
  .order .row-one .title {
    font-size: 1rem;
  }
}
</style>
