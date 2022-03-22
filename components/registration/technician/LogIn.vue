<template>
  <div>
    <Navbar />
    <div class="main">
      <div class="login">
        <div class="header">
          <transition name="fade">
            <div v-if="step == 1">ورود یا ثبت‌نام متخصصین</div>
          </transition>
          <transition name="fade">
            <div v-if="step == 2">کد یکبار مصرف</div>
          </transition>

          <div v-if="step == 3">ثبت نام متخصصین</div>
        </div>
        <div class="body">
          <div v-if="step == 1">
            <div class="desc">
              برای ورود و یا ثبت نام، شماره تلفن همراه خود را وارد کنید.
            </div>
            <div class="phone">
              <label for="phone_number">شماره تلفن همراه</label>
              <input
                maxlength="11"
                type="text"
                id="phone_number"
                placeholder=" مانند :۰۹۱۲۱۲۳۴۵۶۷"
                v-model="phone_number"
                @input="validation"
              />
            </div>
            <span v-if="!valid" class="error">{{ message }}</span>
          </div>

          <div v-if="step == 2">
            <div class="desc">
              کد ۶ رقمی یکبار مصرفی که به شماره {{ phone_number }} ارسال شده است
              را وارد نمایید.
            </div>
            <div class="otp">
              <div class="pin-code">
                <input
                  @input="$event.target.nextElementSibling.focus()"
                  type="text"
                  maxlength="1"
                  v-model="otp1"
                />
                <input
                  @input="$event.target.nextElementSibling.focus()"
                  type="text"
                  maxlength="1"
                  v-model="otp2"
                />
                <input
                  @input="$event.target.nextElementSibling.focus()"
                  type="text"
                  maxlength="1"
                  v-model="otp3"
                />
                <input
                  @input="$event.target.nextElementSibling.focus()"
                  type="text"
                  maxlength="1"
                  v-model="otp4"
                />
                <input
                  @input="$event.target.nextElementSibling.focus()"
                  type="text"
                  maxlength="1"
                  v-model="otp5"
                />
                <input
                  @input="$event.target.nextElementSibling.focus()"
                  type="text"
                  maxlength="1"
                  v-model="otp6"
                />
              </div>
              <div class="resend">
                <a
                  @click.prevent="resendOtp"
                  :class="{ can_resend: resend, cant_resend: !resend }"
                  >ارسال مجدد</a
                >
                <span class="timer">{{ time_left }} ثانیه</span>
              </div>
              <span v-if="resend_success" class="success">{{ message }}</span>
              <span v-if="!valid" class="error">{{ message }}</span>
            </div>
          </div>

          <div v-if="step == 3">
            <div class="information">
              <label for="first_name">نام</label>
              <input type="text" id="first_name" v-model="first_name" />
              <label for="first_name">نام خانوادگی</label>
              <input type="text" id="first_name" v-model="last_name" />
              <div class="location-craft">
                <div class="location">
                  <label for="location">شهر محل سکونت</label>
                  <select name="location" id="location" v-model="city_id">
                    <option
                      v-for="city in cities"
                      :key="city.id"
                      :value="city.id"
                    >
                      {{ city.title }}
                    </option>
                  </select>
                </div>
                <div class="craft">
                  <label for="craft">تخصص</label>
                  <select name="craft" id="craft" v-model="proficiency_id">
                    <option
                      v-for="proficiency in proficiencies"
                      :key="proficiency.id"
                      :value="proficiency.id"
                    >
                      {{ proficiency.title }}
                    </option>
                  </select>
                </div>
              </div>
              <label for="first_name">کد دعوت (اختیاری)</label>
              <input type="text" id="first_name" v-model="invite_code" />
            </div>
          </div>
        </div>
        <div class="footer">
          <button :class="{ valid: valid }" @click="login">ادامه</button>
          <div class="policy">
            با ورود و یا ثبت نام در لِمِ کار شما
            <a href="/policy"> قوانین و شرایط استفاده </a>
            از سرویس های سایت را می‌پذیرید.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../Navbar";
import Axios from "axios";

