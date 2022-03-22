<template>
  <div class="container">
    <Navbar />
    <div class="technician">
      <div class="technician-card">
        <div class="header">
          <div class="profile">
            <div
              class="photo"
              :style="{
                'background-image': 'url(' + technician.profile_picture + ')',
              }"
            ></div>
            <div class="info">
              <div class="name">
                {{ technician.full_name }}
              </div>
              <div class="register-date">
                متخصص لِمِ کار از
                {{ 
                  momentJ(technician.created_at)
                    .locale("fa")
                    .format(" D MMMM YYYY ")
                }}
              </div>
            </div>
          </div>
          <div class="detail">
            <div class="done">{{ projects }}</div>
            <div class="caption">درخواست انجام شده</div>
            <div class="rate">
              <div class="point">{{ technician.rate.substring(0, 3) }}</div>
              <div class="votes">(از {{ technician.votes }} رأی)</div>
            </div>
          </div>
        </div>
        <div class="body">
          <div class="skills">
            <div class="title">{{ technician.proficiency }}</div>
            <div class="skill" v-for="skill in skills" :key="skill.id">
              {{ skill.title }}
            </div>
          </div>
          <div class="confirmed">
            <div class="title">تایید شده توسط لِمِ کار</div>
            <div class="cert" v-for="cert in certificates" :key="cert.id">
              {{ cert.title }}
            </div>
          </div>
          <!-- <div class="photos">
            <div class="title">تصاویر درخواست‌های انجام شده</div>
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
          <Comments :comments="comments" />
        </div>
      </div>
    </div>
    <div class="copyright">
      <Copyright />
    </div>
  </div>
</template>

<script>
import Navbar from "../../Navbar";
import Comments from "./Comments";
import Copyright from "../../Copyright";
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "TechnicianProfile",
  components: {
    Navbar,
    Comments,
    Copyright,
  },
  mounted() {
    this.fetchProfile();
  },
  methods: {
    fetchProfile() {
      Axios.get(this.$hostname + "/technician-profile/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.technician = resp.data.technician.detail[0];
          this.projects = resp.data.technician.projects;
          this.skills = resp.data.technician.skills;
          this.certificates = resp.data.technician.certificates;
          this.comments = resp.data.technician.comments;
          console.log(this.technician);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  props: {
    id: null,
  },
  data() {
    return {
      technician: null,
      public_route: this.$public_backend,
      rate: null,
      votes: null,
      projects: null,
      comments: null,
      certificates: [],
      skills: [],
      momentJ: momentJ,
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
  background-color: #f8f5fc;
  height: 100vh;
}
.technician {
  width: 100%;
  max-width: 1366px;
  height: 820px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
}

.technician .technician-card {
  height: 650px;
  padding: 20px 20px 30px;
  display: flex;
  flex-direction: column;
  position: absolute;
  align-content: space-between;
  background-color: #fff;
  width: 58%;
  max-width: 750px;
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
  border: 1px solid #5c438a17;
  border-radius: 50%;
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
  text-align: center;
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
.body .skills .title,
.body .confirmed .title,
.body .photos .title {
  font-size: 24px;
  font-weight: bold;
  color: #5c438a;
  display: list-item;
  margin-right: 1.6rem;
  margin-bottom: 30px;
  width: 100%;
}
.body .skills,
.body .confirmed,
.body .photos {
  display: flex;
  flex-wrap: wrap;
}
.body .photos .photo {
  margin-bottom: 10px;
}
.body .skills .skill,
.body .confirmed .cert {
  font-size: 20px;
  width: 50%;
  margin-bottom: 30px;
  padding-right: 4%;
  background-position-x: right;
  background-position-y: center;
  background-repeat: no-repeat;
  background-size: 24px;
}
.body .skills .skill {
  background-image: url("../../../assets/panel/resume/skill.svg");
}
.body .confirmed .cert {
  background-image: url("../../../assets/panel/resume/cert.svg");
}
.body .technician {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  margin: 30px 0;
}
.body .technician .info {
  display: flex;
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

.body .date {
  font-size: 18px;
  font-weight: 500;
}

::marker {
  color: #5c438a;
  font-size: 30px;
  display: flex;
  justify-content: flex-start;
  margin: 0 !important;
  padding: 0 !important;
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
  .technician {
    padding: 72px 4% 20px 4%;
    min-height: 700px;
    height: auto;
  }
  .technician .technician-card {
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
  .body .skills,
  .body .confirmed {
    flex-direction: column;
  }
  .body .skills .title,
  .body .confirmed .title,
  .body .photos .title {
    font-size: 1.2rem;
  }
  .body .skills .skill,
  .body .confirmed .cert {
    width: 100%;
    padding-right: 12%;
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
