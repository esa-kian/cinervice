<template>
  <div>
    <div v-if="!loading">
      <div
        class="order"
        v-for="order in current_orders.reverse()"
        :key="order.id"
      >
        <a
          :href="[
            order.client_status == 'current'
              ? '/order/current/' + order.id
              : '/order/accepted/' + order.id,
          ]"
        >
          <div class="row-one">
            <div class="title-offer">
              <div class="title">{{ order.proficiency.title }}</div>
              <div class="offer">
                <div v-if="order.client_status == 'current'">
                  ({{ order.bids_count }} پیشنهاد)
                </div>
                <div v-else-if="order.client_status == 'accepted'">
                  (تخصیص یافته)
                </div>
              </div>
            </div>
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
            <a href="#" @click.prevent="cancelOrderModal(order.id)"
              >لغو درخواست</a
            >
          </div>
        </a>
      </div>
    </div>
    <div v-else>
      <img class="loading" src="../../../../assets/loading.svg" alt="loading" />
    </div>
    <!-- Modal Cancel Order -->
    <div id="current" class="modal">
      <div class="modal-content">
        <div class="header">
          <div class="title">لغو درخواست</div>
          <span class="closecurrent"></span>
        </div>
        <div class="content">
          <div class="logout-icon"></div>
          <p>آیا از لغو درخواست خود اطمینان دارید؟</p>
          <div class="yes-no">
            <button class="acceptcurrent">خیر</button>
            <button @click="cancel(wanna_cancel)" class="acceptcurrent">
              بله
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "CurrentTab",
  mounted() {
    this.fetchOrders();
  },
  methods: {
    fetchOrders() {
      Axios.get(this.$hostname + "/current-orders", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.current_orders = resp.data.orders;
        })
        .catch((err) => {
          console.log(err, "can not fetch current orders");
        });
    },
    cancelOrderModal(project_id) {
      this.wanna_cancel = project_id;
      let modal = document.getElementById("current");

      // Get the <span> element that closes the modal
      let span = document.getElementsByClassName("closecurrent")[0];
      let accept = document.getElementsByClassName("acceptcurrent")[0];

      // When the user clicks the button, open the modal

      modal.style.display = "block";

      // When the user clicks on <span> (x), close the modal
      span.onclick = function () {
        modal.style.display = "none";
      };
      accept.onclick = function () {
        modal.style.display = "none";
      };

      // When the user clicks anywhere outside of the modal, close it
      window.onclick = function (event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
      };
    },
    cancel(project_id) {
      let data = {
        project_id: project_id,
      };
      Axios.patch(this.$hostname + "/cancel-order", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.fetchOrders();

          let modal = document.getElementById("current");

          modal.style.display = "none";
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      wanna_cancel: null,
      acceptted_orders: [],
      current_orders: [],
      momentJ: momentJ,
      loading: true,
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
.row-two a {
  text-decoration: none;
  color: #000;
}
.row-two a:hover {
  text-decoration: underline;
  color: #5c438a;
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
.order .row-one .title-offer {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}
.order .row-one .title-offer .title {
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

/* Modal Cancel Order style */
/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgba(92, 67, 138, 0.25); /* Fallback color */
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  border: 1px solid #888;
  width: 33%; /* Full width */
  height: 330px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  justify-content: center;
  flex-direction: column;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.modal-content .content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 245px;
}
.modal-content .content p {
  font-size: 16px;
  margin-top: 0;
}
/* The Close Button */
.header {
  display: flex;
  color: #000;
  font-size: 22px;
  font-weight: 500;
  justify-content: space-between;
  align-items: center;
  border-bottom: solid 2px #5c438a18;
  padding-bottom: 15px;
}
.header .title {
  display: flex;
  justify-self: center;
  align-self: flex-end;
  margin: 0 auto;
}
.closecurrent {
  display: flex;
  justify-self: flex-end;
  background-image: url("../../../../assets/close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  margin-left: 3%;
}
.closecurrent:hover {
  cursor: pointer;
}
.logout-icon {
  background-image: url("../../../../assets/panel/purple/warning.svg");
  display: flex;
  margin: 30px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 100px;
  height: 100px;
}
.yes-no {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  align-items: center;
  width: 60%;
}
button.acceptcurrent {
  background-color: #fff;
  border-radius: 5px;
  border: 2px solid #5c438a;
  outline: none;
  font-size: 16px;
  font-weight: bold;
  width: 150px;
  color: #5c438a;
  height: 40px;
  width: 40%;
  cursor: pointer;
  transition: 0.4s ease;
}
button.acceptcurrent:hover {
  background-color: #5c438a;
  color: #fff;
  transition: 0.4s ease;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .modal {
    z-index: 999;
  }
  .modal-content {
    width: 75%;
  }
}
@media screen and (max-width: 540px) {
  .order {
    padding: 10px;
    min-height: 120px;
    font-size: 0.9rem;
  }
  .order .row-one,
  .order .row-two {
    flex-direction: column;
  }
  .order .row-one .title-offer .title {
    font-size: 1rem;
  }
  .modal {
    z-index: 999;
  }
  .modal-content {
    width: 90%;
  }
}
</style>
