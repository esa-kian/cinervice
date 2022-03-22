<template>
  <div class="container">
    <Navbar />
    <div class="project">
      <div class="project-card">
        <div class="header">
          <div class="client">
            <div class="info">
              <div
                class="photo"
                :style="{
                  'background-image': 'url(' + project.client_picture + ')',
                }"
              ></div>
              <div class="details">
                <div class="name">
                  <a
                    :href="
                      '/panel/technician/user_profile/' + project.client_id
                    "
                  >
                    {{ project.client_name }}</a
                  >
                </div>
                <div class="register-date">
                  عضو لِمِ کار از {{ created_at }}
                </div>
              </div>
            </div>
          </div>
          <div class="budget">
            <div class="caption">بودجه :</div>
            <div class="budget-val">{{ parseInt(project.budget) }} تومان</div>
          </div>
        </div>
        <div class="body">
          <div class="title">{{ project.proficiency }}</div>

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
            {{ project.details }}
          </div>
          <div class="address">
            <i></i>
            {{ project.address }}
          </div>
          <div class="photos">
            <img
              v-for="photo in project.photos"
              :key="photo.id"
              :src="photo.url"
              alt=""
              width="110px"
              height="110px"
            />
          </div>
        </div>
        <div class="buttons">
          <button @click.prevent="show_cost = true">افزودن پیشنهاد</button>
          <button @click.prevent="show_comment = true">افزودن نظر</button>
        </div>
      </div>
    </div>
    <div class="similars">
      <h3>درخواست های مشابه</h3>
      <div class="req-cards">
        <div class="req-card" v-for="similar in similars" :key="similar.id">
          <a :href="'/project/' + similar.id">
            <div class="header">
              <div class="title">{{ similar.proficiency.title }}</div>
              <div class="price">{{ parseInt(similar.budget) }} تومان</div>
            </div>
            <div class="details">
              <div class="date">
                <i></i>
                {{
                  momentJ(similar.start_at)
                    .locale("fa")
                    .format("dddd D jMMMM YYYY ساعت HH:mm")
                }}
              </div>
              <div class="address">
                <i></i>
                {{
                  similar.address.city.title + ", " + similar.address.town.title
                }}
              </div>
            </div>
          </a>
        </div>
      </div>
    </div>
    <div class="copyright">
      <Copyright />
    </div>
    <!-- Modal bid -->
    <transition name="fade">
      <div id="cost-modal" class="modal" v-if="show_cost">
        <div class="modal-content">
          <div class="header">
            <div class="title">افزودن پیشنهاد</div>
            <span class="close" @click="show_cost = false"></span>
          </div>
          <div class="content">
            <div class="cost">
              <p>مبلغ مورد نظر خود را برای انجام این درخواست وارد کنید.</p>
              <input
                v-model="amount"
                type="text"
                id="cost"
                placeholder="تومان"
              />
            </div>
            <div class="comment">
              <p>توضیحات لازم برای پیشنهاد خود را درج نمایید.</p>
              <textarea
                v-model="description"
                name="comment"
                id="comment"
              ></textarea>
            </div>
          </div>
          <span
            class="error"
            v-if="has_error"
            @click.prevent="has_error = false"
            >{{ message }}</span
          >
          <div class="yes-no">
            <button v-if="!loading_bid" @click.prevent="finish" class="done">
              ثبت پیشنهاد
            </button>
            <div v-else>
              <img
                class="loading"
                src="../../../assets/loading_t.svg"
                alt="loading"
              />
            </div>
          </div>
        </div>
      </div>
    </transition>
    <!-- Modal comment -->
    <transition name="fade">
      <div id="cost-modal" class="modal" v-if="show_comment">
        <div class="modal-content">
          <div class="header">
            <div class="title">افزودن نظر</div>
            <span class="close" @click="show_comment = false"></span>
          </div>
          <div class="content">
            <div class="comment">
              <p>نظر خود را درباره این درخواست ثبت نمایید.</p>
              <textarea
                v-model="comment"
                name="comment"
                id="comment"
              ></textarea>
            </div>
          </div>
          <span
            class="error"
            v-if="has_error"
            @click.prevent="has_error = false"
            >{{ message }}</span
          >
          <div class="yes-no">
            <button
              v-if="!loading_comment"
              @click.prevent="finish_comment"
              class="done"
            >
              ثبت نظر
            </button>
            <div v-else>
              <img
                class="loading"
                src="../../../assets/loading_t.svg"
                alt="loading"
              />
            </div>
          </div>
        </div>
      </div>
    </transition>
    <!-- done bid modal  -->
    <transition name="fade">
      <div id="doneModal" class="modal" v-if="show_done">
        <div class="modal-content">
          <div class="content">
            <div class="done-icon"></div>
            <p>پیشنهاد شما با موفقیت ثبت شد.</p>
          </div>
        </div>
      </div>
    </transition>
    <!-- done comment modal  -->
    <transition name="fade">
      <div id="doneModal" class="modal" v-if="show_done_comment">
        <div class="modal-content">
          <div class="content">
            <div class="done-icon"></div>
            <p>نظر شما با موفقیت ثبت شد.</p>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "./Navbar";
