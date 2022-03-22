<template>
  <div class="marquee">
    <div class="req-card" v-for="task in tasks" :key="task.id" @click="modal">
      <div class="header">
        <div class="title">{{ task.proficiency.title }}</div>
        <div class="price">{{ parseInt(task.budget) }} تومان</div>
      </div>
      <div class="details">
        <div class="date">
          <i></i
          >{{
            momentJ(task.start_at)
              .locale("fa")
              .format("dddd D jMMMM YYYY ساعت HH:mm")
          }}
        </div>
        <div class="address">
          <i></i>{{ task.address.city.title + ", " + task.address.town.title }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "LastOrders",
  mounted() {
    this.fetchLastOrders();
  },
  methods: {
    fetchLastOrders() {
      Axios.get(this.$hostname + "/last-orders")
        .then((resp) => {
          this.tasks = resp.data.orders;
        })
        .catch((err) => {
          console.log(err, "can not fetch last orders");
        });
    },
  },
  data() {
    return {
      tasks: [],
      momentJ: momentJ,
    };
  },
};
</script>

<style scoped>
.marquee {
  display: flex;
  position: absolute;
  bottom: 10%;
  left: 0;
  animation: marquee 80s linear infinite;
}

.req-card {
  display: flex;
  height: 150px;
  width: 380px;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  margin: 10px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  border: 2px solid transparent;
  transition: 0.4s ease;
}
@keyframes marquee {
  from {
    transform: translateX(-50%);
  }
  to {
    transform: translateX(min(100vw, 1366px));
  }
}
.req-card:hover {
  border: 2px solid #5c438a;
  cursor: pointer;
  transition: 0.4s ease;
}
.req-card .header {
  display: flex;
  justify-content: space-between;
  color: #5c438a;
  opacity: 0.9;
}
.req-card .header .title {
  font-size: 20px;
  font-weight: bold;
}
.req-card .header .price {
  font-size: 18px;
  font-weight: bold;
}
.req-card .details {
  font-size: 1.07rem;
  font-weight: 500;
  opacity: 0.8;
}
.req-card .details .date {
  display: flex;
  align-items: center;
}
.req-card .details .address {
  display: flex;
  align-items: center;
}
.req-card .details i {
  display: flex;
  justify-content: flex-start;
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
.req-card .details .date i {
  background-image: url("../../assets/Tasks/Event.svg");
}
.req-card .details .address i {
  background-image: url("../../assets/Tasks/Location.svg");
}
@media screen and (max-width: 540px) {
  .req-card {
    height: 120px;
    width: 300px;
    padding: 15px;
  }
}
</style>