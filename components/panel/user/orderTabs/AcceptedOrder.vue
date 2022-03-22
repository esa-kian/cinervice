<template>
  <div class="container">
    <Navbar />
    <div class="accepted">
      <div class="accepted-card">
        <div class="header">
          <div class="title">{{ order.proficiency.title }}</div>
          <div class="budget">
            <div class="caption">مبلغ کل:</div>
            <div class="budget-val">{{ parseInt(order.budget) }} تومان</div>
          </div>
        </div>
        <div class="body">
          <div class="technician">
            <div class="info">
              <div
                class="photo"
                :style="{
                  'background-image': 'url(' + order.technician_picture + ')',
                }"
              ></div>
              <div class="details">
                <div class="name">
                  <a
                    target="_blank"
                    :href="'/technician_profile/' + order.technician_id"
                  >
                    {{ order.technician_name }}
                  </a>
                </div>
              </div>
            </div>

            <div class="buttons">
              <button @click="paymentModal">پرداخت</button>
              <button @click="startChat()">آغاز چت</button>
            </div>
          </div>
          <div class="date">
            <i></i>
            {{ start_at }}
          </div>
          <div class="skills">
            <ul>
              <li v-for="skill in skills" :key="skill.skill_id">
                {{ skill.title }}
              </li>
            </ul>
          </div>
          <div class="detail">
            {{ order.details }}
          </div>
          <div class="address">
            <i></i>
            {{
              order.address.city.title +
              ", " +
              order.address.town.title +
              ", " +
              order.address.description
            }}
          </div>
          <div class="photos">
            <img
              v-for="photo in order.photos"
              :key="photo.id"
              :src="photo.url"
              alt=""
              width="110px"
              height="110px"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Modal payment  -->
    <div id="payment" class="modal">
      <div class="modal-content">
        <div class="header">
          <div class="title">پرداخت</div>
          <span class="closepay"></span>
        </div>
        <div class="content">
          <div class="cost">
            <label for="cost">هزینه سرویس :</label>
            <span>{{ order.budget }}تومان</span>
          </div>
          <div class="tip">
            <label for="tip"
              >درصورت تمایل به پرداخت انعام، مبلغ مورد نظر را وارد
              نمایید.</label
            >
            <input
              type="text"
              name="tip"
              id="tip"
              v-model="tip"
              placeholder="تومان"
              @input="calcTotal"
            />
          </div>
          <div class="total">
            <label for="total">مجموع مبلغ قابل پرداخت :</label>
            {{ total }}تومان
          </div>
          <div class="balance">
            <label for="balance">موجودی :</label>
            <span>{{ balance }}تومان</span>
          </div>
          <div v-if="!loading_pay" class="buttons">
            <button @click="creditPay" v-if="can_pay">پرداخت از کیف پول</button>
            <button @click="creditPay" v-else>افزایش موجودی</button>
            <button @click="cashPay">پرداخت نقدی</button>
          </div>
          <div v-else>
            <img
              class="loading"
              src="../../../../assets/loading.svg"
              alt="loading"
            />
          </div>
        </div>
      </div>
    </div>
    <!-- Modal rate -->

    <div id="rate-modal" class="modal">
      <div class="rate-modal-content">
        <div class="header">
          <div class="title">افزودن نظر</div>
        </div>
        <div class="rate-content">
          <div class="rate">
            <p>به میزان رضایت خود از این متخصص امتیاز دهید.</p>
            <StarRating />
          </div>
          <div class="comment">
            <p>نظرات خود را درباره این متخصص ثبت نمایید.</p>
            <textarea v-model="comment" name="comment" id="comment"></textarea>
          </div>
        </div>
        <div class="buttons submit-comment">
          <button v-if="!loading_comment" @click.prevent="rateAndComment">
            ثبت نظر
          </button>
          <div v-else>
            <img
              class="loading"
              src="../../../../assets/loading.svg"
              alt="loading"
            />
          </div>
        </div>
      </div>
    </div>

    <div class="copyright">
      <Copyright />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "../../../Navbar";
import Copyright from "../../../Copyright";
import StarRating from "../../technician/historyTabs/StarRating";