import Copyright from "./Copyright";
import momentJ from "jalali-moment";

export default {
  name: "Project",
  components: {
    Copyright,
    Navbar,
  },
  mounted() {
    this.fetchProject();
  },
  methods: {
    fetchProject() {
      Axios.get(this.$hostname + "/projects/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.project = resp.data.project.detail[0];
          this.similars = resp.data.similars;
          this.skills = resp.data.project.skills;
          this.created_at = moment(this.project.client_date).format(
            " jD jMMMM jYYYY "
          );
          this.start_at = moment(this.project.start_at).format(
            "dddd jD jMMMM jYYYY ساعت HH:mm"
          );
        })
        .catch((err) => {
          console.log(err);
          this.$router.push("/register/technician");
        });
    },
    finish() {
      this.has_error = false
      this.loading_bid = true;
      if (this.amount == null) {
        this.loading_bid = false;
        this.has_error = true;
        this.message = "مبلغ پیشنهاد را وارد کنید";
      } else if (this.description == null) {
        this.loading_bid = false;
        this.has_error = true;
        this.message = "پر کردن توضیحات اجباری است";
      } else {
        let data = {
          project_id: this.id,
          description: this.description,
          amount: eval(this.amount),
        };
        Axios.post(this.$hostname + "/make-bid", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.loading_bid = false;
            this.show_cost = false;
            this.show_done = true;
            setTimeout(() => (this.show_done = false), 3000);
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    finish_comment() {
      this.has_error = false
      this.loading_comment = true;
      let data = {
        content: this.comment,
        project_id: this.id,
      };
      Axios.post(this.$hostname + "/add-comment", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading_comment = false;
          this.show_comment = false;
          this.show_done_comment = true;
          setTimeout(() => (this.show_done_comment = false), 3000);
        })
        .catch((err) => {
          this.loading_comment = false;
          this.has_error = true;
          this.message = err.response.data.message;
        });
    },
  },
  props: {
    id: null,
  },
  data() {
    return {
      project: null,
      skills: null,
      show_cost: false,
      description: null,
      amount: null,
      show_comment: false,
      show_done: false,
      show_done_comment: false,
      comment: null,
      momentJ: momentJ,
      similars: null,
      loading_comment: false,
      loading_bid: false,
      message: "",
      has_error: false,
    };
  },
};
</script>

<style scoped>
span.error {
  background-color: #c7434377;
  width: 50%;
  border-radius: 10px;
  margin: auto;
  color: rgb(10, 8, 8);
  cursor: pointer;
}

img.loading {
  width: 40px;
  height: 40px;
  margin: auto;
}
.copyright {
  padding: 0 11.5%;
}
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
}
.project {
  background-color: #f7fff9;
  height: 700px;
  width: 100%;
  max-width: 1366px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  margin: auto;
}

