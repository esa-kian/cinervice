<template>
  <div class="container">
    <Navbar />

    <div class="faq">
      <h3>اعلانات</h3>
      <div v-if="!loading" role="tablist">
        <div
          v-for="(notification, index) in notifications"
          :item="notification.id"
          :key="notification.id"
        >
          <b-card no-body>
            <b-card-header header-tag="header" role="tab">
              <a @click.prevent="setActive(notification.id)" href>
                <b-button
                  block
                  v-b-toggle="'accordion-' + index"
                  variant="info"
                >
                  <div class="title">
                    <div class="right-side">
                      <div class="notif-title">
                        <div
                          :class="{
                            unread: notification.unread == 1,
                            read: notification.unread == 0,
                          }"
                        ></div>
                        {{ notification.title }}
                      </div>
                      <div class="date">
                        {{
                          momentJ(notification.created_at)
                            .locale("fa")
                            .format("HH:mm - YYYY/MM/D")
                        }}
                      </div>
                    </div>
                    <div class="left-side">
                      <div class="arrow"></div>
                    </div>
                  </div>
                </b-button>
              </a>
            </b-card-header>
            <b-collapse
              :id="'accordion-' + index"
              accordion="my-accordion"
              role="tabpanel"
            >
              <b-card-body>
                <b-card-text>{{ notification.description }}</b-card-text>
              </b-card-body>
            </b-collapse>
          </b-card>
        </div>
      </div>
      <div v-else>
        <img class="loading" src="../../assets/loading.svg" alt="loading" />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "../Navbar";
import Footer from "../Footer";
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "Notifications",
  components: {
    Navbar,
    Footer,
  },
  mounted() {
    this.fetchNotifications();
  },
  methods: {
    fetchNotifications() {
      Axios.get(this.$hostname + "/notifications", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.notifications = resp.data.notifications.data;
        })
        .catch((err) => {
          this.$router.push("/");
        });
    },
    setActive(id) {
      let data = {
        notification_id: id,
      };
      Axios.patch(this.$hostname + "/notifications", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.fetchNotifications();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      notifications: [],
      loading: true,
      momentJ: momentJ,
    };
  },
};
</script>

<style scoped>
@import url("bootstrap/dist/css/bootstrap.css");

.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  padding: 0;
}
img.loading {
  width: 70px;
  height: 70px;
  margin: 150px auto;
}
.faq {
  width: 100%;
  padding: 110px 11.5% 50px 11.5%;
  margin: 0px 0px 0px 0px;
  background-color: #f8f5fc;
}
h3 {
  font-size: 28px;
  color: #5c438a;
  margin-top: 0px;
  font-family: IRANsans;
}
p {
  font-size: 16px;
}
button {
  background: transparent;
  border: transparent;
  font-size: 18px;
  font-family: IRANsans;
  display: flex;
  align-items: center;
  text-decoration: none;
  width: 100%;
}
button:hover {
  cursor: pointer;
}
a {
  text-decoration: none;
}
button:focus {
  outline: transparent !important;
  outline-color: transparent !important;
}
.card {
  border-bottom: solid 2px #d8d1e5;
  padding-bottom: 10px;
  padding-top: 10px;
}
.title {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.title .right-side {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #132135;
  width: 60%;
}
.notif-title {
  display: flex;
  align-items: center;
}
.right-side .date {
  color: #132135;
  opacity: 0.8;
}
.title .right-side .read {
  background-image: url("../../assets/Caution_black.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  height: 20px;
  width: 20px;
  margin-left: 10px;
}
.title .right-side .unread {
  background-image: url("../../assets/Caution.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  height: 20px;
  width: 20px;
  margin-left: 10px;
}
.left-side {
  display: flex;
  align-items: center;
}
.left-side .arrow {
  background-image: url("../../assets/FAQ/arrow_down.svg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  height: 15px;
  width: 15px;
}

button:focus .arrow {
  transition: 0.3s ease;
  transform: rotate(180deg);
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .faq {
    padding: 80px 4% 30px 4%;
  }
  .question {
    height: 25px;
    width: 25px;
    margin-left: 15px;
  }
  .title .right-side {
    width: 90%;
  }
}
@media screen and (max-width: 540px) {
  .faq {
    padding: 80px 4% 30px 4%;
  }
  .question {
    height: 25px;
    width: 25px;
    margin-left: 15px;
  }
}
</style>
