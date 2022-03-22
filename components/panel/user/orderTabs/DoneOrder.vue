<template>
  <div class="container">
    <Navbar />
    <div class="done">
      <div class="done-card">
        <div class="header">
          <div class="title">{{ order.proficiency.title }}</div>
          <div class="budget">
            <div class="caption">مبلغ کل:</div>
            <div class="budget-val">{{ parseInt(order.budget) }} تومان</div>
          </div>
        </div>
        <div class="body">
          <div class="technician">
            <div class="info">
              <div
                class="photo"
                :style="{
                  'background-image': 'url(' + order.technician_picture + ')',
                }"
              ></div>
              <div class="details">
                <div class="name">
                  <a href="/panel/user/technician_profile">
                    {{ order.technician_name }}
                  </a>
                </div>

                <div
                  class="save"
                  @click="saveTechnician(order.technician_id)"
                  v-show="!saved"
                >
                  افزودن به متخصصین منتخب
                </div>
              </div>
            </div>
            <div class="vote">
              <div class="title">امتیاز شما به این متخصص:</div>
              <div class="star">
                <div v-for="index in rate" :key="index" class="fill"></div>
                <i v-for="index in 5 - rate" :key="index" class="empty"></i>
              </div>
            </div>
          </div>
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
            {{ order.details }}
          </div>
          <div class="address">
            <i></i>
            {{
              order.address.city.title +
              ", " +
              order.address.town.title +
              ", " +
              order.address.description
            }}
          </div>
          <div class="photos">
            <img
              v-for="photo in order.photos"
              :key="photo.id"
              :src="photo.url"
              alt=""
              width="110px"
              height="110px"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="copyright">
      <Copyright />
    </div>
  </div>
</template>

<script>
import Navbar from "../../../Navbar";
import Copyright from "../../../Copyright";
import Axios from "axios";

export default {
  name: "Done",
  components: {
    Navbar,
    Copyright,
  },
  mounted() {
    this.fetchOrder();
  },
  methods: {
    fetchOrder() {
      Axios.get(this.$hostname + "/done-orders/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.order = resp.data.order.detail[0];
          this.start_at = moment(this.order.start_at).format(
            "dddd jD jMMMM jYYYY ساعت HH:mm"
          );
          if (resp.data.order.skills) {
            this.skills = resp.data.order.skills;
          }
          if (resp.data.order.rate) {
            this.rate = resp.data.order.rate;
          }
        })
        .catch((err) => {
          this.$router.push("/");
        });
    },
    saveTechnician(id) {
      Axios.post(
        this.$hostname + "/saved-technicians/" + id,
        eval(localStorage.token),
        {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        }
      )
        .then((resp) => {
          this.saved = true;
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
      order: null,
      skills: [],
      rate: null,
      saved: false,
      start_at: null,
      public_route: this.$public_backend,
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
  height: auto;
}
.done {
  background-color: #f8f5fc;
  height: 850px;
  width: 100%;
  max-width: 1366px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
}

.done .done-card {
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
}
.header .title {
  font-size: 24px;
  font-weight: bold;
  color: #5c438a;
}
.header .budget {
  border-radius: 5px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  color: #000;
  padding: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: 500;
  width: 250px;
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
.body .technician .info .photo {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 120px;
  height: 120px;
  border: 1px solid #5c438a17;
  border-radius: 60px;
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
.body .technician .info .details .save {
  font-size: 18px;
  font-weight: normal;
  padding-right: 25px;
  background-image: url("../../../../assets/panel/save.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-size: 20px;
  cursor: pointer;
  transition: 0.3s ease;
}

.body .technician .info .details .save:hover {
  background-image: url("../../../../assets/panel/saved.svg");
  transition: 0.3s ease;
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
  color: #5c438a;
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
  border: 2px dashed #5c438a42;
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
  background-image: url("../../../../assets/Tasks/Location.svg");
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
  background-image: url("../../../../assets/Tasks/Event.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}

.star {
  display: flex;
  flex-direction: row-reverse;
  margin-top: 10px;
}
.star .fill {
  background-image: url("../../../../assets/panel/stars/fill.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 25px;
  height: 25px;
}
.star .empty {
  background-image: url("../../../../assets/panel/stars/empty.png");
  background-repeat: no-repeat;
  background-size: contain;
  width: 25px;
  height: 25px;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .done {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }

  .done .done-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
    margin-top: 0;
  }
  .copyright {
    padding: 0 4%;
  }
}
@media screen and (max-width: 540px) {
  .done {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }

  .done .done-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
    margin-top: 0;
  }
  .body .technician .info {
    flex-direction: column;
  }
  .header {
    flex-direction: column;
  }
  .copyright {
    padding: 0 4%;
  }
  .body .technician {
    flex-direction: column;
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
  .body .photos img {
    margin-top: 10px;
  }
  .header .budget {
    margin-top: 20px;
  }
}
</style>