.project .project-card {
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
  align-items: center;
}
.body .title {
  font-size: 24px;
  font-weight: bold;
  color: #7ab383;
}
.header .budget {
  border-radius: 5px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  color: #7ab383;
  padding: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: 500;
  width: 250px;
  max-height: 47px;
  margin-left: 50px;
}
.header .client {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  margin: 30px 0;
}
.header .client .info {
  display: flex;
}
.header .client .info .photo {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 120px;
  height: 120px;
  border-radius: 60px;
}
.header .client .info .details {
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
.header .client .info .details .register-date {
  color: #000;
  font-size: 16px;
  font-weight: 500;
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
  color: #7ab383;
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
  border: 2px dashed #7ab38342;
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
  background-image: url("../../../assets/panel/green/location.svg");
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
  background-image: url("../../../assets/panel/green/event.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
.similars {
  display: flex;
  flex-direction: column;
  padding: 0 9%;
  background-color: #f7fff9;
}
h3 {
  font-size: 26px;
  font-weight: 500;
  color: #7ab383;
}
.req-cards {
  flex-wrap: wrap;
  display: flex;
  align-content: center;
  flex-direction: row;
  justify-content: flex-start;
}
.req-cards a:hover {
  text-decoration: none;
}
.req-card {
  display: flex;
  margin: 10px;
  height: 150px;
  width: 31.2%;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  border: 2px solid transparent;
  transition: 0.4s ease;
}

.req-card:hover {
  border: 2px solid #7ab383;
  cursor: pointer;
  transition: 0.4s ease;
  text-decoration: none;
}

.req-cards .req-card .header {
  display: flex;
  justify-content: space-between;
  color: #7ab383;
  opacity: 0.9;
}

.req-cards .req-card .header .title {
  font-size: 20px;
  font-weight: bold;
}
.req-cards .req-card .header .price {
  font-size: 18px;
  font-weight: bold;
}

.req-cards .req-card .details {
  font-size: 18px;
  font-weight: 500;
  opacity: 0.8;
}

.req-cards .req-card .details .date {
  display: flex;
  align-items: center;
}
.req-cards .req-card .details .address {
  display: flex;
  align-items: center;
}
.req-cards .req-card .details i {
  display: flex;
  justify-content: flex-start;
  margin-left: 10px;
  background-size: contain;
  background-repeat: no-repeat;
  width: 20px;
  height: 20px;
}
.req-cards .req-card .details .date i {
  background-image: url("../../../assets/panel/green/event.svg");
}
.req-cards .req-card .details .address i {
  background-image: url("../../../assets/panel/green/location.svg");
}

.buttons {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 65%;
  margin: 0 auto;
}

button {
  margin-top: 50px;
  align-self: center;
  cursor: pointer;
  outline: none;
  padding: 10px 45px 10px;
  border-radius: 5px;
  font-size: 18px;
  font-weight: 500;
  width: 45%;
  background-color: #fff;
  border: 2px solid #7ab383;
  font-family: "IRANSans";
  color: #7ab383;
  transition: 0.4s ease;
}
button:hover {
  background-color: #7ab383;
  color: #fff;
  transition: 0.4s ease;
}

/* 
* styles cost modal 
*/
/* Modal general style */
/* The Modal (background) */
.modal {
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
.modal-content .header {
  display: flex;
  color: #000;
  font-size: 22px;
  font-weight: 500;
  justify-content: space-between;
  align-items: center;
  border-bottom: solid 2px #7ab38318;
  padding-bottom: 15px;
}
.modal-content .header .title {
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
/* 
* style done modal 
*/

#doneModal .modal-content {
  width: 30%;
  height: 290px;
}
.done-icon {
  background-image: url("../../../assets/panel/green/done.svg");
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
  margin: auto;
}

button.done {
  background-color: #fff;
  border-radius: 5px;
  border: 2px solid #7ab383;
  outline: none;
  font-size: 16px;
  font-weight: bold;
  color: #7ab383;
  height: 46px;
  width: 100%;
  transition: 0.4s ease;
  cursor: pointer;
  margin-top: 17px;
}

button.done:hover {
  background-color: #7ab383;
  color: #fff;
  transition: 0.4s ease;
}
#cost-modal .modal-content .header {
  height: 70px;
  color: #7ab383;
}
#cost-modal .modal-content {
  justify-content: space-between;
  height: 490px;
  width: 50%;
}
#cost-modal .modal-content .content {
  justify-content: space-between;
  align-items: unset;
}
#cost-modal p {
  text-align: right;
}
#cost-modal .yes-no {
  margin-bottom: 40px;
  margin-top: 10px;
}
.comment,
.cost {
  width: 94% !important;
  margin: 10px 20px;
}
.cost {
  display: flex;
  justify-content: space-between;
}
.comment p,
.cost p {
  padding: 0 !important;
  margin: 0;
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
  border: solid 1px #7ab383;
  resize: none;
  transition: 0.4s ease;
  font-family: IRANsans;
}
textarea:focus {
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  opacity: 1;
  transition: 0.4s ease;
}

input#cost {
  border-radius: 5px;
  border: solid 1px #7ab383;
  outline: none;
  width: 35%;
  text-align: left;
  font-size: 20px;
  font-family: IRANsans;
  padding: 10px;
  transition: 0.4s ease;
  height: 44px;
  opacity: 0.6;
}
input#cost:focus {
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.4s ease;
  opacity: 1;
}
/* 
* effect show/hide modals 
*/
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
@media screen and (max-width: 540px) {
  .project {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }
  .project .project-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }
  .header {
    flex-direction: column;
  }
  .header .client .info .details .register-date {
    font-size: 0.9rem;
  }
  .body .title {
    margin-top: 20px;
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
  .copyright {
    padding: 0 4%;
  }
  .body .photos img {
    margin-top: 10px;
  }

  .req-cards {
    width: 100%;
    margin-top: 40px;
    flex-direction: column;
  }
  .req-card {
    width: 90%;
    height: 220px;
  }
  .req-cards .req-card .details,
  .req-cards .req-card .header {
    flex-direction: row;
  }
  #cost-modal .modal-content {
    width: 90%;
    height: fit-content;
    display: flex;
  }

  #cost-modal .modal-content .header {
    flex-direction: row;
    height: 60px;
  }
  .cost {
    flex-direction: column;
  }
  input#cost {
    width: 100%;
  }
  #cost-modal p {
    width: 100%;
  }
  textarea {
    width: 100%;
  }
  .comment,
  .cost {
    margin: 10px;
  }
  #cost-modal .modal-content .content {
    display: contents;
  }
  #cost-modal .yes-no {
    margin-bottom: 10px;
    margin-top: 0;
  }
  button.done {
    margin-top: 0;
  }
  #doneModal .modal-content {
    width: 90%;
  }
}
</style>
