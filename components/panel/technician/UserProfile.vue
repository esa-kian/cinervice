<template>
  <div>
    <Navbar />
    <div class="user">
      <div class="user-card">
        <div class="header">
          <div class="profile">
            <div
              class="photo"
              :style="{
                'background-image': 'url(' + client.profile_picture + ')',
              }"
            ></div>
            <div class="info">
              <div class="name">
                {{ client.full_name }}
              </div>
              <div class="register-date">عضو لِمِ کار از{{ created_at }}</div>
            </div>
          </div>
          <div class="detail">
            <div class="done">{{ projects }}</div>
            <div class="caption">درخواست ثبت شده</div>
            <div class="rate">
              <div class="point">{{ client.rate.substring(0, 3) }}</div>
              <div class="votes">(از {{ votes }} رأی)</div>
            </div>
          </div>
        </div>
        <div class="body">
          <!-- <div class="photos">
            <div class="title">تصاویر درخواست‌های ثبت شده</div>
            <img
              class="photo"
              src="../../../assets/post.png"
              alt=""
              width="150px"
              height="150px"
            />
            <img
              class="photo"
              src="../../../assets/post.png"
              alt=""
              width="150px"
              height="150px"
            />
            <img
              class="photo"
              src="../../../assets/post.png"
              alt=""
              width="150px"
              height="150px"
            />
            <img
              class="photo"
              src="../../../assets/post.png"
              alt=""
              width="150px"
              height="150px"
            />
          </div> -->

          <CommentsForUser :comments="comments" />
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
import Navbar from "./Navbar";
import CommentsForUser from "./CommentsForUser";
import Copyright from "./Copyright";

export default {
  name: "Done",
  components: {
    Navbar,
    CommentsForUser,
    Copyright,
  },
  mounted() {
    this.fetch();
  },
  methods: {
    fetch() {
      Axios.get(this.$hostname + "/client-profile/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.client = resp.data.client.detail[0];
          this.created_at = moment(this.client.created_at).format(
            " jD jMMMM jYYYY "
          );
          this.projects = resp.data.client.projects;
          this.comments = resp.data.client.comments;
          this.votes = resp.data.client.votes;
        })
        .catch((err) => {
          this.$router.push("/");
        });
    },
  },
  props: {
    id: null,
  },
  data() {
    return {
      client: null,
      projects: null,
      comments: [],
      votes: null,
    };
  },
};
</script>

<style scoped>
.copyright {
  padding: 0 11.5%;
}
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
}
.user {
  background-color: #f7fff9;
  height: 820px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
  width: 100%;
  max-width: 1366px;
}

.user .user-card {
  height: 650px;
  padding: 20px 20px 30px;
  display: flex;
  flex-direction: column;
  position: absolute;
  align-content: space-between;
  background-color: #fff;
  width: 58%;
  border-radius: 5px;
  max-height: 1000px;
  overflow-y: scroll;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.header {
  display: flex;
  justify-content: space-between;
  margin: 50px 8%;
}
.header .profile {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.header .profile .info {
  margin-right: 20px;
}
.header .name {
  font-size: 24px;
  font-weight: bold;
  color: #000;
}
.header .registe-date {
  opacity: 0.9;
  font-size: 16px;
}
.header .photo {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 120px;
  height: 120px;
  border-radius: 60px;
}
.header .detail {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 15px 25px 15px 24px;
  border-radius: 10px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
}
.header .detail .done {
  font-size: 26px;
  font-weight: bold;
}
.header .detail .caption {
  font-size: 20px;
  font-weight: 500;
}
.header .detail .rate {
  display: flex;
  width: 80%;
  margin-top: 10px;
}
.header .detail .rate .point {
  font-size: 18px;
  padding-right: 25px;
  margin-left: 25px;
  background-image: url("../../../assets/panel/stars/fill.svg");
  background-repeat: no-repeat;
  background-size: 16px;
  background-position-y: 4px;
  background-position-x: right;
  width: 25px;
  height: 25px;
}
.header .detail .rate .votes {
  opacity: 0.5;
  font-size: 14px;
  margin-right: 10px;
}

.body .photos .title {
  font-size: 24px;
  font-weight: bold;
  color: #7ab383;
  display: list-item;
  margin-right: 1.6rem;
  margin-bottom: 30px;
  width: 100%;
}

.body .photos {
  display: flex;
  flex-wrap: wrap;
}
.body .photos .photo {
  margin-bottom: 10px;
}

a {
  color: #000;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}

::marker {
  color: #7ab383;
  font-size: 30px;
  display: flex;
  justify-content: flex-start;
  margin: 0 !important;
  padding: 0 !important;
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
.photos {
  display: flex;
  justify-content: center;
  margin: 5px;
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
@media screen and (max-width: 540px) {
  .user {
    padding: 72px 4% 20px 4%;
    min-height: 700px;
    height: auto;
  }
  .user .user-card {
    width: 100%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 5px 5px 15px 30px;
  }
  .header {
    flex-direction: column;
    margin: 30px 8%;
  }
  .header .profile {
    flex-direction: column;
  }
  .header .profile .info {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 10px;
  }
  .body .photos .title {
    font-size: 1.2rem;
  }
  .photos {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    width: 100%;
  }
  .photos img {
    width: 45%;
    margin-left: 0;
  }
}
</style>