export default {
  name: "LogIn",
  components: {
    Navbar,
  },
  mounted() {
    this.fetchProficiencies();
    this.fetchCities();
  },
  updated() {
    this.checkCodeFill();
  },
  methods: {
    timer() {
      if (this.time_left > 0) {
        setTimeout(() => {
          this.time_left -= 1;
          this.timer();
        }, 1000);
      } else {
        this.resend = true;
      }
    },
    validation() {
      if (
        parseInt(this.phone_number.substring(0, 1)) !== 0 ||
        parseInt(this.phone_number.substring(1, 2)) !== 9
      ) {
        this.valid = false;
        this.message = "شماره تلفن همراه نامعتبر است";
      } else {
        if (this.phone_number.length == 11) {
          this.valid = true;
          this.message = "";
        } else {
          this.valid = false;
        }
      }
    },
    checkCodeFill() {
      if (
        this.otp1 &&
        this.otp2 &&
        this.otp3 &&
        this.otp4 &&
        this.otp5 &&
        this.otp6
      ) {
        this.valid = true;
        this.verifyOtp();
      }
    },
    fetchProficiencies() {
      Axios.get(this.$hostname + "/proficiencies")
        .then((resp) => {
          this.proficiencies = resp.data.proficiencies;
        })
        .catch((err) => {
          console.log(err, "can not fetch proficiencies");
        });
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
    login() {
      if (this.step == 1 && this.valid) {
        this.demandOtp();
      }
      if (this.step == 2 && this.valid) {
        this.verifyOtp();
      }
      if (this.step == 3 && this.valid) {
        this.register();
      }
    },
    resendOtp() {
      let data = {
        phone_number: this.phone_number,
      };
      Axios.post(this.$hostname + "/send-otp", data)
        .then(({ data }) => {
          console.log(data);
          this.timer();
          this.valid = true;
          this.resend_success = true;
          this.message = "کد جدید ارسال شد";
        })
        .catch((err) => {
          this.valid = false;
          this.message = "تا یک ساعت آینده امکان ارسال کد برای شما نیست";
        });
    },
    demandOtp() {
      let data = {
        phone_number: this.phone_number,
      };
      Axios.post(this.$hostname + "/send-otp", data)
        .then(({ data }) => {
          console.log(data);

          this.valid = false;
          this.step++;
          this.timer();
        })
        .catch(({ err }) => {
          console.log(err);
          this.valid = false;
          this.message = "تا یک ساعت آینده امکان ارسال کد برای شما نیست";
        });
    },
    verifyOtp() {
      let data = {
        phone_number: this.phone_number,
        type: this.type,
        otp:
          this.otp1 + this.otp2 + this.otp3 + this.otp4 + this.otp5 + this.otp6,
      };
      Axios.post(this.$hostname + "/verify-otp", data)
        .then(({ data }) => {
          if (data.token) {
            localStorage.setItem("isAuth", true);
            localStorage.setItem(
              "name",
              JSON.stringify(data.name.first_name + " " + data.name.last_name)
            );
            localStorage.setItem("token", JSON.stringify(data.token));
            localStorage.setItem("user_type", 2);
            this.$router.push("/panel/technician");
          } else {
            this.valid = false;
            this.step++;
          }
        })
        .catch(({ err }) => {
          this.otp1 = null;
          this.otp2 = null;
          this.otp3 = null;
          this.otp4 = null;
          this.otp5 = null;
          this.otp6 = null;
          this.valid = false;
          this.message = "کد وارد شده اشتباه است";
          console.log(err);
        });
    },
    register() {
      let data = {
        first_name: this.first_name,
        last_name: this.last_name,
        type: this.type,
        phone_number: this.phone_number,
        invite_code: this.invite_code,
        city_id: this.city_id,
        proficiency_id: this.proficiency_id,
      };
      Axios.post(this.$hostname + "/sign-up", data)
        .then(({ data }) => {
          if (data.token) {
            localStorage.setItem("isAuth", true);
            localStorage.setItem(
              "name",
              JSON.stringify(data.name.first_name + " " + data.name.last_name)
            );
            localStorage.setItem("token", JSON.stringify(data.token));
            localStorage.setItem("user_type", 2);
            this.$router.push("/panel/technician");
          } else {
            this.valid = false;
            this.message = "خطایی رخ داد لطفا بعدا تلاش مجدد کنید";
          }
        })
        .catch(({ err }) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      proficiencies: null,
      cities: [],
      step: 1,
      phone_number: null,
      type: 2,
      otp1: null,
      otp2: null,
      otp3: null,
      otp4: null,
      otp5: null,
      otp6: null,
      first_name: null,
      last_name: null,
      invite_code: null,
      city_id: null,
      proficiency_id: null,
      valid: null,
      message: "",
      time_left: 120,
      resend: false,
      resend_success: false,
    };
  },
};
</script>

<style scoped>
.main {
  width: 100%;
  height: 100vh;
  margin: 0px 0px 0px 0px;
  background-color: #f7fff9;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  align-content: space-between;
}
.main .login {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 110px;
  flex-direction: column;
  align-content: space-between;
  background-color: #fff;
  width: 32%;
  max-width: 425px;
  min-height: 410px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  padding: 34px;
}

.main .login .header {
  display: flex;
  justify-content: center;
  font-size: 24px;
  font-weight: 500;
  min-height: 36px;
  margin-bottom: 30px;
  color: #7ab383;
}

.header div {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}

.main .login .body {
  display: flex;
  flex-direction: column;
  width: 100%;
  font-size: 0.9em;
}
/* 
step 3 styles 
*/
.information {
  display: flex;
  flex-direction: column;
}
.information label {
  margin-bottom: 10px;
}
.information input {
  justify-content: right;
  text-align: right;
  margin-bottom: 20px;
}
.location-craft {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
.location-craft .craft {
  display: flex;
  flex-direction: column;
  width: 60%;
}
.location-craft .location {
  display: flex;
  flex-direction: column;
  width: 38%;
}
select {
  background-image: url("../../../assets/FAQ/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-x: 15px;
  background-position-y: 15px;
  background-size: 15px;
  width: 500px;
  outline: none;
  appearance: none;
  border: solid 2px #7ab38333;
  background-color: #fff;
  border-radius: 5px;
  height: 44px;
  font-size: 14px;
  font-weight: 500;
  margin-top: 10px;
  margin-bottom: 20px;
  font-family: IRANSans;
  padding-right: 10px;
  width: 100%;
  transition: 0.3s ease;
}
select option {
  background: #7ab38333;
  color: #7ab383;
}
select:hover {
  border: solid 2px #7ab383;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.3s ease;
}
/* 
step 2 styles 
*/
.otp .pin-code {
  display: flex;
  justify-content: space-between;
  flex-direction: row-reverse;
  margin-top: 30px;
  margin-bottom: 12px;
}
.otp input {
  max-width: 15%;
}
.otp .resend {
  display: flex;
  justify-content: space-between;
}
.otp .resend a {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
.can_resend {
  opacity: 1;
}
.cant_resend {
  opacity: 0.5;
}
/* 
step 1 styles 
*/
.main .login .body .phone {
  display: flex;
  flex-direction: column;
  margin-top: 20px;
}
.main .login .body .phone label {
  margin-bottom: 10px;
  opacity: 0.8;
}
.main .login .body input {
  outline: none;
  text-align: left;
  padding: 8px 18px;
  font-size: 18px;
  font-family: IRANsans;
  border-radius: 5px;
  border: 2px solid #7ab38333;
  transition: 0.4s ease;
}
.main .login .body input:focus {
  border: 2px solid #7ab383;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.171);
  transition: 0.4s ease;
}

.main .login .body .desc {
  text-align: center;
}

.main .login .footer {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.main .login .footer .policy {
  font-size: 12px;
}
.footer button {
  display: flex;
  background-color: #7ab383;
  border: 2px solid #7ab383;
  opacity: 0.5;
  margin: 30px 15px 20px 15px;
  width: 100%;
  outline: none;
  cursor: pointer;
  justify-content: center;
  border-radius: 5px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  transition: 0.4s ease;
  padding: 10px 20px;
  font-family: IRANsans;
}
.valid {
  opacity: 1 !important;
  transition: 0.4s ease;
}
span.error {
  color: #8f2222;
}
span.success {
  color: rgb(31, 129, 31);
}
.footer a {
  color: #7ab383;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .main .login {
    margin-top: 100px;
    width: 90%;
    padding: 25px;
  }
}
@media screen and (max-width: 540px) {
  .main .login {
    margin-top: 100px;
    width: 90%;
    padding: 25px;
  }
}
</style>