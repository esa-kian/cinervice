<template>
  <div class="suggests">
    <div class="title">پیشنهادات ({{ bids.length }})</div>
    <div class="suggest" v-for="bid in bids" :key="bid.id">
      <div class="header">
        <div class="profile">
          <div
            class="avatar"
            :style="{
              'background-image': 'url(' + bid.profile_picture + ')',
            }"
          ></div>
          <div class="detail">
            <div class="name">
              {{ bid.full_name }}
              <a :href="'/technician_profile/' + bid.technician_id"
                >مشاهده پروفایل</a
              >
            </div>
            <div class="rate">
              {{ bid.rate.substring(0, 3) }}
              <span class="votes"> (از {{ bid.votes }} رأی)</span>
            </div>
          </div>
        </div>
        <div class="price">
          <div class="value">
            قیمت پیشنهادی : {{ parseInt(bid.amount) }} تومان
          </div>
          <div class="accept">
            <button
              v-if="!loading"
              @click.prevent="
                acceptBid(bid.id, bid.technician_id, project_id, bid.user_id)
              "
            >
              قبول پیشنهاد
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
      <div class="body">{{ bid.description }}</div>
      <div class="footer">
        <div @click="startChat(bid.user_id)" class="chat">آغاز چت</div>
        <div class="time">
          {{ momentJ(bid.created_at).locale("fa").format("HH:mm - YYYY/MM/D") }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "Suggest",
  props: {
    bids: null,
    project_id: null,
  },
  methods: {
    acceptBid(bid_id, technician_id, project_id, user_id) {
      let data = {
        bid_id: bid_id,
        technician_id: technician_id,
        project_id: project_id,
      };
      this.loading = true;

      Axios.patch(this.$hostname + "/accept-bid", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          let data = {
            receiver_id: user_id,
          };
          Axios.post(this.$hostname + "/start-conversation", data, {
            headers: {
              Authorization: "Bearer " + eval(localStorage.token),
            },
          })
            .then((resp) => {
              this.$router.push("/panel/user/2");
            })
            .catch((err) => {
              console.log(err, "fail");
            });
        })
        .catch((err) => {
          console.log(err, "fail");
        });
    },
    startChat(user_id) {
      let data = {
        receiver_id: user_id,
      };
      Axios.post(this.$hostname + "/start-conversation", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.$router.push("/panel/user/5");
        })
        .catch((err) => {
          console.log(err, "fail");
        });
    },
  },
  data() {
    return {
      loading: false,
      momentJ: momentJ,
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
.suggests {
  margin-top: 50px;
  border-top: 2px solid #5c438a1a;
  display: flex;
  flex-direction: column;
}
.suggests .title {
  margin-top: -15px;
  width: 18%;
  background: #fff;
  margin-bottom: 20px;
  font-size: 20px;
  color: #5c438a;
}
.suggests .suggest {
  display: flex;
  flex-direction: column;
  margin-bottom: 50px;
}
.suggests .suggest .header {
  display: flex;
  width: 100%;
  justify-content: space-between;
  margin-bottom: 20px;
}
.price .accept button {
  font-family: IRANsans;
  background-color: #5c438a;
  color: #fff;
  border-radius: 5px;
  border: solid 1px #979797;
  outline: none;
  font-size: 18px;
  padding: 8px 0px;
  width: 100%;
  margin-top: 15px;
  cursor: pointer;
  transition: 0.4s ease;
}
.price .accept button:hover {
  opacity: 0.8;
  transition: 0.4s ease;
}
.suggests .suggest .header .profile {
  display: flex;
}
.suggests .suggest .header .profile .detail {
  margin-right: 20px;
}
.name a {
  font-size: 14px;
  opacity: 0.9;
  color: #000;
  transition: 0.3s ease;
}
.name a:hover {
  font-size: 14px;
  opacity: 1;
  color: #5c438a;
  transition: 0.3s ease;
}
.rate {
  padding-right: 25px;
  font-size: 16px;
  background-image: url("../../../../assets/panel/stars/fill.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-size: 20px;
}
.votes {
  font-size: 14px;
  opacity: 0.5;
}
.suggests .suggest .header .profile .avatar {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 70px;
  height: 70px;
  border: 1px solid #5c438a17;
  border-radius: 60px;
}
.suggests .suggest .footer {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  font-size: 14px;
}
.suggests .suggest .footer .chat {
  background-image: url("../../../../assets/panel/chat.svg");
  background-repeat: no-repeat;
  background-position: left;
  background-size: 15px;
  padding-left: 20px;
}
.suggests .suggest .footer .chat:hover {
  background-image: url("../../../../assets/panel/chat_hover.svg");
  color: #5c438a;
  cursor: pointer;
  text-decoration: underline;
}
.suggests .suggest .footer .time {
  color: #132135;
  opacity: 0.6;
}
@media screen and (max-width: 540px) {
  .suggests .suggest .header {
    flex-direction: column;
  }
}
</style>
