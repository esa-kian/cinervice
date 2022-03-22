<template>
  <div class="container">
    <Navbar />

    <div class="faq">
      <h3>سؤالات متداول</h3>
      <div role="tablist">
        <div
          v-for="(message, index) in messages"
          :item="message.id"
          :key="message.id"
        >
          <b-card no-body>
            <b-card-header header-tag="header" role="tab">
              <a @click.prevent="setActive(message.id)" href>
                <b-button
                  block
                  v-b-toggle="'accordion-' + index"
                  variant="info"
                >
                  <div class="title">
                    <div class="right-side">
                      <div class="question"></div>
                      {{ message.title }}
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
                <b-card-text>{{ message.body }}</b-card-text>
              </b-card-body>
            </b-collapse>
          </b-card>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from "../Navbar";
import Footer from "../Footer";

export default {
  name: "Faq",
  components: {
    Navbar,
    Footer,
  },
  data() {
    return {
      messages: [
        {
          id: 1,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 2,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 3,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 4,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 5,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 6,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 7,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 8,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 9,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
        {
          id: 10,
          title: "نحوه ثبت درخواست به چه صورت میباشد؟",
          body:
            "کاربری در تاریخ 3 خرداد ماه 1399 ساعت 10 و 46 دقیقه و 24 ثانیه با اطلاعات کاربری شما وارد سامانه شد، لطفا اگر احساس می کنید این ورود توسط شما نبوده است ، نسبت به تعویض رمز عبور خود در اولین فرصت اقدام نمایید.",
        },
      ],
      id: null,
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
.card-body {
  transition: 0.3s ease !important;
}
.title {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.title .right-side {
  display: flex;
  align-items: center;
}
.title .right-side .question {
  background-image: url("../../assets/FAQ/Question.svg");
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
  .container {
    padding: 0px;
  }
  .faq {
    padding: 80px 4% 30px 4%;
  }
  .question {
    height: 25px;
    width: 25px;
    margin-left: 15px;
  }
}
@media screen and (max-width: 540px) {
  .container {
    padding: 0px;
  }
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
