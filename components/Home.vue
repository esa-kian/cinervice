<template>
  <div class="content">
    <TechnicianNavbar v-if="type == 2" />
    <Navbar v-else />

    <div class="section-one">
      <div class="container-header">
        <div class="title">سخت نیست، فقط لِم داره…</div>
        <div class="caption">
          پیدا کردن متخصص و انجام امور شما، در کوتاه‌ترین زمان ممکن.
        </div>
        <div class="search">
          <form action="#">
            <div class="search-box">
              <div class="filter-search">
                <select class="filter-search">
                  <option
                    v-for="city in cities"
                    :key="city.id"
                    :value="city.id"
                  >
                    {{ city.title }}
                  </option>
                </select>
              </div>
              <input
                type="text"
                placeholder="سرویس مورد نظر خود را جستجو کنید…"
              />
              <button type="submit">جستجو</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="section-two">
      <div class="title">انجام درخواست شما در ۳ مرحله‌ی ساده</div>
      <div class="steps">
        <div class="step-one">
          <div class="number">
            <span>۱</span>
            <img
              src="../assets/Home/step1.png"
              alt=""
              width="225"
              height="150"
            />
          </div>
          <div class="head">ثبت پیشنهاد</div>
          <div class="body">
            نوع درخواست و قیمت پیشنهادی خود را انتخاب نموده و سفارش خود را ثبت
            نمایید.
          </div>
        </div>
        <div class="step-two">
          <div class="number">
            <span>۲</span>
            <img
              src="../assets/Home/step2.png"
              alt=""
              width="184"
              height="136"
            />
          </div>
          <div class="head">دریافت و بررسی پیشنهادات</div>
          <div class="body">
            بر اساس درخواست و پیشنهادات شما، متخصصین ما قیمیت های پیشنهادی خود
            را به شما ارائه میدهند.
          </div>
        </div>
        <div class="step-three">
          <div class="number">
            <span>۳</span>
            <img
              src="../assets/Home/step3.png"
              alt=""
              width="125"
              height="133"
            />
          </div>
          <div class="head">انتخاب متخصص و انجام کار</div>
          <div class="body">
            پس از انتخاب متخصص، در زمان تعیین شده درخواست شما انجام خواهد شد.
          </div>
        </div>
      </div>
    </div>
    <div class="section-three">
      <div class="download">
        <div class="title">اپلیکیشن لِمِ کار</div>
        <div class="body">
          اپلیکیشن لِمِ کار را برای آیفون و اندروید دانلود کنید و متخصص مورد نظر
          خود را در کوتاهترین زمان ممکن بیابید.
        </div>
        <div class="links">
          <a href=""><button class="android"></button></a>
          <a href=""><button class="ios"></button></a>
        </div>
      </div>
      <img src="../assets/Home/download.png" alt="" />
    </div>
    <div class="section-four">
      <div class="head">
        <div class="title">محبوب‌ترین دسته‌بندی ها</div>
        <div class="show-all">
          <router-link :to="'/categories'">
            مشاهده تمام دسته‌بندی ها
          </router-link>
        </div>
      </div>
      <PopularCats />
    </div>
    <div class="section-five">
      <div class="title">چرا لِمِ کار؟</div>
      <div class="body">
        <div class="why-icons">
          <div id="plumbing" alt="" />
          <div id="time" alt="" />
          <div id="sale" alt="" />
        </div>
        <div class="why-caption">
          <span>برترین نیروهای متخصص</span>
          <span>انجام درخواست در کوتاهترین زمان ممکن</span>
          <span>منصفانه‌ترین قیمت ها</span>
        </div>
      </div>
    </div>
    <div class="section-six">
      <div class="caption">
        <div class="title">متخصصین ما</div>
        <div class="body">
          لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده
          از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و
          سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای
          متنوع با هدف بهبود ابزارهای کاربردی می باشد.
        </div>
        <div class="join">
          <router-link :to="'/register/technician'">
            <button>پیوستن به متخصصین لِمِ کار</button>
          </router-link>
        </div>
      </div>
      <Slider />
    </div>
    <div class="section-seven">
      <div class="title">آخرین درخواست‌های انجام شده</div>
      <LastOrders />
    </div>
    <div class="section-eight">
      <div class="head">
        <div class="title">آخرین مطالب بلاگ</div>
        <div class="blog">
          <a href="">مشاهده بلاگ </a>
        </div>
      </div>
      <LastPostBlog />
    </div>
    <Footer />
  </div>
