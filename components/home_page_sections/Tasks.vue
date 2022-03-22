<template>
  <div>
    <Navbar />
    <div class="requests">
      <div class="head">
        <div class="title">درخواست‌های جاری</div>
      </div>
      <div v-if="!loading" class="req-cards">
        <div
          class="req-card"
          v-for="task in tasks"
          :key="task.id"
          @click="modal"
        >
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
              <i></i
              >{{ task.address.city.title + ", " + task.address.town.title }}
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <img class="loading" src="../../assets/loading.svg" alt="loading" />
      </div>
      <Copyright />
    </div>
    <!-- Modal Task Error -->
    <div id="error" class="modal">
      <div class="modal-content-error">
        <div class="closeerror">
          <span class="closeerror">&times;</span>
        </div>
        <div class="content">
          <div class="forbidden"></div>
          <p>
            جهت حفظ حریم خصوصی کاربران،نمایش محتویات درخواست‌ها تنها برای
            متخصصین امکان‌پذیر میباشد.
          </p>
          <button class="accepterror">تأیید</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "../Navbar";
import Copyright from "../Copyright";
import momentJ from "jalali-moment";

export default {
  name: "Tasks",
  components: {
    Navbar,
    Copyright,
  },
  mounted() {
    this.fetchTasks();
  },

  methods: {
    fetchTasks() {
      Axios.get(this.$hostname + "/tasks")
        .then((resp) => {
          this.loading = false;
          this.tasks = resp.data.tasks;
        })
        .catch((err) => {
          console.log(err, "can not fetch tasks");
        });
    },
    modal() {
      let modal = document.getElementById("error");

      // Get the <span> element that closes the modal
      let span = document.getElementsByClassName("closeerror")[0];
      let accept = document.getElementsByClassName("accepterror")[0];

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
  },
  data() {
    return {
      tasks: [],
      loading: true,
      momentJ: momentJ,
    };
  },
};
</script>

<style scoped>
@import url("bootstrap/dist/css/bootstrap.css");
.requests {
  width: 100%;
  max-width: 1366px;
  padding: 110px 11.5% 50px 11.5%;
  margin: auto;
  background-color: #f8f5fc;
  height: auto;
}
img.loading {
  width: 70px;
  height: 70px;
  margin: 0 auto;
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
.head .title {
  display: flex;
}

.head .title {
  font-size: 1.4rem;
  font-weight: 500;
  color: #5c438a;
}

.req-cards {
  flex-wrap: wrap;
  padding-top: 46px;
  display: flex;
  align-content: center;
  justify-content: flex-start;
}

.req-card {
  display: flex;
  margin: 10px 1%;
  height: 150px;
  width: 31%;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  border: 2px solid transparent;
  transition: 0.4s ease;
}

.req-card:hover {
  border: 2px solid #5c438a;
  cursor: pointer;
  transition: 0.4s ease;
}

.req-cards .req-card .header {
  display: flex;
  justify-content: space-between;
  color: #5c438a;
  opacity: 0.9;
}

.req-cards .req-card .header .title {
  font-size: 1.2rem;
  font-weight: bold;
}
.req-cards .req-card .header .price {
  font-size: 1rem;
  font-weight: bold;
}

.req-cards .req-card .details {
  font-size: 1rem;
  font-weight: 500;
  opacity: 0.8;
}

.req-cards .req-card .details .date {
  display: flex;
  align-items: center;
}
.req-cards .req-card .details .address {
  display: flex;
  align-items: center;
}
.req-cards .req-card .details i {
  display: flex;
  justify-content: flex-start;
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
.req-cards .req-card .details .date i {
  background-image: url("../../assets/Tasks/Event.svg");
}
.req-cards .req-card .details .address i {
  background-image: url("../../assets/Tasks/Location.svg");
}
/* Modal Task Error style */
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
  background-color: rgba(92, 67, 138, 0.25); /* Black w/ opacity */
}

/* Modal Content */
.modal-content-error {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 43%; /* Full width */
  height: 320px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.modal-content-error .content {
  display: flex;
  flex-direction: column;
  align-items: center;
}
/* The Close Button */
.closeerror {
  color: #5c438a;
  float: left;
  font-weight: lighter;
  font-size: 32px;
}

.closeerror:hover,
.closeerror:focus {
  color: #5c438a;
  text-decoration: none;
  cursor: pointer;
  align-items: flex-end;
}
.forbidden {
  background-image: url("../../assets/forbidden.svg");
  display: flex;
  margin: 20px;
  background-repeat: round;
  width: 100px;
  height: 100px;
}
button.accepterror {
  background-color: #5c438a;
  padding: 9px 61px 7px;
  border-radius: 10px;
  border: none;
  outline: none;
  font-size: 16px;
  font-weight: bold;
  width: 150px;
  color: #fff;
  height: 40px;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .requests {
    padding: 80px 3% 0px 3%;
  }
  .req-cards {
    justify-content: center;
    padding-top: 20px;
  }
  .req-card {
    width: 48%;
  }

  .modal-content-error {
    width: 70%;
  }
}
@media screen and (max-width: 540px) {
  .requests {
    padding: 80px 4% 0px 4%;
  }
  .req-cards {
    flex-direction: column;
    padding-top: 20px;
  }
  .req-card {
    width: 100%;
  }

  .modal-content-error {
    width: 90%;
  }
}
</style>