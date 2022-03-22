<template>
  <div class="balance-transactions">
    <div class="balance">
      <div class="icon"></div>
      <div class="title">میزان اعتبار شما</div>
      <div class="value">{{ balance }} تومان</div>
      <div class="increase">
        <button @click="balanceIncrease">افزایش موجودی</button>
        <button @click="makeWithdraw" :class="{ deactive: !withdraw }">
          ایجاد درخواست برداشت
        </button>
      </div>
    </div>
    <div class="transactions">
      <div class="title">تراکنش‌ها</div>

      <div class="header">
        <div class="date"></div>
        <div class="type"></div>
        <div class="value"></div>
        <div class="reg-id"></div>
      </div>

      <table v-if="!loading">
        <thead>
          <tr>
            <th>تاریخ</th>
            <th>نوع</th>
            <th>مقدار</th>
            <th>شناسه تراکنش</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transaction in transactions" :key="transaction.id">
            <td>
              {{
                momentJ(transaction.created_at)
                  .locale("fa")
                  .format("dddd D jMMMM YYYY ساعت HH:mm")
              }}
            </td>
            <td v-if="transaction.type === 'tip'">انعام</td>
            <td v-if="transaction.type === 'payment'">پرداخت</td>
            <td v-if="transaction.type === 'deposit'">افزایش موجودی</td>
            <td v-if="transaction.type === 'withdraw'">برداشت</td>
            <td v-if="transaction.type === 'credit'">کسب درآمد</td>
            <td>{{ parseInt(transaction.amount) }}</td>
            <td>{{ transaction.id }}</td>
          </tr>
        </tbody>
      </table>
      <div v-else>
        <img class="loading" src="../../../assets/loading.svg" alt="loading" />
      </div>
    </div>
    <!-- Modal balance increase  -->
    <div id="increase" class="modal-increase">
      <div class="modal-content-increase">
        <div class="header">
          <div class="title">افزایش موجودی</div>
          <span class="closeincrease"></span>
        </div>
        <div class="content">
          <p>مبلغ مورد نظر برای افزایش موجودی را وارد نمایید.</p>
          <div class="yes-no">
            <input v-model="amount" type="text" placeholder="(تومان)" />
            <button class="accept" @click.prevent="deposit">
              انتقال به درگاه پرداخت
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- done deposit modal  -->
    <transition name="fade">
      <div id="doneModal" class="modal" v-if="success_deposit">
        <div class="modal-content">
          <div class="content">
            <div class="done-icon"></div>
            <p>{{ message }}</p>
          </div>
        </div>
      </div>
    </transition>

    <!-- Modal make a withdraw  -->
    <div id="withdraw" class="modal-increase">
      <div class="modal-content-increase">
        <div class="header">
          <div class="title">درخواست برداشت</div>
          <span class="closewithdraw"></span>
        </div>
        <div class="content">
          <p>مبلغ مورد نظر برای برداشت را وارد نمایید.</p>
          <div class="yes-no">
            <input
              v-model="withdraw_amount"
              type="text"
              placeholder="(تومان)"
            />
            <button
              v-if="!loading_withdraw"
              class="accept"
              @click.prevent="submitWithdraw"
            >
              ثبت درخواست برداشت
            </button>
            <div v-else>
              <img
                class="loading"
                src="../../../assets/loading.svg"
                alt="loading"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- done withdraw modal  -->
    <transition name="fade">
      <div id="doneModal" class="modal" v-if="success_withdraw">
        <div class="modal-content">
          <div class="content">
            <div class="done-icon"></div>
            <p>
              درخواست شما با موفقیت ثبت شد. درخواست های ثبت شده بعد از حداکثر ۲۴
              ساعت (به جز ایام تعطیل) تسویه خواهند شد.
            </p>
          </div>
        </div>
      </div>
    </transition>
    <!-- error withdraw modal  -->
    <transition name="fade">
      <div id="errorModal" class="modal" v-if="error">
        <div class="modal-content">
          <div class="content">
            <div class="error-icon"></div>
            <p>{{ error_message }}</p>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "BalanceTransaction",
  mounted() {
    this.init();
  },
  methods: {
    init() {
      this.fetchTransactions();
      this.fetchBalance();
    },
    fetchBalance() {
      Axios.get(this.$hostname + "/balance", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.balance = resp.data.balance;
          localStorage.setItem("balance", this.balance);
          if (this.balance > 100000) {
            this.withdraw = true;
          }
        })
        .catch((err) => {
          console.log("can not fetch balance");
        });
    },
    fetchTransactions() {
      Axios.get(this.$hostname + "/transactions", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.transactions = resp.data.transactions;
        })
        .catch((err) => {
          console.log(err, "can not fetch transactions");
        });
    },
    deposit() {
      let data = {
        amount: this.amount,
      };
      Axios.post(this.$hostname + "/deposit", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          let modal = document.getElementById("increase");
          modal.style.display = "none";
          this.message = resp.data.message;
          this.success_deposit = true;
          setTimeout(() => (this.success_deposit = false), 3000);
          this.init();
        })
        .catch((err) => {
          this.message = err;
        });
    },
    submitWithdraw() {
      this.loading_withdraw = true;
      let data = {
        amount: this.withdraw_amount,
      };
      Axios.post(this.$hostname + "/withdraw-request", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          let modal = document.getElementById("withdraw");
          modal.style.display = "none";
          this.success_withdraw = true;
          this.loading_withdraw = false;
          setTimeout(() => (this.success_withdraw = false), 5000);
        })
        .catch((err) => {
          this.error = true;
          this.error_message = err.response.data.message;
          this.loading_withdraw = false;
          setTimeout(() => (this.error = false), 3000);
        });
    },
    makeWithdraw() {
      if (this.balance < 100000) {
        this.error = true;
        this.error_message = "حداقل موجودی قابل برداشت ۱۰۰،۰۰۰ تومان میباشد";
        setTimeout(() => (this.error = false), 3000);
      } else {
        let modal = document.getElementById("withdraw");

        // Get the <span> element that closes the modal
        let span = document.getElementsByClassName("closewithdraw")[0];

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
      }
    },
    balanceIncrease() {
      let modal = document.getElementById("increase");

      // Get the <span> element that closes the modal
      let span = document.getElementsByClassName("closeincrease")[0];

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
  },
  data() {
    return {
      balance: null,
      transactions: [],
      amount: null,
      message: "",
      success_deposit: false,
      withdraw: false,
      error: false,
      error_message: "",
      show_withdraw: false,
      success_withdraw: false,
      withdraw_amount: null,
      loading: true,
      loading_withdraw: false,
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
.balance-transactions {
  padding: 60px 8.5%;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 550px;
  overflow-y: scroll;
}
.balance-transactions .balance {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  margin-bottom: 40px;
  align-items: center;
  width: 75%;
}
.balance-transactions .balance div {
  margin-bottom: 10px;
}
.balance-transactions .balance .icon {
  background-image: url("../../../assets/panel/purple/Wallet.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  width: 100px;
  height: 100px;
}
.balance-transactions .balance .title {
  font-size: 22px;
  font-weight: 500;
}
.balance-transactions .balance .value {
  font-size: 18px;
  font-weight: 500;
}
.balance-transactions .balance .increase {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: auto;
  width: 80%;
}
.balance-transactions .balance .increase button {
  font-family: IRANsans;
  background-color: #5c438a;
  color: #fff;
  border-radius: 5px;
  border: solid 1px #979797;
  outline: none;
  font-size: 14px;
  font-weight: bold;
  width: 45%;
  padding: 8px 25px;
  cursor: pointer;
  transition: 0.4s ease;
}
.balance-transactions .balance .increase button:hover {
  opacity: 0.8;
  transition: 0.4s ease;
}

.balance-transactions .transactions {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-top: 2px solid #5c438a1a;
  width: 100%;
}
.balance-transactions .transactions .title {
  margin-top: -15px;
  width: 18%;
  background: #fff;
  margin-bottom: 22px;
  opacity: 0.9;
  font-size: 20px;
  color: #5c438a;
}
table {
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}

thead tr {
  background-color: #5c438a0c;
  font-size: 16px;
  height: 25px;
}
tbody {
  font-size: 14px;
}

td:first-child {
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}
td:last-child {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}
tr {
  height: 45px;
}
tbody tr:hover {
  border-color: #5c438a2f;
  background-color: #5c438a4f;
  cursor: pointer;
}

/* Modal Increase balance style */
/* The Modal (background) */
.modal-increase {
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
.modal-content-increase {
  background-color: #fefefe;
  margin: auto;
  width: 33%; /* Full width */
  height: 290px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  justify-content: center;
  flex-direction: column;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.modal-increase .header {
  display: flex;
  justify-content: center;
}
.modal-increase .title {
  margin: auto;
}
.modal-content-increase .yes-no {
  flex-direction: column;
  margin: auto;
}
.modal-content-increase button.accept {
  border-radius: 5px;
  margin-top: 30px;
  margin-bottom: 20px;
  cursor: pointer;
  width: 70%;
}
.modal-content-increase input {
  outline: none;
  opacity: 0.2;
  height: 40px;
  border-radius: 5px;
  border: solid 1px #162133;
  padding: 10px;
  transition: 0.4s ease;
  font-size: 14px;
  font-family: IRANsans;
  margin-top: 30px;
}
.modal-content-increase input:focus {
  opacity: 1;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.4s ease;
}
.yes-no {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  align-items: center;
  width: 70%;
}
.closeincrease {
  display: flex;
  justify-self: flex-end;
  background-image: url("../../../assets/close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  margin-left: 3%;
  cursor: pointer;
}

.closewithdraw {
  display: flex;
  justify-self: flex-end;
  background-image: url("../../../assets/close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  margin-left: 3%;
  cursor: pointer;
}

button.accept {
  font-family: IRANsans;
  background-color: #5c438a;
  color: #fff;
  border-radius: 5px;
  border: solid 1px #979797;
  outline: none;
  font-size: 0.9rem;
  font-weight: bold;
  width: 70%;
  padding: 8px 1%;
  cursor: pointer;
  transition: 0.4s ease;
}
button.deactive {
  font-family: IRANsans;
  background-color: #5c438a;
  color: #fff;
  border-radius: 5px;
  border: solid 1px #979797;
  outline: none;
  font-size: 0.9rem;
  font-weight: bold;
  width: 70%;
  padding: 8px 1%;
  cursor: pointer;
  transition: 0.4s ease;
  opacity: 0.6;
}

button.accept:hover {
  opacity: 0.8;
  transition: 0.4s ease;
}
/* 
* style done modal 
*/
.modal {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgba(92, 67, 138, 0.25); /* Fallback color */
  background-color: rgba(92, 67, 138, 0.25); /* Fallback color */
}
/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  width: 37%; /* Full width */
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
#doneModal .modal-content {
  width: 30%;
  height: 290px;
}
.done-icon {
  background-image: url("../../../assets/panel/purple/done.svg");
  display: flex;
  margin: 0px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 100px;
  height: 100px;
}
.error-icon {
  background-image: url("../../../assets/forbidden.svg");
  display: flex;
  margin: 0px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 100px;
  height: 100px;
}

@media screen and (min-width: 540px) and (max-width: 768px) {
  .balance-transactions {
    padding: 20px 4%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }

  thead tr,
  tbody {
    font-size: 0.7rem;
  }
  .balance-transactions .transactions .title {
    width: 33%;
  }
  .modal-content-increase {
    width: 90%;
  }
  .header {
    display: flex;
    justify-content: space-between;
  }
  .title {
    display: flex;
    margin: auto;
  }
}

@media screen and (max-width: 540px) {
  .balance-transactions {
    padding: 20px 4%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }
  .balance-transactions .balance .increase {
    flex-direction: column;
    width: 100%;
    align-items: center;
  }
  .balance-transactions .balance .increase button {
    width: 100%;
    margin-bottom: 20px;
  }
  thead tr,
  tbody {
    font-size: 0.7rem;
  }
  .balance-transactions .transactions .title {
    width: 33%;
  }
  .modal-content-increase {
    width: 90%;
  }
  .header {
    display: flex;
    justify-content: space-between;
  }
  .title {
    display: flex;
    margin: auto;
  }
}
</style>
