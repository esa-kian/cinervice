<template>
  <div>
    <div v-if="!loading" class="technician-card">
      <div class="header">
        <div class="profile">
          <div
            class="photo"
            :style="{
              'background-image': 'url(' + details.profile_picture + ')',
            }"
          ></div>
          <div class="info">
            <div class="name">
              {{ details.full_name }}
            </div>
            <div class="register-date">متخصص لِمِ کار از {{ created_at }}</div>
          </div>
        </div>
        <div class="detail">
          <div class="done">{{ done }}</div>
          <div class="caption">درخواست انجام شده</div>
          <div class="rate">
            <div class="point">{{ rate.substring(0, 3) }}</div>
            <div class="votes">(از {{ votes }} رأی)</div>
          </div>
        </div>
      </div>
      <div class="body">
        <div class="skills">
          <div class="title">{{ details.proficiency }}</div>
          <div class="skill" v-for="skill in skills" :key="skill.skill_id">
            {{ skill.title }}
          </div>
        </div>
        <div class="confirmed">
          <div class="title">تایید شده توسط لِمِ کار</div>
          <div class="cert" v-for="cert in certificates" :key="cert.id">
            {{ cert.title }}
          </div>
        </div>
        <div class="photos">
          <div class="title">تصاویر درخواست‌های انجام شده</div>
          <img
            v-for="photo in photos"
            :key="photo.id"
            :src="photo.url"
            alt=""
            width="150px"
            height="150px"
          />
        </div>
        <Comments :comments="comments" />
      </div>
    </div>
    <div v-else>
      <img class="loading" src="../../../assets/loading_t.svg" alt="loading" />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "../../Navbar";
import Comments from "./Comments";

export default {
  name: "Profile",
  components: {
    Navbar,
    Comments,
  },
  mounted() {
    this.resume();
  },
  methods: {
    resume() {
      Axios.get(this.$hostname + "/resume", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.done = resp.data.resume.projects;
          this.rate = resp.data.resume.technician[0].rate;
          this.votes = resp.data.resume.technician[0].votes;
          this.details = resp.data.resume.technician[0];
          this.skills = resp.data.resume.skills;
          this.certificates = resp.data.resume.certificates;
          this.comments = resp.data.resume.comments;
          this.photos = resp.data.resume.photos;
          this.created_at = moment(this.details.created_at).format(
            " jD jMMMM jYYYY "
          );
          this.loading = false;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      rate: null,
      votes: null,
      done: null,
      details: null,
      skills: [],
      certificates: [],
      comments: [],
      loading: true,
    };
  },
};
</script>

<style scoped>
img.loading {
  width: 70px;
  height: 70px;
  margin: 250px auto;
}
.technician-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  padding: 0px 50px;
  height: 550px;
  overflow-y: scroll;
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
.body .skills .title,
.body .confirmed .title,
.body .photos .title {
  font-size: 24px;
  font-weight: bold;
  color: #7ab383;
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
  color: #7ab383;
}

.body .date {
  font-size: 18px;
  font-weight: 500;
}

::marker {
  color: #7ab383;
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
  border: 2px dashed #7ab38342;
  padding: 2px;
  outline: none;
}
.body .photos img {
  display: flex;
}
@media screen and (max-width: 540px) {
  .technician-card {
    padding: 10px 10px 10px 27px;
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
@media screen and (min-width: 540px) and (max-width: 768px) {
  .technician-card {
    padding: 10px 10px 10px 27px;
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
  .header .detail .rate {
    justify-content: center;
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
