<template>
  <div class="container">
    <Navbar />
    <div class="main">
      <transition name="fade">
        <div v-if="step == 9" class="review">
          <div class="header">
            <div class="title">{{ proficiency_title }}</div>
            <div class="budget">
              <div class="caption">بودجه شما :</div>
              <div class="budget-val">{{ budget }} تومان</div>
            </div>
          </div>
          <div class="body">
            <div class="date">
              <i></i>
              {{
                momentJ(start_at)
                  .locale("fa")
                  .format("dddd D jMMMM YYYY ساعت HH:mm")
              }}
            </div>
            <div class="skills">
              <ul>
                <li>{{ skills }}</li>
              </ul>
            </div>
            <div class="detail">
              {{ details }}
            </div>
            <div class="address">
              <i></i>
              {{ city_title + ", " + town + ", " + address }}
            </div>
            <div class="photos">
              <!-- <img
                src="../../assets/post.png"
                alt=""
                width="110px"
                height="110px"
              />
              <img
                src="../../assets/post.png"
                alt=""
                width="110px"
                height="110px"
              />
              <img
                src="../../assets/post.png"
                alt=""
                width="110px"
                height="110px"
              /> -->
            </div>
            <div v-if="vip == 1" class="discount">
              <div class="title">کد تخفیف</div>
              <div class="code">
                <input type="text" v-model="discount_code" />
                <button @click="checkDiscount" id="discount">اعمال</button>
              </div>
            </div>
            <span :class="[valid ? 'valid' : 'error']">{{ message }}</span>
          </div>
          <div class="footer">
            <img
              v-if="loading"
              class="loading"
              src="../../assets/loading.svg"
              alt="loading"
            />
            <div v-else class="next-prev">
              <button @click="prevStep">مرحله قبل</button>

              <button @click="nextStep">ثبت درخواست</button>
            </div>
          </div>
        </div>
      </transition>
      <transition name="fade">
        <div v-if="step == 10" class="done">
          <div class="header">درخواست شما با موفقیت ثبت شد.</div>
          <div class="body">
            <p>
              {{ name }} عزیز،‌ لطفا منتظر بمانید تا اولین متخصص برای خدمت رسانی
              به شما اعلام آمادگی کند.
            </p>
            <hr />
            <p>
              متخصص معرفی شده در زمان مقرر برای انجام کار شما آماده خواهد بود.
              لطفا آدرس دقیق و جزییات سفارش را تلفنی هماهنگ نمایید.
            </p>
            <hr />

            <p>
              در صورتی که بعد از مشاهده پروفایل متخصص و نظرات دیگران درباره او
              به نظرتان می رسد که او گزینه مناسبی برای کار شما نیست، می توانید
              گزینه «رد متخصص» را انتخاب نمایید و سپس منتظر بمانید تا متخصص
              جدیدی کار شما را بپذیرد.
            </p>
            <div class="identification">
              <div class="title">شناسه درخواست :</div>
              <div class="id-code">{{ tracking_code }}</div>
            </div>
          </div>
          <div class="footer">
            <div class="next-prev">
              <button @click.prevent="tracking">پیگیری درخواست</button>
            </div>
          </div>
        </div>
      </transition>
      <div v-if="step != 10 && step != 9" class="new-request">
        <div class="header">
          <div v-if="step == 0">افزودن آدرس</div>
          <div v-else>ثبت درخواست</div>
        </div>
        <div class="content">
          <div class="remain-bar">
            <div
              class="complete-bar"
              :style="{ width: step * 14.3 + '%' }"
            ></div>
          </div>
          <div class="body">
            <transition name="fade">
              <div v-if="step == 1">
                <StepOne @continue_btn="continueBtn" />
              </div>
            </transition>
            <transition name="fade">
              <div v-if="step == 2">
                <StepTwo />
              </div>
            </transition>
            <transition name="fade">
              <div v-if="step == 3">
                <StepThree @continue_btn="continueBtn" />
              </div>
            </transition>
            <transition name="fade">
              <div v-if="step == 4">
                <StepFour />
              </div>
            </transition>
            <transition name="fade">
              <div v-if="step == 5">
                <StepFive @continue_btn="continueBtn" />
              </div>
            </transition>
            <transition name="fade">
              <div v-if="step == 6">
                <StepSix @continue_btn="continueBtn" />
              </div>
            </transition>
            <transition name="fade">
              <div v-if="step == 7 && vip == 1">
                <StepSeven />
              </div>
            </transition>
            <transition name="fade">
              <NewAddress v-if="step == 0" />
            </transition>
          </div>
          <div class="footer">
            <div v-if="step == 5" class="new-address">
              <button @click="newAddress">افزودن آدرس جدید</button>
            </div>
            <div v-if="step != 0" class="next-prev">
              <button v-if="step != 1" @click="prevStep">مرحله قبل</button>
              <button v-if="continue_btn" @click="nextStep">ادامه</button>
            </div>
            <div class="next-prev add-address">
              <button v-if="step == 0" @click="addAddress">افزودن آدرس</button>
            </div>
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
import Navbar from "../Navbar";
import StepOne from "./StepOne";
import StepTwo from "./StepTwo";
import StepThree from "./StepThree";
import StepFour from "./StepFour";
import StepFive from "./StepFive";
import StepSix from "./StepSix";
import StepSeven from "./StepSeven";
import NewAddress from "./NewAddress";
import Review from "./Review";
import Copyright from "../Copyright";
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "NewRequest",
  mounted() {
    this.start();
  },
  components: {
    Navbar,
    StepOne,
    StepTwo,
    StepThree,
    StepFour,
    StepFive,
    StepSix,
    StepSeven,
    NewAddress,
    Review,
    Copyright,
  },
  methods: {
    start() {
      if (localStorage.details && localStorage.proficiency) {
        this.continue_btn = true;
      } else {
        this.continue_btn = false;
      }
    },
    newAddress() {
      this.step = 0;
    },
    addAddress() {
      let data = {
        city_id: localStorage.city,
        town_id: localStorage.town,
        description: localStorage.description,
        lat: localStorage.lat,
        long: localStorage.long,
      };

      Axios.post(this.$hostname + "/addresses", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((data) => {
          this.step = 5;
        })
        .catch((err) => {
          console.log(err.message, "درخواست نامعتبر");
        });

      // localStorage.setItem("addresses", localStorage.description);
    },
    continueBtn(val) {
      this.continue_btn = val;
    },
    nextStep() {
      this.proficiency_title = localStorage.proficiency_title;
      this.budget = localStorage.budget;
      this.start_at = localStorage.datetime;
      this.skills = localStorage.skill_title;
      this.details = localStorage.details;
      this.city_title = localStorage.city_title;
      this.town = localStorage.town;
      this.address = localStorage.description;
      this.name = localStorage.name;
      this.vip = parseInt(localStorage.vip);
      if (this.step == 2) {
        this.continue_btn = false;
      }
      if (this.step == 4) {
        this.continue_btn = false;
      }
      if (this.step == 5) {
        this.continue_btn = false;
      }
      if (this.step == 7) {
        this.step = 9;
      } else if (this.step == 6 && localStorage.vip == 0) {
        this.step = 9;
      } else if (this.step == 9) {
        let data = {
          proficiency_id: parseInt(localStorage.proficiency),
          details: localStorage.details,
          skills: JSON.stringify(localStorage.skills),
          products: JSON.stringify(localStorage.products),
          photos: JSON.stringify(localStorage.photos),
          start_at: localStorage.datetime,
          budget: parseInt(localStorage.budget),
          city_id: parseInt(localStorage.city),
          address_id: parseInt(localStorage.address),
          vip: parseInt(localStorage.vip),
          discount_code: this.discount_code,
        };
        this.loading = true;
        Axios.post(this.$hostname + "/projects", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.tracking_code = resp.data.tracking_code;
            this.loading = false;
            this.step++;
          })
          .catch((err) => {
            console.log("fail", err);
          });
      } else {
        this.step++;
      }
    },
    tracking() {
      localStorage.removeItem("proficiency");
      localStorage.removeItem("details");
      localStorage.removeItem("skills");
      localStorage.removeItem("products");
      localStorage.removeItem("photos");
      localStorage.removeItem("datetime");
      localStorage.removeItem("budget");
      localStorage.removeItem("city");
      localStorage.removeItem("address");
      localStorage.removeItem("vip");
      localStorage.removeItem("proficiency_title");
      localStorage.removeItem("skill_title");
      localStorage.removeItem("city_title");
      localStorage.removeItem("description");
      localStorage.removeItem("town");
      this.$router.push("/order/current/" + this.tracking_code);
    },
    prevStep() {
      if (this.step == 9) {
        if (this.vip == 1) {
          this.step = 7;
        } else {
          this.step = 6;
        }
      } else if (this.step == 3) {
        this.step--;
        this.continue_btn = true;
      } else {
        this.step--;
      }
    },
    checkDiscount() {
      Axios.get(this.$hostname + "/check-discount/" + this.discount_code, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.valid = resp.data.valid;
          this.message = resp.data.message;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      step: 1,
      proficiency_title: localStorage.proficiency_title,
      budget: localStorage.budget,
      start_at: localStorage.datetime,
      skills: localStorage.skill_title,
      details: localStorage.details,
      address: localStorage.description,
      town: localStorage.town,
      city: localStorage.city,
      city_title: localStorage.city_title,
      momentJ: momentJ,
      discount_code: "",
      vip: null,
      tracking_code: null,
      name: "",
      continue_btn: false,
      message: "",
      valid: null,
      loading: false,
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
  height: 100%;
  min-height: 100vh;
}
.copyright {
  padding: 0 11.5%;
}
.main {
  width: 100%;
  height: 730px;
  margin: auto;
  background-color: #f8f5fc;
  display: flex;
  align-items: center;
  justify-content: center;
  align-content: space-between;
}
.done {
  display: flex;
  flex-direction: column;
  position: absolute;
  align-content: space-between;
  justify-content: center;
  background-color: #fff;
  width: 62%;
  min-height: 400px;
  border-radius: 5px;
  padding: 20px 20px 0 20px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
img.loading {
  width: 40px;
  height: 40px;
  margin: auto;
}
.done .header {
  display: flex;
  justify-content: center;
  color: #5c438a;
  font-size: 24px;
  font-weight: 500;
}
.done .body {
  display: flex;
  justify-content: center;
  text-align: center;
  flex-direction: column;
  align-items: center;
  font-size: 16px;
}
.done .body .identification {
  display: flex;
  justify-content: center;
  font-size: 18px;
  opacity: 0.8;
}
.done .footer button {
  width: 32%;
  margin: 20px 0;
}
.review {
  display: flex;
  flex-direction: column;
  position: absolute;
  align-content: space-between;
  background-color: #fff;
  width: 58%;
  min-height: 520px;
  border-radius: 5px;
  padding: 20px 20px 0 20px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.review .header {
  display: flex;
  justify-content: space-between;
  color: #5c438a;
}
.review .header .title {
  font-size: 24px;
  font-weight: bold;
}
.review .header .budget {
  border-radius: 5px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  padding: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: 500;
  width: 250px;
}

.review .body .date {
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
.review .body .address {
  margin-top: 20px;
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
.discount {
  display: flex;
  align-items: baseline;
  margin-top: 20px;
}

.discount .title {
  font-size: 16px;
  font-weight: 500;
  color: #162133;
  opacity: 0.8;
  margin-left: 20px;
}
.review .body .photos img {
  display: flex;
}
.address {
  display: flex;
  justify-content: flex-start;
  margin: 20px 0;
}
.address i {
  background-image: url("../../assets/Tasks/Location.svg");
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
  background-image: url("../../assets/Tasks/Event.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
.code {
  margin-bottom: 30px;
  display: flex;
  justify-content: flex-start;
}

.code input {
  outline: none;
  margin-top: 0;
  width: 260px;
  height: 42px;
  opacity: 0.3;
  border-radius: 5px;
  border: solid 2px #5c438a;
  border-left: none;
  border-top-left-radius: 0px;
  border-bottom-left-radius: 0px;
  padding: 5px 10px;
  font-family: IRANsans;
  text-align: left;
  transition: 0.4s ease;
}

.code #discount {
  outline: none;
  border: none;
  cursor: pointer;
  background-color: #5c438a;
  color: #fff;
  font-size: 16px;
  font-weight: 500;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  padding-left: 25px;
  padding-right: 25px;
  opacity: 0.3;
  transition: 0.4s ease;
}
.code input:focus,
.discount input:focus ~ #discount {
  opacity: 1;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.4s ease;
}
.new-request {
  display: flex;
  flex-direction: column;
  align-content: space-between;
  background-color: #fff;
  width: 49%;
  height: 500px;
  border-radius: 5px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}
.new-request .header {
  display: flex;
  align-items: center;
  justify-content: center;
}
.new-request .header div {
  font-size: 24px;
  font-weight: 500;
  color: #5c438a;
  padding-top: 20px;
  padding-bottom: 20px;
}
.main .new-request .content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.main .new-request .body {
  display: flex;
  padding: 0 20px 20px 20px;
  margin-top: auto;
  min-height: 320px;
  width: 100%;
  position: relative;
  overflow-y: scroll;
  overflow-x: hidden;
}

.content .remain-bar {
  height: 5px;
  background-color: #5c438a2d;
  margin-bottom: 15px;
}
.content .complete-bar {
  height: 5px;
  background-color: #5c438a;
  border-top-left-radius: 2px;
  border-bottom-left-radius: 2px;
  transition: 0.4s linear;
}
.main .new-request .body div {
  position: absolute;
  width: 96%;
}

.footer .next-prev {
  display: flex;
  flex-direction: row;
  justify-content: center;
  padding-left: 100px;
  padding-bottom: 20px;
  padding-right: 100px;
}
.footer .new-address {
  display: flex;
  justify-content: center;
}
.footer button {
  display: flex;
  background-color: #fff;
  border: 2px solid #5c438a;
  margin: 0 15px;
  width: 36%;
  outline: none;
  cursor: pointer;
  justify-content: center;
  border-radius: 5px;
  color: #5c438a;
  font-size: 18px;
  font-weight: 500;
  transition: 0.4s ease;
  padding: 10px 20px;
  font-family: IRANsans;
}
.footer button:hover {
  background-color: #5c438a;
  color: #fff;
  transition: 0.4s ease;
}

.new-address button {
  position: absolute;
  font-size: 14px;
  margin-top: -4rem;
  margin-right: 0;
  padding: 8px 20px;
  width: 200px;
}

.add-address button {
  padding: 5px 20px;
  font-size: 14px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .main {
    padding-top: 72px;
    min-height: 578px;
    height: auto;
  }
  .new-request {
    width: 92%;
    font-size: 70%;
  }
  .copyright {
    padding: 0 4%;
  }
  .footer button {
    width: 100%;
    font-size: 0.9rem;
    padding: 10px 15px;
  }
  .footer .next-prev {
    padding-left: 0px;
    padding-right: 0px;
  }
  .new-address button {
    width: 50%;
  }
  .review {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }

  ul {
    display: block;
  }
  .address i {
    background-repeat: no-repeat;
    background-size: contain;
    width: 35px;
    height: 25px;
  }
  .photos {
    flex-direction: column;
    align-items: center;
  }
  .photos img {
    width: 200px;
    height: 200px;
  }
  .review .body {
    height: fit-content;
  }

  .code input {
    width: 100%;
  }

  .done {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }
  .done .footer button {
    width: 70%;
    margin: 10px 0;
  }
  .done .header {
    font-size: 1.2rem;
    text-align: center;
  }
  .done .body {
    font-size: 0.9rem;
  }
}
@media screen and (max-width: 540px) {
  .main {
    padding-top: 72px;
    min-height: 578px;
    height: auto;
  }
  .new-request {
    width: 92%;
    font-size: 70%;
  }
  .new-request .body {
    overflow-x: hidden;
  }
  .copyright {
    padding: 0 4%;
  }
  .footer button {
    width: 100%;
    font-size: 0.9rem;
    padding: 10px 15px;
  }
  .footer .next-prev {
    padding-left: 0px;
    padding-right: 0px;
  }
  .new-address button {
    width: 50%;
  }
  .review {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }

  .review .header {
    flex-direction: column;
  }
  ul {
    display: block;
  }
  .address i {
    background-repeat: no-repeat;
    background-size: contain;
    width: 35px;
    height: 25px;
  }
  .photos {
    flex-direction: column;
    align-items: center;
  }
  .photos img {
    width: 200px;
    height: 200px;
  }
  .review .body {
    height: fit-content;
  }
  .discount {
    flex-direction: column;
  }
  .code input {
    width: 70%;
  }

  .done {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }
  .done .footer button {
    width: 70%;
    margin: 10px 0;
  }
  .done .header {
    font-size: 1.2rem;
    text-align: center;
  }
  .done .body {
    font-size: 0.9rem;
  }
}
</style>