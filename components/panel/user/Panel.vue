<template>
  <div class="container">
    <Navbar :activeTab="activeTab" />
    <div v-if="loading" class="loading">
      <img src="../../../assets/loading.svg" alt="loading" />
      سخت نیست، فقط لِم داره…
    </div>
    <div v-else class="panel">
      <div class="user-panel">
        <div class="content">
          <div v-if="activeTab === '1'">
            <Account />
          </div>
          <div v-if="activeTab === '2'">
            <MyOrders />
          </div>
          <div v-if="activeTab === '3'">
            <BalanceTransaction />
          </div>
          <div v-if="activeTab === '4'">
            <SavedTechnician />
          </div>
          <div v-if="activeTab === '5'">
            <Messages />
          </div>
          <div v-if="activeTab === '6'">
            <InviteFriends />
          </div>
        </div>
        <div class="sidebar">
          <div class="balance">
            <div class="logo"></div>
            <div class="value">{{ balance }} تومان</div>
            <div class="increase" @click="balanceIncrease">
              <a>افزایش موجودی</a>
            </div>
          </div>
          <div class="control-panel">
            <div class="sections">
              <div
                :class="{
                  active_account: isActive('1'),
                  account: !isActive('1'),
                }"
                @click.prevent="switchTab('1')"
              >
                حساب کاربری
              </div>
              <div
                :class="{
                  active_orders: isActive('2'),
                  orders: !isActive('2'),
                }"
                @click.prevent="switchTab('2')"
              >
                درخواست های من
              </div>
              <div
                :class="{
                  active_balance_transaction: isActive('3'),
                  balance_transaction: !isActive('3'),
                }"
                @click.prevent="switchTab('3')"
              >
                اعتبار و تراکنش ها
              </div>
              <div
                :class="{
                  active_saved_technician: isActive('4'),
                  saved_technician: !isActive('4'),
                }"
                @click.prevent="switchTab('4')"
              >
                متخصصین منتخب
              </div>
              <div
                :class="{
                  active_messages: isActive('5'),
                  messages: !isActive('5'),
                }"
                @click.prevent="switchTab('5')"
              >
                پیام ها
              </div>
              <div
                :class="{
                  active_invite_friends: isActive('6'),
                  invite_friends: !isActive('6'),
                }"
                @click.prevent="switchTab('6')"
              >
                معرفی به دوستان
              </div>
            </div>
            <div class="logout" @click="logoutModalPanel">خروج</div>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal Logout -->
    <div id="myModal" class="modal">
      <div class="modal-content">
        <div class="header">
          <div class="title">خروج از حساب کاربری</div>
          <span class="close"></span>
        </div>
        <div class="content">
          <div class="logout-icon"></div>
          <p>آیا مطمئن هستید؟</p>
          <div class="yes-no">
            <button class="accept">خیر</button>
            <button class="accept">بله</button>
          </div>
        </div>
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
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "../../Navbar";
import Account from "./Account";
import MyOrders from "./MyOrders";
import BalanceTransaction from "./BalanceTransaction";
import InviteFriends from "./InviteFriends";
import Messages from "./Messages";
import SavedTechnician from "./SavedTechnician";