</template>

<script>
import LastOrders from "./home_page_sections/LastOrders";
import LastPostBlog from "./home_page_sections/LastPostBlog";
import PopularCats from "./home_page_sections/PopularCats";
import Slider from "./home_page_sections/Slider";
import Navbar from "./Navbar";
import TechnicianNavbar from "./panel/technician/Navbar";
import Footer from "./Footer";
import Axios from "axios";

export default {
  mounted() {
    this.fetchCities();
  },
  name: "Home",
  components: {
    LastOrders,
    LastPostBlog,
    PopularCats,
    Slider,
    Navbar,
    TechnicianNavbar,
    Footer,
  },
  methods: {
    fetchCities() {
      Axios.get(this.$hostname + "/cities")
        .then((resp) => {
          this.cities = resp.data.cities;
        })
        .catch((err) => {
          console.log(err, "can not fetch cities");
        });
    },
  },
  data() {
    return {
      type: localStorage.user_type,
      cities: null,
    };
  },
};
</script>

<style scoped>
.content {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  background-color: #f8f5fc;
  height: auto;
}
.section-one {
  width: 100%;
  height: 670px;
  background-image: url("../assets/Home/Bannerr.png");
  background-color: #fff;
  background-repeat: no-repeat;
  background-size: 690px;
  background-position-y: 70px;
  padding-top: 60px;
}
.section-one .container-header {
  display: flex;
  flex-direction: column;
  width: 50%;
  padding-right: 7%;
  padding-top: 220px;
}
.section-one .title {
  font-size: 2.3rem;
  font-weight: 500;
  color: #5c438a;
}
.section-one .caption {
  font-size: 1.2rem;
  opacity: 0.8;
}
.section-one .search {
  border-radius: 5px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  width: 80%;
  min-width: 500px;
  height: 50px;
  margin-top: 30px;
}
.section-one form {
  width: 100% !important;
  margin: 0 !important;
  height: 50px;
}
.search-box {
  display: flex;
}
.section-one .search-box .filter-search {
  border-left: 1px solid #5c438a1f;
  display: flex;
  min-width: 82px;
  width: 20%;
  height: 50px;
}
.section-one .search-box select.filter-search {
  outline: none;
  appearance: none;
  border: none;
  border-radius: 20px;
  background-image: url("../assets/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-y: 24px;
  background-position-x: 1em;
  background-size: 10px;
  cursor: pointer;
  background-color: #fff;
  font-size: 0.9rem;
  font-weight: 300;
  font-family: IRANSans;
  width: 100%;
  padding: 10px;
}
.section-one select option {
  background: #fff;
  color: #5c438a;
  width: 100px;
}

.section-one form .search-box input {
  outline: none;
  border: none;
  width: 70%;
  min-width: 284px;
  padding-right: 10px;
  font-family: IRANsans;
  font-size: 1rem;
  height: 50px;
}

.section-one form .search-box button {
  outline: none;
  border: none;
  background-color: #5c438aa8;
  color: #fff;
  font-size: 1.1rem;
  font-weight: 500;
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  padding-left: 25px;
  padding-right: 25px;
  cursor: pointer;
  transition: 0.4s ease;
  height: 50px;
  font-family: IRANsans;
}
.section-one form .search-box button:hover {
  background-color: #5c438a;
  transition: 0.4s ease;
}

.section-two {
  height: 432px;
  display: flex;
  flex-direction: column;
  padding: 50px 7%;
  background-image: url("../assets/Home/path.svg");
  background-position: center;
  background-repeat: no-repeat;
}
.section-two .title {
  font-size: 1.6rem;
  color: #5c438a;
  font-weight: 500;
  margin-bottom: 20px;
}
.section-two .steps {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  width: 100%;
}
.section-two .steps .step-one,
.section-two .steps .step-two,
.section-two .steps .step-three {
  width: 25%;
}
.section-two .steps span {
  font-size: 150px;
  font-weight: 500;
  color: #5c438a;
  line-height: 100px;
}
.section-two .steps .number {
  display: flex;
  align-items: baseline;
}

.section-two .steps .head {
  font-size: 1.1rem;
  font-weight: 500;
  color: #5c438a;
}
.section-two .steps .body {
  font-size: 1rem;
  color: #000;
}

.section-three {
  height: 339px;
  display: flex;
  justify-content: space-between;
  padding: 0 9%;
  background-color: #fff;
}
.section-three img {
  margin-top: 20px;
  width: 35%;
}
.section-three .download {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-top: 50px;
  width: 58%;
  height: 90%;
}
.section-three .download .title {
  color: #5c438a;
  font-size: 1.6rem;
}
.section-three .download .body {
  font-size: 1rem;
}
.section-three .download .links {
  display: flex;
  align-items: baseline;
  justify-content: center;
}
.section-three .download .links button {
  transition: 0.4s ease;
  width: 200px;
  height: 50px;
  outline: none;
  background-color: transparent;
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  cursor: pointer;
  border: none;
  margin: 3px;
}
.section-three .download .links button.ios {
  background-image: url("../assets/Home/ios.png");
}
.section-three .download .links button.ios:hover {
  background-image: url("../assets/Home/ios_hover.png");
  transition: 0.4s ease;
}
.section-three .download .links button.android {
  background-image: url("../assets/Home/android.png");
}
.section-three .download .links button.android:hover {
  background-image: url("../assets/Home/android_hover.png");
  transition: 0.4s ease;
}
.section-four {
  display: flex;
  flex-direction: column;
  height: 382px;
  padding: 50px 9%;
}
.section-four .head {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.section-four .head .title {
  font-size: 1.6rem;
  font-weight: 500;
  color: #5c438a;
}
.section-four .head a {
  opacity: 0.5;
  text-decoration: none;
  color: #000;
  font-size: 0.9rem;
  transition: 0.4s ease;
}
.section-four .head a:hover {
  opacity: 1;
  text-decoration: underline;
  color: #5c438a;
  transition: 0.4s ease;
}

.section-five {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 282px;
  padding: 50px 9%;
  background-color: #fff;
}

.section-five .title {
  font-size: 1.6rem;
  color: #5c438a;
  font-weight: 500;
}

.section-five .body {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.section-five .body .why-caption,
.section-five .body .why-icons {
  display: flex;
  justify-content: space-between;
  margin: auto;
  width: 75%;
}
.section-five .body .why-caption {
  z-index: 990;
}
.section-five .body .why-icons div {
  width: 150px;
  height: 150px;
  background-color: #f8f5fc;
  border-radius: 75px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 70px;
  opacity: 0.7;
  transition: 0.4s ease-out;
}
.section-five .body .why-icons div:hover {
  opacity: 1;
  transition: 0.5s ease-out;
  background-size: 90px;
  transform: rotate(360deg);
}
.section-five .body .why-icons #plumbing {
  background-image: url("../assets/Home/plumbing.png");
}
.section-five .body .why-icons #time {
  background-image: url("../assets/Home/time.png");
}
.section-five .body .why-icons #sale {
  background-image: url("../assets/Home/sale.png");
}