export default {
  name: "Done",
  components: {
    Navbar,
    Copyright,
    StarRating,
  },
  mounted() {
    this.fetchOrder();
  },
  methods: {
    fetchOrder() {
      Axios.get(this.$hostname + "/accepted-orders/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.order = resp.data.order.detail[0];
          this.start_at = moment(this.order.start_at).format(
            "dddd jD jMMMM jYYYY ساعت HH:mm"
          );
          this.skills = resp.data.order.skills;
          this.cost = resp.data.order.detail[0].budget;
          this.fetchBalance();
        })
        .catch((err) => {
          this.$router.push("/");
        });
    },
    calcTotal() {
      if (this.tip) {
        this.total = parseInt(this.tip) + parseInt(this.cost);
      } else {
        this.total = parseInt(this.cost);
      }
      if (this.balance >= this.total) {
        this.can_pay = true;
      } else {
        this.can_pay = false;
      }
    },
    fetchBalance() {
      Axios.get(this.$hostname + "/balance", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.balance = resp.data.balance;
          this.calcTotal();
        })
        .catch((err) => {
          console.log("can not fetch balance");
        });
    },
    startChat() {
      this.$router.push("/panel/user/5");
    },
    creditPay() {
      if (this.can_pay) {
        this.loading_pay = true;

        let data = {
          payment: this.cost,
          tip: this.tip,
          project_id: this.id,
          technician_id: this.order.technician_id,
        };
        Axios.post(this.$hostname + "/credit-payment", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            let modal = document.getElementById("payment");
            this.show_rate = true;
            this.loading_pay = false;
            modal.style.display = "none";
            this.rateAndCommentModal();
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        this.$router.push("/panel/user/3");
      }
    },
    cashPay() {
      let data = {
        payment: this.cost,
        project_id: this.id,
        technician_id: this.order.technician_id,
      };
      this.loading_pay = true;
      Axios.post(this.$hostname + "/cash-payment", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          let modal = document.getElementById("payment");
          this.show_rate = true;
          this.loading_pay = false;
          modal.style.display = "none";
          this.rateAndCommentModal();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    rateAndComment() {
      this.loading_comment = true;

      let data = {
        vote: localStorage.vote,
        comment: this.comment,
        project_id: this.id,
        technician_id: this.order.technician_id,
      };
      Axios.post(this.$hostname + "/rate-comment/client", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          localStorage.removeItem("vote");
          this.show_rate = false;
          this.loading_comment = false;
          this.$router.push("/panel/user/2");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    paymentModal() {
      let modal = document.getElementById("payment");

      // Get the <span> element that closes the modal
      let span = document.getElementsByClassName("closepay")[0];

      // When the user clicks the button, open the modal

      modal.style.display = "block";

      // When the user clicks on <span> (x), close the modal
      span.onclick = function () {
        modal.style.display = "none";
      };

      // When the user clicks anywhere outside of the modal, close it
      window.onclick = function (event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
      };
    },
    rateAndCommentModal() {
      let modal = document.getElementById("rate-modal");

      // When the user clicks the button, open the modal

      modal.style.display = "block";
    },
  },
  props: {
    id: null,
  },
  data() {
    return {
      order: null,
      skills: [],
      bids: [],
      comments: [],
      total: null,
      const: null,
      tip: null,
      can_pay: null,
      balance: null,
      show_rate: false,
      comment: null,
      start_at: null,
      loading_pay: false,
      loading_comment: false,
    };
  },
};
</script>

<style scoped>
img.loading {
  width: 40px;
  height: 40px;
  margin: 0 auto;
}
.copyright {
  padding: 0 11.5%;
}
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  background-color: #f8f5fc;
  height: auto;
}
.accepted {
  width: 100%;
  max-width: 1366px;
  height: 850px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
}

.accepted .accepted-card {
  height: auto;
  padding: 20px 20px 30px;
  display: flex;
  flex-direction: column;
  position: absolute;
  align-content: space-between;
  background-color: #fff;
  width: 58%;
  max-width: 800px;
  border-radius: 5px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.header {
  display: flex;
  justify-content: space-between;
}
.header .title {
  font-size: 24px;
  font-weight: bold;
  color: #5c438a;
}
.header .budget {
  border-radius: 5px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  color: #000;
  padding: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: 500;
  width: 250px;
}
.body .technician {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  margin: 30px 0;
}
.body .technician .info {
  display: flex;
  align-items: center;
}
.body .technician .info .photo {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 120px;
  height: 120px;
  border: 1px solid #5c438a17;
  border-radius: 60px;
}
.body .technician .info .details {
  margin-right: 20px;
  font-size: 20px;
  line-height: 40px;
  font-weight: bold;
}
a {
  color: #000;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
.body .technician .info .details .skill {
  color: #5c438a;
}
.buttons {
  display: flex;
  flex-wrap: wrap;
  width: 50%;
  justify-content: space-between;
}
.body .technician .buttons button {
  background-color: #fff;
  border: 2px solid #5c438a;
  height: 50px;
  padding: 0 40px;
  margin-top: 10px;
  width: 48%;
  outline: none;
  cursor: pointer;
  justify-content: center;
  border-radius: 5px;
  color: #5c438a;
  font-size: 18px;
  font-weight: 500;
  transition: 0.4s ease;
  font-family: IRANsans;
}
.body .technician .buttons button:hover {
  background-color: #5c438a;
  color: #fff;
  transition: 0.4s ease;
}
.body .date {
  font-size: 18px;
  font-weight: 500;
}
ul {
  display: flex;
}
ul li {
  justify-content: space-between;
  margin-left: 30px;
  display: list-item;
}

::marker {
  color: #5c438a;
  font-size: 24px;
  display: flex;
  justify-content: flex-start;
  margin: 0 !important;
  padding: 0 !important;
}
.detail {
  margin-top: 10px;
  display: list-item;
  margin-right: 30px;
}
.body .address {
  margin-top: 20px;
}
.photos {
  display: flex;
  justify-content: center;
  margin: 5px;
  flex-wrap: wrap;
}
.photos img {
  margin-left: 10px;
  border: 2px dashed #5c438a42;
  padding: 2px;
  outline: none;
}
.body .photos img {
  display: flex;
}
.address {
  display: flex;
  justify-content: flex-start;
  margin: 20px 0;
}
.address i {
  background-image: url("../../../../assets/Tasks/Location.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
.date {
  display: flex;
  justify-content: flex-start;
  margin: 20px 0;
}
.date i {
  background-image: url("../../../../assets/Tasks/Event.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
/* Modal payment style */

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

.modal-content {
  background-color: #fefefe;
  margin: 0 auto;
  width: 40%; /* Full width */
  height: 390px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.modal-content .header,
.rate-modal-content .header {
  display: flex;
  justify-content: center;
  padding: 10px 10px;
  border-bottom: solid 1px #5c438a36;
}
.modal .title {
  margin: auto;
}
.closepay,
.closerate {
  display: flex;
  justify-self: flex-end;
  background-image: url("../../../../assets/close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  cursor: pointer;
}
.modal .content {
  height: 300px;
}
.modal .content div {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  align-items: center;
  border-bottom: solid 1px #5c438a36;
  width: 95%;
  margin: auto;
  font-size: 14px;
  height: 58px;
}
.modal .content input {
  outline: none;
  border: none;
  text-align: left;
  margin-top: 10px;
  font-family: IRANsans;
  transition: 0.4s ease;
  background-color: transparent;
  width: 25%;
}
.modal .content .balance {
  border-radius: 5px;
  background-color: #5c438a15;
  padding-right: 50px;
  background-image: url("../../../../assets/panel/purple/Wallet.svg");
  background-repeat: no-repeat;
  background-position-x: right;
  background-position-y: center;
  background-size: 40px;
  border-bottom: none !important;
}
.modal .content input:focus {
  border-bottom: 2px solid #5c438a;
  transition: 0.4s ease;
}

.modal-content .total {
  border-bottom: none !important;
}

.modal-content .buttons {
  display: flex;
  flex-wrap: wrap;
  width: 80% !important;
  justify-content: space-between;
  border-bottom: none !important;
}
.modal-content .buttons button {
  background-color: #fff;
  border: 2px solid #5c438a;
  height: 40px;
  padding: 0 30px;
  margin: 20px 0;
  width: 48%;
  outline: none;
  cursor: pointer;
  justify-content: center;
  border-radius: 5px;
  color: #5c438a;
  font-size: 16px;
  font-weight: 500;
  transition: 0.4s ease;
  font-family: IRANsans;
}
.rate-modal-content .buttons button {
  background-color: #fff;
  border: 2px solid #5c438a;
  height: 50px;
  padding: 0 30px;
  margin: 20px 0;
  width: 30%;
  outline: none;
  cursor: pointer;
  justify-content: center;
  border-radius: 5px;
  color: #5c438a;
  font-size: 16px;
  font-weight: 500;
  transition: 0.4s ease;
  font-family: IRANsans;
}
.modal-content button:hover,
.rate-modal-content button:hover {
  background-color: #5c438a;
  color: #fff;
  transition: 0.4s ease;
}
.comment,
.rate {
  width: 94% !important;
  margin: 10px 20px;
}
.rate {
  display: flex;
  justify-content: space-between;
}
.comment p,
.rate p {
  padding: 0 !important;
  margin: 10px 0;
  display: flex;
  justify-content: space-between;
  width: 60%;
}
textarea {
  height: 194px;
  width: 100%;
  padding: 10px;
  opacity: 0.2;
  border-radius: 5px;
  outline: none;
  border: solid 1px #5c438a;
  resize: none;
  transition: 0.4s ease;
  font-family: IRANsans;
}
textarea:focus {
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  opacity: 1;
  transition: 0.4s ease;
}
.rate-modal-content {
  background-color: #fefefe;
  margin: 0 auto;
  width: 50%; /* Full width */
  height: 458px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.rate-content {
  height: 400px;
}
.submit-comment {
  justify-content: center !important;
  width: 100% !important;
  margin: auto;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .accepted {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }

  .accepted .accepted-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }
  .copyright {
    padding: 0 4%;
  }
}
@media screen and (max-width: 540px) {
  .accepted {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }

  .accepted .accepted-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }
  .header {
    flex-direction: column;
  }
  .copyright {
    padding: 0 4%;
  }
  .body .technician {
    flex-direction: column;
  }
  ul {
    display: block;
  }
  .address i {
    background-repeat: no-repeat;
    background-size: contain;
    width: 30px;
    height: 20px;
  }
  .photos {
    flex-direction: column;
    align-items: center;
  }
  .body .photos img {
    margin-top: 10px;
  }
  .header .budget {
    margin-top: 20px;
  }
  .buttons {
    width: 100%;
  }
  .modal-content {
    width: 90%;
  }
  .modal-content .buttons {
    width: 100%;
    align-items: center;
    flex-direction: column;
  }
  .modal-content .buttons button {
    margin: 10px 0;
    width: 90%;
  }
}
</style>
