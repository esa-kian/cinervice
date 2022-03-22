<template>
  <div>
    <header>
      <nav class="navigation" @mouseleave="showMenu = false">
        <div class="mobile">
          <router-link :to="'/'"> <div class="logo"></div></router-link>
          <span @click="openSidebar">&#9776;</span>
        </div>
        <ul class="nav__right">
          <router-link :to="'/'"> <li class="logo"></li></router-link>
          <li>
            <div class="filter-search">
              <select class="filter-search">
                <option v-for="city in cities" :key="city.id" :value="city.id">
                  {{ city.title }}
                </option>
              </select>
            </div>
          </li>
          <li>
            <router-link :to="'/categories'"> دسته‌بندی‌ها</router-link>
          </li>
          <li>
            <router-link :to="'/new_request'"> ثبت درخواست </router-link>
          </li>
          <li>
            <router-link :to="'/tasks'"> درخواست‌ها </router-link>
          </li>
          <li>
            <router-link :to="'/register/technician'">
              <button class="join-technician">
                پیوستن متخصصین
              </button></router-link
            >
          </li>
        </ul>
        <ul class="nav__left">
          <i
            v-if="isAuth"
            @click.prevent="notification"
            :class="{
              notification_active: inNotifications,
              notification: !inNotifications,
            }"
          >
            <span v-if="new_notifications" id="badge">•</span>
          </i>

          <li v-if="isAuth" @mouseover="showMenu = true">
            <a>{{ name }} <i class="dropdown-icon"></i></a>

            <div
              @mouseleave="showMenu = false"
              class="control-panel"
              v-if="showMenu"
            >
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
              <div class="logout" @click="logoutModal">خروج</div>
            </div>
          </li>
          <li v-else>
            <router-link :to="'/register/user'">
              <button class="user-panel">پنل کاربری</button>
            </router-link>
          </li>
        </ul>
      </nav>
    </header>

    <!-- Sidebar in responsive mode -->
    <div id="sidebar" class="sidenav">
      <a href="javascript:void(0)" class="closebtn" @click="closeSidebar"
        >&times;</a
      >
      <ul class="nav__right">
        <li class="logo"><a href="/"></a></li>
        <li>
          <div class="filter-search">
            <select class="filter-search">
              <option v-for="city in cities" :key="city.id" :value="city.id">
                {{ city.title }}
              </option>
            </select>
          </div>
        </li>
        <li>
          <router-link :to="'/categories'"> دسته‌بندی‌ها</router-link>
        </li>
        <li>
          <router-link :to="'/new_request'"> ثبت درخواست </router-link>
        </li>
        <li>
          <router-link :to="'/tasks'"> درخواست‌ها </router-link>
        </li>
        <li>
          <router-link :to="'/register/technician'">
            <button class="join-technician">پیوستن متخصصین</button></router-link
          >
        </li>
        <li v-if="isAuth" @click="showMenuPanel">
          <a>{{ name }} <i class="dropdown-icon"></i></a>

          <div id="control-panel" class="control-panel">
            <div class="sections">
              <span v-if="new_notifications" id="badge">•</span>

              <div
                @click.prevent="notification"
                :class="{
                  notification_active: inNotifications,
                  notification: !inNotifications,
                }"
              >
                اعلانات
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
            <div class="logout" @click.prevent="logoutModal">خروج</div>
          </div>
        </li>
        <li v-else>
          <router-link :to="'/register/user'">
            <button class="user-panel">پنل کاربری</button>
          </router-link>
        </li>
      </ul>
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
            <button class="accept" @click="logout">بله</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "Navbar",
  mounted() {
    this.init();
    this.fetchCities();
  },
  methods: {
    init() {
      if (localStorage.isAuth) {
        this.hasUnreadNotification();
        this.isAuth = true;
        this.name = eval(localStorage.name);
        if (this.$route.name == "Notifications") {
          this.inNotifications = true;
        }
        window.setInterval(() => {
          this.hasUnreadNotification();
        }, 30000);
      } else {
        this.isAuth = false;
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
    hasUnreadNotification() {
      Axios.get(this.$hostname + "/new-notification", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.new_notifications = resp.data.new_notifications;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    openSidebar() {
      document.getElementById("sidebar").setAttribute("style", "width:100%");
    },
    closeSidebar() {
      let sidebar = document.getElementById("sidebar");
      document.getElementById("sidebar").setAttribute("style", "width:0px");
      // When the user clicks anywhere outside of the modal, close it
      window.onclick = function (event) {
        if (event.target == document.getElementById("sidebar")) {
          document.getElementById("sidebar").setAttribute("style", "width:0px");
        }
      };
    },
    switchTab(x) {
      this.$router.push("/panel/user/" + x);
    },
    isActive(menuItem) {
      return this.activeTab === menuItem;
    },
    showMenuPanel() {
      if (this.showMenu == false) {
        document
          .getElementById("control-panel")
          .setAttribute("style", "height:400px");

        this.showMenu = true;
      } else {
        document
          .getElementById("control-panel")
          .setAttribute("style", "height:0px");
        this.showMenu = false;
      }
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
      Axios.get(this.$hostname + "/logout", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          localStorage.removeItem("name");
          localStorage.removeItem("token");
          localStorage.removeItem("isAuth");
          localStorage.removeItem("user_type");
          this.$router.push("/");
          this.$router.go();
        })
        .catch((err) => {
          console.log(err, "can not logout");
        });
    },
    notification() {
      this.$router.push("/notifications");
    },
  },
  props: {
    activeTab: null,
  },
  data() {
    return {
      name: null,
      isAuth: false,
      showMenu: false,
      inNotifications: false,
      cities: null,
      new_notifications: null,
    };
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}
.filter-search {
  display: flex;
  width: 100%;
  min-width: 82px;
  height: 50px;
}
select.filter-search {
  outline: none;
  appearance: none;
  border: none;
  border-radius: 20px;
  background-image: url("../assets/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-y: 20px;
  background-position-x: 1em;
  background-size: 10px;
  cursor: pointer;
  background-color: transparent;
  font-size: 1rem;
  font-weight: 300;
  font-family: IRANSans;
  width: 100%;
  height: 55px;
  padding: 15px;
}
select option {
  background: #fff;
  color: #5c438a;
  width: 100px;
}
ul {
  margin: 0px;
}
header {
  max-width: 1366px;
  width: 100%;
  margin: 0 auto;
}
.navigation {
  background-color: rgba(255, 255, 255, 0.589);
  box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.05);
  backdrop-filter: blur(8px) saturate(180%);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  z-index: 995;
  width: 100%;
  max-width: 1366px;
  margin: auto;
  height: 60px;
}
.navigation span {
  display: none;
}
.navigation .logo {
  background-image: url("../assets/logo.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  height: 50px;
  width: 50px;
}

.navigation a {
  color: #000;
  transition: 0.4s ease;
}

.navigation a:hover {
  transition: 0.4s ease;
  opacity: 0.8;
}

.navigation .nav__right,
.navigation .nav__left {
  display: flex;
  justify-content: center;
  align-items: center;
}

.navigation .nav__right li,
.navigation .nav__left li {
  list-style: none;
  padding: 0;
  margin-left: 40px;
  font-size: 0.8rem;
}
.navigation .nav__right li.logo {
  margin-right: 126px;
}
.dropdown-icon {
  background-image: url("../assets/Blog/arrow_down.svg");
  background-repeat: round;
  display: inline-flex;
  width: 7px;
  height: 5px;
  margin-right: 9px;
}
button.join-technician {
  font-family: IRANsans;
  background-color: #fff;
  border: 2px solid #7ab383;
  color: #7ab383;
  outline: none;
  border-radius: 10px;
  padding: 7px 15px;
  font-size: 0.8rem;
  font-weight: 500;
  transition: 0.4s ease;
}
button.join-technician:hover {
  cursor: pointer;
  background-color: #7ab383;
  color: #fff;
  transition: 0.4s ease;
}
/*
 *    Left side
 */
span#badge {
  color: #f10816;
  font-size: 1.9rem;
  display: block;
  position: absolute;
  padding-right: 3px;
  padding-top: 12px;
  font-style: normal;
  line-height: 0px;
}
i.notification {
  background-image: url("../assets/notifications.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 30px;
  margin-left: 10px;
  height: 30px;
  transition: 0.5s linear;
  cursor: pointer;
}
i.notification:hover {
  background-image: url("../assets/notifications_active.svg");
  -webkit-animation: ring 4s 0.1s ease-in-out infinite;
  -webkit-transform-origin: 50% 4px;
  -moz-animation: ring 4s 0.1s ease-in-out infinite;
  -moz-transform-origin: 50% 4px;
  animation: ring 4s 0.1s ease-in-out infinite;
  transform-origin: 50% 4px;
}

@-webkit-keyframes ring {
  0% {
    -webkit-transform: rotateZ(0);
  }
  1% {
    -webkit-transform: rotateZ(30deg);
  }
  3% {
    -webkit-transform: rotateZ(-28deg);
  }
  5% {
    -webkit-transform: rotateZ(34deg);
  }
  7% {
    -webkit-transform: rotateZ(-32deg);
  }
  9% {
    -webkit-transform: rotateZ(30deg);
  }
  11% {
    -webkit-transform: rotateZ(-28deg);
  }
  13% {
    -webkit-transform: rotateZ(26deg);
  }
  15% {
    -webkit-transform: rotateZ(-24deg);
  }
  17% {
    -webkit-transform: rotateZ(22deg);
  }
  19% {
    -webkit-transform: rotateZ(-20deg);
  }
  21% {
    -webkit-transform: rotateZ(18deg);
  }
  23% {
    -webkit-transform: rotateZ(-16deg);
  }
  25% {
    -webkit-transform: rotateZ(14deg);
  }
  27% {
    -webkit-transform: rotateZ(-12deg);
  }
  29% {
    -webkit-transform: rotateZ(10deg);
  }
  31% {
    -webkit-transform: rotateZ(-8deg);
  }
  33% {
    -webkit-transform: rotateZ(6deg);
  }
  35% {
    -webkit-transform: rotateZ(-4deg);
  }
  37% {
    -webkit-transform: rotateZ(2deg);
  }
  39% {
    -webkit-transform: rotateZ(-1deg);
  }
  41% {
    -webkit-transform: rotateZ(1deg);
  }

  43% {
    -webkit-transform: rotateZ(0);
  }
  100% {
    -webkit-transform: rotateZ(0);
  }
}

@-moz-keyframes ring {
  0% {
    -moz-transform: rotate(0);
  }
  1% {
    -moz-transform: rotate(30deg);
  }
  3% {
    -moz-transform: rotate(-28deg);
  }
  5% {
    -moz-transform: rotate(34deg);
  }
  7% {
    -moz-transform: rotate(-32deg);
  }
  9% {
    -moz-transform: rotate(30deg);
  }
  11% {
    -moz-transform: rotate(-28deg);
  }
  13% {
    -moz-transform: rotate(26deg);
  }
  15% {
    -moz-transform: rotate(-24deg);
  }
  17% {
    -moz-transform: rotate(22deg);
  }
  19% {
    -moz-transform: rotate(-20deg);
  }
  21% {
    -moz-transform: rotate(18deg);
  }
  23% {
    -moz-transform: rotate(-16deg);
  }
  25% {
    -moz-transform: rotate(14deg);
  }
  27% {
    -moz-transform: rotate(-12deg);
  }
  29% {
    -moz-transform: rotate(10deg);
  }
  31% {
    -moz-transform: rotate(-8deg);
  }
  33% {
    -moz-transform: rotate(6deg);
  }
  35% {
    -moz-transform: rotate(-4deg);
  }
  37% {
    -moz-transform: rotate(2deg);
  }
  39% {
    -moz-transform: rotate(-1deg);
  }
  41% {
    -moz-transform: rotate(1deg);
  }

  43% {
    -moz-transform: rotate(0);
  }
  100% {
    -moz-transform: rotate(0);
  }
}

@keyframes ring {
  0% {
    transform: rotate(0);
  }
  1% {
    transform: rotate(30deg);
  }
  3% {
    transform: rotate(-28deg);
  }
  5% {
    transform: rotate(34deg);
  }
  7% {
    transform: rotate(-32deg);
  }
  9% {
    transform: rotate(30deg);
  }
  11% {
    transform: rotate(-28deg);
  }
  13% {
    transform: rotate(26deg);
  }
  15% {
    transform: rotate(-24deg);
  }
  17% {
    transform: rotate(22deg);
  }
  19% {
    transform: rotate(-20deg);
  }
  21% {
    transform: rotate(18deg);
  }
  23% {
    transform: rotate(-16deg);
  }
  25% {
    transform: rotate(14deg);
  }
  27% {
    transform: rotate(-12deg);
  }
  29% {
    transform: rotate(10deg);
  }
  31% {
    transform: rotate(-8deg);
  }
  33% {
    transform: rotate(6deg);
  }
  35% {
    transform: rotate(-4deg);
  }
  37% {
    transform: rotate(2deg);
  }
  39% {
    transform: rotate(-1deg);
  }
  41% {
    transform: rotate(1deg);
  }

  43% {
    transform: rotate(0);
  }
  100% {
    transform: rotate(0);
  }
}

.notification_active {
  background-image: url("../assets/notifications_active.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 30px;
  margin-left: 10px;
  height: 30px;
}

.navigation .nav__left {
  margin-left: 6%;
  padding-right: 0px;
}
.navigation .nav__left button {
  background-color: #5c438aa8;
  color: #fff;
  border-radius: 10px;
  font-family: IRANsans;
  border: none;
  outline: none;
  padding: 7px 33px;
  font-size: 0.8rem;
  font-weight: 500;
  transition: 0.4s ease;
}
.navigation .nav__left button:hover {
  cursor: pointer;
  background-color: #5c438a;
  transition: 0.4s ease;
}
.nav__left a:hover {
  cursor: pointer;
}

.control-panel {
  display: flex;
  flex-direction: column;
  align-content: space-between;
  position: fixed;
  width: 15%;
  top: 60px;
  left: 4%;
  padding: 0 0 15px 0;
  font-size: 0.8rem;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
}
.control-panel .sections {
  border-bottom: 2px solid #7ab38317;
  height: 350px;
}
.control-panel .sections div {
  height: 55px;
  padding: 16px 20%;
  background-position: 95%;
  cursor: pointer;
  transition: 0.4s ease;
}
.control-panel .sections div:hover {
  background-color: #5c438a21;
  transition: 0.4s ease;
}
.control-panel .account {
  background-image: url("../assets/panel/black/Account.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.control-panel .orders {
  background-image: url("../assets/panel/black/List.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}

.control-panel .balance_transaction {
  background-image: url("../assets/panel/black/Wallet.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.control-panel .saved_technician {
  background-image: url("../assets/panel/black/Saved.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.control-panel .messages {
  background-image: url("../assets/panel/black/Messages.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.control-panel .invite_friends {
  background-image: url("../assets/panel/black/Friends.svg");
  background-repeat: no-repeat;
  background-position: right;
  border-right: solid 5px transparent;
}
.control-panel .logout {
  background-image: url("../assets/panel/black/Exit.svg");
  background-repeat: no-repeat;
  background-position: right;
  padding-right: 30px;
  margin-top: 20px;
  cursor: pointer;
  margin-right: 30px;
}

.active_account {
  background-image: url("../assets/panel/purple/Account.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-color: #5c438a21;
  color: #5c438a;
}
.active_orders {
  background-image: url("../assets/panel/purple/List.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-color: #5c438a21;
  color: #5c438a;
}

.active_balance_transaction {
  background-image: url("../assets/panel/purple/Wallet.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-color: #5c438a21;
  color: #5c438a;
}
.active_saved_technician {
  background-image: url("../assets/panel/purple/saved.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-color: #5c438a21;
  color: #5c438a;
}
.active_messages {
  background-image: url("../assets/panel/purple/Messages.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-color: #5c438a21;
  color: #5c438a;
}
.active_invite_friends {
  background-image: url("../assets/panel/purple/Friends.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-color: #5c438a21;
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
  background-image: url("../assets/close.svg");
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
  background-image: url("../assets/panel/purple/Exit.svg");
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
.mobile {
  display: none;
}
.sidenav {
  display: none;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .control-panel .sections div {
    background-position: 98%;
    background-size: 30px;
    padding: 15px 10%;
  }
  span#badge {
    padding-right: 17px;
    padding-top: 24px;
  }
  .navigation {
    padding: 1%;
  }
  .mobile {
    display: flex;
    justify-content: space-between;
    width: 100%;
    align-items: center;
  }
  .navigation .nav__left,
  .navigation .nav__right {
    display: none;
  }
  .sidenav {
    display: initial;
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 996;
    top: 0;
    left: 0;
    background-color: rgba(255, 255, 255, 0.884);
    box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.05);
    backdrop-filter: blur(8px) saturate(180%);
    overflow-x: hidden;
    transition: 0.1s linear;
    padding-top: 60px;
  }
  .navigation span {
    display: flex;
    font-size: 2.8rem;
    font-weight: bold;
    color: #5c438a;
  }
  button.user-panel {
    background-color: #5c438aa8;
    color: #fff;
    border-radius: 10px;
    border: none;
    outline: none;
    padding: 7px 33px;
    font-size: 0.8rem;
    font-weight: 500;
    transition: 0.4s ease;
    font-family: IRANsans;
  }
  button.user-panel:hover {
    cursor: pointer;
    background-color: #5c438a;
    transition: 0.4s ease;
  }

  .sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 1.1rem;
    color: rgba(0, 0, 0, 0.726);
    display: block;
    transition: 0.3s linear;
  }

  .sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 0;
    font-size: 36px;
    margin-left: 5px;
    color: #5c438a;
  }
  ul {
    padding: 0;
  }
  li {
    list-style: none;
    border-bottom: 2px solid #5c438a46;
    padding-right: 4%;
  }
  .control-panel {
    height: 0;
    display: flex;
    flex-direction: column;
    align-content: space-between;
    width: 100%;
    top: unset;
    left: unset;
    padding: 0 0 15px 0;
    font-size: 1.1rem;
    border-radius: 0;
    box-shadow: none;
    background-color: transparent;
    overflow: hidden;
    transition: 0.3s linear;
  }
  .modal {
    z-index: 999;
  }
  .modal-content {
    width: 90%;
  }
  select.filter-search {
    background-color: transparent;
    width: 30%;
    height: 45px;
    padding: 0 10px;
    font-size: 0.9rem;
  }
  .filter-search {
    height: 45px;
  }
  .notification {
    background-image: url("../assets/notifications.svg");
    background-repeat: no-repeat;
  }
}
@media screen and (max-width: 540px) {
  .navigation {
    padding: 2%;
  }
  .control-panel .sections div {
    background-position: 95%;
    background-size: 25px;
    padding: 15px 15%;
  }

  .mobile {
    display: flex;
    justify-content: space-between;
    width: 100%;
    align-items: center;
  }
  .navigation span {
    display: flex;
    font-size: 1.8rem;
    font-weight: bold;
    color: #5c438a;
  }
  .navigation .nav__left,
  .navigation .nav__right {
    display: none;
  }
  .sidenav {
    display: initial;
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 996;
    top: 0;
    left: 0;
    background-color: rgba(255, 255, 255, 0.884);
    box-shadow: 0 4px 10px 0 rgba(0, 0, 0, 0.05);
    backdrop-filter: blur(8px) saturate(180%);
    overflow-x: hidden;
    transition: 0.1s linear;
    padding-top: 60px;
  }
  button.user-panel {
    background-color: #5c438aa8;
    color: #fff;
    border-radius: 10px;
    border: none;
    outline: none;
    padding: 7px 33px;
    font-size: 0.8rem;
    font-weight: 500;
    transition: 0.4s ease;
    font-family: IRANsans;
  }
  button.user-panel:hover {
    cursor: pointer;
    background-color: #5c438a;
    transition: 0.4s ease;
  }
  .sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 1.1rem;
    color: rgba(0, 0, 0, 0.726);
    display: block;
    transition: 0.3s linear;
  }

  .sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 0;
    font-size: 36px;
    margin-left: 5px;
    color: #5c438a;
  }
  ul {
    padding: 0;
  }
  li {
    list-style: none;
    border-bottom: 2px solid #5c438a46;
    padding-right: 4%;
  }
  .control-panel {
    height: 0;
    display: flex;
    flex-direction: column;
    align-content: space-between;
    width: 100%;
    top: unset;
    left: unset;
    padding: 0 0 15px 0;
    font-size: 1.1rem;
    border-radius: 0;
    box-shadow: none;
    background-color: transparent;
    overflow: hidden;
    transition: 0.3s linear;
  }
  .modal {
    z-index: 999;
  }
  .modal-content {
    width: 90%;
  }
  select.filter-search {
    background-color: transparent;
    width: 30%;
    height: 45px;
    padding: 0 10px;
    font-size: 0.9rem;
  }
  .filter-search {
    height: 45px;
  }
}
</style>