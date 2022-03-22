<template>
  <div class="container">
    <Navbar :activeTab="activeTab" />
    <div class="panel">
      <div class="technician-panel">
        <div class="content">
          <div v-if="activeTab === '0'">
            <Dashboard />
          </div>
          <div v-if="activeTab === '1'">
            <Account />
          </div>
          <div v-if="activeTab === '2'">
            <History />
          </div>
          <div v-if="activeTab === '3'">
            <Messages />
          </div>

          <div v-if="activeTab === '4'">
            <Profile />
          </div>
          <div v-if="activeTab === '5'">
            <InviteFriends />
          </div>
        </div>
        <div class="sidebar">
          <div class="info">
            <div
              class="logo"
              :style="{
                'background-image': 'url(' + profile_picture + ')',
              }"
            ></div>
            <div class="detail">
              <div class="name">
                {{ full_name.substring(0, 10) }}
                {{ full_name.length > 10 ? "..." : "" }}
              </div>
              <div class="rate">{{ rate.substring(0, 3) }}</div>
            </div>
          </div>
          <div class="control-panel">
            <div class="sections">
              <div
                :class="{
                  active_dashboard: isActive('0'),
                  dashboard: !isActive('0'),
                }"
                @click.prevent="switchTab('0')"
              >
                داشبورد
              </div>
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
                  active_history: isActive('2'),
                  history: !isActive('2'),
                }"
                @click.prevent="switchTab('2')"
              >
                تاریخچه
              </div>

              <div
                :class="{
                  active_messages: isActive('3'),
                  messages: !isActive('3'),
                }"
                @click.prevent="switchTab('3')"
              >
                پیام ها
              </div>

              <div
                :class="{
                  active_profile: isActive('4'),
                  profile: !isActive('4'),
                }"
                @click.prevent="switchTab('4')"
              >
                مشاهده پروفایل
              </div>

              <div
                :class="{
                  active_invite_friends: isActive('5'),
                  invite_friends: !isActive('5'),
                }"
                @click.prevent="switchTab('5')"
              >
                معرفی به دوستان
              </div>
            </div>
            <div class="logout" @click="logoutModal">خروج</div>
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
  </div>
</template>

<script>
import Navbar from "./Navbar";
import Dashboard from "./Dashboard";
import History from "./History";
import Account from "./Account";
import Messages from "./Messages";
import Profile from "./Profile";
import InviteFriends from "./InviteFriends";
import Axios from "axios";