.section-six {
  display: flex;
  justify-content: space-between;
  padding: 50px 9%;
  height: 408px;
  width: 100%;
}
.section-six .caption {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 54%;
}
.section-six .caption .title {
  font-size: 1.6rem;
  color: #5c438a;
  font-weight: 500;
}

.section-six .caption .body {
  margin-top: 30px;
  margin-bottom: 70px;
}

.section-six .caption .join {
  margin: auto;
}
.section-six .caption .join button {
  outline: none;
  background-color: transparent;
  border: 2px solid #7ab383;
  color: #7ab383;
  font-family: IRANsans;
  border-radius: 10px;
  transition: 0.4s ease;
  cursor: pointer;
  padding: 11px 24px;
  font-size: 1rem;
}
.section-six .caption .join button:hover {
  background-color: #7ab383;
  color: #f8f5fc;
  transition: 0.4s ease;
}
.section-seven {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 325px;
  background-color: #fff;
  padding-top: 50px;
  width: 1366px;
  position: relative;
  overflow: hidden;
}
.section-seven .title {
  font-size: 1.6rem;
  color: #5c438a;
  font-weight: 500;
  padding: 0 9%;
}

.section-eight {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 560px;
  padding: 50px 9%;
  width: 100%;
}
.section-eight .head {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.section-eight .head .title {
  font-size: 1.6rem;
  font-weight: 500;
  color: #5c438a;
}
.section-eight .head a {
  opacity: 0.5;
  text-decoration: none;
  color: #000;
  font-size: 0.9rem;
  transition: 0.4s ease;
}
.section-eight .head a:hover {
  opacity: 1;
  text-decoration: underline;
  color: #5c438a;
  transition: 0.4s ease;
}
@media screen and (max-width: 540px) {
  .section-one {
    background-size: contain;
    height: 380px;
  }
  .section-one .container-header {
    background-color: rgba(255, 255, 255, 0.678);
    backdrop-filter: blur(2px) saturate(100%);
    width: 100%;
    padding-right: 5%;
    padding-top: 100px;
    height: 360px;
    position: absolute;
    text-align: center;
  }
  .section-one .title {
    font-size: 1.3rem;
  }
  .section-one .caption {
    font-size: 0.9rem;
    font-weight: bold;
  }
  .section-one .search {
    width: 95%;
    min-width: 200px;
    margin-top: 30px;
  }
  .section-one .search-box .filter-search {
    width: 30%;
    min-width: 50px;
  }
  .section-one .search-box select.filter-search {
    padding: 10px;
    /* min-height: 200px; */
  }
  .section-one form .search-box input {
    width: 70%;
    min-width: 100px;
    padding-right: 5px;
    font-size: 0.7rem;
  }
  .section-one form .search-box button {
    font-size: 0.8rem;
    padding-left: 5px;
    padding-right: 5px;
  }
  .section-two {
    height: fit-content;
    flex-direction: column;
  }
  .section-two .title {
    text-align: center;
    font-size: 1.2rem;
  }
  .section-two .steps {
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }
  .section-two .steps .step-one,
  .section-two .steps .step-two,
  .section-two .steps .step-three {
    text-align: center;
    width: 100%;
  }
  .section-two .steps span {
    line-height: 120px;
  }
  .section-two .steps .number {
    margin-top: 20px;
  }

  .section-two .steps .head {
    font-size: 1.1rem;
    font-weight: 500;
    color: #5c438a;
  }
  .section-two .steps .body {
    font-size: 1rem;
    color: #000;
  }
  .section-three {
    text-align: center;
    height: fit-content;
    flex-direction: column;
  }
  .section-three img {
    margin-top: 20px;
    width: 100%;
  }
  .section-three .download {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    padding-top: 20px;
  }
  .section-three .download .title {
    font-size: 1.2rem;
  }
  .section-three .download .body {
    margin: 20px 0;
    font-size: 0.9rem;
  }
  .section-three .download .links {
    display: flex;
    align-items: center;
    width: 100%;
  }
  .section-three .download .links button {
    transition: 0.4s ease;
    width: 133px;
    height: 38px;
    outline: none;
    background-color: transparent;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    cursor: pointer;
    border: none;
    margin: 3px;
  }
  .section-four {
    height: fit-content;
  }
  .section-four .head {
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
  .section-four .head .title {
    font-size: 1.2rem;
  }
  .section-four .head a {
    font-size: 0.7rem;
  }

  .section-four .body {
    justify-content: center;
  }

  .section-four .cat-card .icon {
    background-size: 90px;
    padding: 3.5rem;
  }

  .section-five {
    text-align: center;
    height: fit-content;
    padding: 20px 4%;
  }

  .section-five .title {
    font-size: 1.2rem;
    margin-bottom: 20px;
  }

  .section-five .body {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  .section-five .body .why-caption,
  .section-five .body .why-icons {
    width: 100%;
  }
  .section-five .body .why-caption span {
    max-width: 90px;
    font-size: 0.8rem;
  }
  .section-five .body .why-icons div {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    background-size: 45px;
  }
  .section-five .body .why-icons div:hover {
    background-size: 50px;
  }
  .section-six {
    padding: 20px 4%;
    height: fit-content;
    flex-direction: column;
    text-align: center;
  }
  .section-six .caption {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  .section-six .caption .title {
    font-size: 1.2rem;
  }
  .section-six .caption .body {
    margin-top: 20px;
    margin-bottom: 40px;
  }
  .section-six .caption .join button {
    margin-bottom: 20px;
  }
  .section-seven {
    padding-top: 20px;
    height: 260px;
  }
  .section-seven .title {
    font-size: 1.2rem;
    padding: 0 4%;
  }
  .section-eight {
    height: fit-content;
    padding: 30px 9%;
    text-align: center;
  }
  .section-eight .head {
    flex-direction: column;
  }
  .section-eight .head .title {
    font-size: 1.2rem;
  }
  .section-eight .head a {
    font-size: 0.7rem;
  }
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .section-one {
    background-size: contain;
    height: 380px;
  }
  .section-one .container-header {
    background-color: rgba(255, 255, 255, 0.678);
    backdrop-filter: blur(2px) saturate(100%);
    width: 100%;
    padding-right: 5%;
    padding-top: 100px;
    height: 360px;
    position: absolute;
  }
  .section-one .title {
    font-size: 1.3rem;
  }
  .section-one .caption {
    font-size: 0.9rem;
    font-weight: bold;
  }
  .section-one .search {
    width: 60%;
    min-width: 200px;
    margin-top: 30px;
  }
  .section-one .search-box .filter-search {
    width: 30%;
    min-width: 50px;
  }
  .section-one .search-box select.filter-search {
    padding: 10px;
  }
  .section-one form .search-box input {
    width: 63%;
    min-width: 100px;
    padding-right: 5px;
    font-size: 0.7rem;
  }
  .section-one form .search-box button {
    font-size: 0.8rem;
    padding-left: 5px;
    padding-right: 5px;
  }

  .section-two .steps .head {
    font-size: 0.9rem;
    font-weight: 500;
    color: #5c438a;
  }
  .section-two .steps .body {
    font-size: 0.9rem;
    color: #000;
  }
  .section-two .steps span {
    line-height: 120px;
    font-size: 120px;
  }
  .section-three {
    height: 212px;
  }
  .section-three .download .body {
    margin: 10px 0;
    font-size: 0.9rem;
  }
  .section-three .download .links button {
    width: 113px;
    height: 28px;
  }
  .section-four {
    height: 535px;
  }
  .section-five {
    height: 300px;
  }

  .section-five .body .why-caption,
  .section-five .body .why-icons {
    width: 100%;
  }
  .section-six {
    height: fit-content;
  }
  .section-six .caption {
    width: 50%;
  }
  .section-seven .title {
    padding: 0 5%;
  }
}
</style>