export default {
  name: "Panel",
  components: {
    Navbar,
    Account,
    MyOrders,
    BalanceTransaction,
    InviteFriends,
    Messages,
    SavedTechnician,
  },
  props: {
    activeTab: {
      default: "1",
    },
  },
  mounted() {
    this.isAuth();
    this.loading = false;
  },
  methods: {
    isAuth() {
      Axios.get(this.$hostname + "/is-auth", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {})
        .catch((err) => {
          this.$router.push("/");
        });
    },
    switchTab(x) {
      this.$router.push("/panel/user/" + x);
    },
    isActive(menuItem) {
      return this.activeTab === menuItem;
    },
    logoutModalPanel() {
      let modal = document.getElementById("myModal");

      // Get the <span> element that closes the modal
      let span = document.getElementsByClassName("close")[0];
      let accept = document.getElementsByClassName("accept")[0];

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
          Axios.get(this.$hostname + "/balance", {
            headers: {
              Authorization: "Bearer " + eval(localStorage.token),
            },
          })
            .then((resp) => {
              this.balance = resp.data.balance;
              localStorage.setItem("balance", this.balance);
            })
            .catch((err) => {
              console.log("can not fetch balance");
            });
        })
        .catch((err) => {
          this.message = err;
        });
    },
    balanceIncrease() {
      let modal = document.getElementById("increase");

      // Get the <span> element that closes the modal
      let span = document.getElementsByClassName("close")[0];

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
      balance: localStorage.balance,
      amount: null,
      message: "",
      success_deposit: false,
      loading: true,
    };
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  background-color: #f8f5fc;
  height: 100vh;
}
.panel {
  width: 100%;
  min-height: 700px;
  padding: 110px 9% 50px 9%;
  margin: 0;
}
.panel .user-panel {
  width: 100%;
  min-height: 500px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  display: flex;
  justify-content: space-between;
  flex-direction: row-reverse;
}
.panel .user-panel .content {
  width: 100%;
  max-height: 500px;
}
.panel .user-panel .sidebar {
  display: flex;
  flex-direction: column;
  width: 23%;
  border-left: 2px solid #5c438a17;
}
.panel .user-panel .sidebar .balance {
  display: flex;
  flex-direction: column;
  padding: 15px 40px;
  align-items: center;
  border-bottom: 2px solid #5c438a17;
}
.panel .user-panel .sidebar .balance div {
  margin-bottom: 5px;
}
.panel .user-panel .sidebar .balance .logo {
  background-image: url("../../../assets/panel/purple/Wallet.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  width: 40px;
  height: 40px;
}
.panel .user-panel .sidebar .balance .value {
  font-size: 16px;
  font-weight: 500;
}
.panel .user-panel .sidebar .balance .increase {
  font-size: 14px;
  font-weight: 500;
}
a {
  text-decoration: none;
  color: #000;
  font-size: 14px;
  cursor: pointer;
}
a:hover {
  text-decoration: underline;
  color: #5c438a;
}

.panel .user-panel .sidebar .control-panel {
  display: flex;
  flex-direction: column;
  align-content: space-between;
  padding: 30px 0 20px 0;
  font-size: 14px;
}
.panel .user-panel .sidebar .control-panel .sections {
  border-bottom: 2px solid #5c438a17;
  height: 350px;
}
.panel .user-panel .sidebar .control-panel .sections div {
  margin-bottom: 30px;
  padding-right: 30%;
  background-position: 85%;
  cursor: pointer;
}
.panel .user-panel .sidebar .control-panel .account {
  background-image: url("../../../assets/panel/black/Account.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.panel .user-panel .sidebar .control-panel .orders {
  background-image: url("../../../assets/panel/black/List.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.panel .user-panel .sidebar .control-panel .balance_transaction {
  background-image: url("../../../assets/panel/black/Wallet.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.panel .user-panel .sidebar .control-panel .saved_technician {
  background-image: url("../../../assets/panel/black/Saved.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.panel .user-panel .sidebar .control-panel .messages {
  background-image: url("../../../assets/panel/black/Messages.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.panel .user-panel .sidebar .control-panel .invite_friends {
  background-image: url("../../../assets/panel/black/Friends.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.panel .user-panel .sidebar .control-panel .logout {
  background-image: url("../../../assets/panel/black/Exit.svg");
  background-repeat: no-repeat;
  background-position: right;
  padding-right: 30px;
  margin-top: 20px;
  cursor: pointer;
  margin-right: 30px;
}

.active_account {
  background-image: url("../../../assets/panel/purple/Account.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #5c438a;
  border-radius: 5px;
  color: #5c438a;
}
.active_orders {
  background-image: url("../../../assets/panel/purple/List.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #5c438a;
  border-radius: 5px;
  color: #5c438a;
}

.active_balance_transaction {
  background-image: url("../../../assets/panel/purple/Wallet.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #5c438a;
  border-radius: 5px;
  color: #5c438a;
}
.active_saved_technician {
  background-image: url("../../../assets/panel/purple/saved.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #5c438a;
  border-radius: 5px;
  color: #5c438a;
}
.active_messages {
  background-image: url("../../../assets/panel/purple/Messages.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #5c438a;
  border-radius: 5px;
  color: #5c438a;
}
.active_invite_friends {
  background-image: url("../../../assets/panel/purple/Friends.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #5c438a;
  border-radius: 5px;
  color: #5c438a;
}

/* Modal Logout style */
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
.modal-content {
  background-color: #fefefe;
  margin: auto;
  border: 1px solid #888;
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
.close {
  display: flex;
  justify-self: flex-end;
  background-image: url("../../../assets/close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  margin-left: 3%;
}
.close:hover {
  cursor: pointer;
}
.logout-icon {
  background-image: url("../../../assets/panel/purple/Exit.svg");
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
button.accept {
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
  transition: 0.4s ease;
}
button.accept:hover {
  background-color: #5c438a;
  color: #fff;
  transition: 0.4s ease;
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
  background-image: url("../../../assets/panel/green/Close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  margin-left: 3%;
}
.closeincrease:hover {
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
  margin: 30px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 100px;
  height: 100px;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .panel .user-panel .sidebar {
    display: none;
  }
  .panel {
    width: 100%;
    max-height: 700px;
    height: 700px;
    position: relative;
    padding: 90px 4% 30px 4%;
  }
  .panel .user-panel .content {
    max-height: 100%;
  }
}
@media screen and (max-width: 540px) {
  .panel .user-panel .sidebar {
    display: none;
  }
  .panel {
    width: 100%;
    max-height: 700px;
    height: 700px;
    position: relative;
    padding: 90px 4% 30px 4%;
  }
  .panel .user-panel .content {
    max-height: 100%;
  }
}
</style>