export default {
  name: "Panel",
  components: {
    Navbar,
    Dashboard,
    History,
    Account,
    Messages,
    Profile,
    InviteFriends,
  },
  props: {
    activeTab: {
      default: "1",
    },
  },
  mounted() {
    this.detail();
  },
  methods: {
    detail() {
      Axios.get(this.$hostname + "/resume", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.full_name = resp.data.resume.technician[0].full_name;
          this.rate = resp.data.resume.technician[0].rate;
          this.profile_picture = resp.data.resume.technician[0].profile_picture;
        })
        .catch((err) => {
          this.$router.push("/register/technician");
        });
    },
    switchTab(x) {
      this.$router.push("/panel/technician/" + x);
    },
    isActive(menuItem) {
      return this.activeTab === menuItem;
    },
    logoutModal() {
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
    logout() {
      localStorage.removeItem("isAuth");
      this.$router.push("/");
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
      rate: "",
      full_name: "",
      profile_picture: null,
      public_route: this.$public_backend,
    };
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  background-color: #f7fff9;
  height: 100vh;
}
.panel {
  width: 100%;
  min-height: 700px;
  padding: 110px 9% 50px 9%;
  margin: 0px 0px 0px 0px;
}
.panel .technician-panel {
  width: 100%;
  min-height: 500px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  display: flex;
  justify-content: space-between;
  flex-direction: row-reverse;
}
.panel .technician-panel .content {
  width: 100%;
  max-height: 500px;
}
.panel .technician-panel .sidebar {
  display: flex;
  flex-direction: column;
  width: 23%;
  border-left: 2px solid #7ab38317;
}
.panel .technician-panel .sidebar .info {
  display: flex;
  padding: 15px 20px;
  align-items: center;
  border-bottom: 2px solid #7ab38317;
}
.panel .technician-panel .sidebar .info div {
  margin-bottom: 5px;
}
.panel .technician-panel .sidebar .info .logo {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  align-self: flex-start;
  border-radius: 50%;
  width: 70px;
  height: 70px;
}
.panel .technician-panel .sidebar .info .detail {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: auto;
}
.panel .technician-panel .sidebar .info .detail .rate {
  background-image: url("../../../assets/panel/stars/fill.svg");
  background-repeat: no-repeat;
  background-position-x: right;
  background-position-y: center;
  padding-right: 20px;
}
a {
  text-decoration: none;
  color: #000;
  font-size: 14px;
  cursor: pointer;
}
a:hover {
  text-decoration: underline;
  color: #7ab383;
}

.panel .technician-panel .sidebar .control-panel {
  display: flex;
  flex-direction: column;
  align-content: space-between;
  padding: 30px 0 20px 0;
  font-size: 14px;
}
.panel .technician-panel .sidebar .control-panel .sections {
  border-bottom: 2px solid #7ab38317;
  height: 350px;
}
.panel .technician-panel .sidebar .control-panel .sections div {
  margin-bottom: 30px;
  padding-right: 30%;
  background-position: 85%;
  cursor: pointer;
}

.panel .technician-panel .sidebar .control-panel .dashboard {
  background-image: url("../../../assets/panel/black/Dashboard.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.panel .technician-panel .sidebar .control-panel .account {
  background-image: url("../../../assets/panel/black/Account.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.panel .technician-panel .sidebar .control-panel .history {
  background-image: url("../../../assets/panel/black/List.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.panel .technician-panel .sidebar .control-panel .profile {
  background-image: url("../../../assets/panel/black/Resume.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.panel .technician-panel .sidebar .control-panel .messages {
  background-image: url("../../../assets/panel/black/Messages.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.panel .technician-panel .sidebar .control-panel .invite_friends {
  background-image: url("../../../assets/panel/black/Friends.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.panel .technician-panel .sidebar .control-panel .logout {
  background-image: url("../../../assets/panel/black/Exit.svg");
  background-repeat: no-repeat;
  background-position: right;
  padding-right: 30px;
  margin-top: 20px;
  cursor: pointer;
  margin-right: 30px;
}

.active_dashboard {
  background-image: url("../../../assets/panel/green/Dashboard.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #7ab383;
  border-radius: 5px;
  color: #7ab383;
}

.active_account {
  background-image: url("../../../assets/panel/green/Account.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #7ab383;
  border-radius: 5px;
  color: #7ab383;
}
.active_history {
  background-image: url("../../../assets/panel/green/History.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #7ab383;
  border-radius: 5px;
  color: #7ab383;
}

.active_profile {
  background-image: url("../../../assets/panel/green/Resume.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #7ab383;
  border-radius: 5px;
  color: #7ab383;
}

.active_messages {
  background-image: url("../../../assets/panel/green/Messages.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #7ab383;
  border-radius: 5px;
  color: #7ab383;
}
.active_invite_friends {
  background-image: url("../../../assets/panel/green/Friends.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px #7ab383;
  border-radius: 5px;
  color: #7ab383;
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
  background-color: rgba(122, 179, 131, 0.2); /* Fallback color */
  background-color: rgba(122, 179, 131, 0.2); /* Black w/ opacity */
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
  border-bottom: solid 2px #7ab38318;
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
  background-image: url("../../../assets/panel/green/Close.svg");
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
  background-image: url("../../../assets/panel/green/Exit.svg");
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
  border: 2px solid #7ab383;
  outline: none;
  font-size: 16px;
  font-weight: bold;
  width: 150px;
  color: #7ab383;
  height: 40px;
  width: 40%;
  transition: 0.4s ease;
}
button.accept:hover {
  background-color: #7ab383;
  color: #fff;
  transition: 0.4s ease;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 2px #7ab3831e;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #7ab3839f;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #7ab383;
}

@media screen and (min-width: 540px) and (max-width: 768px) {
  .panel {
    padding: 90px 3% 30px 3%;
  }
  .panel .technician-panel .content {
    width: 75%;
  }
  .panel .technician-panel .sidebar {
    width: 25%;
  }
}

@media screen and (max-width: 540px) {
  .panel .technician-panel .sidebar {
    display: none;
  }
  .panel {
    width: 100%;
    max-height: 700px;
    height: 700px;
    position: relative;
    padding: 90px 4% 30px 4%;
  }
  .panel .technician-panel .content {
    max-height: 100%;
  }
}
</style>