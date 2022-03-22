<template>
  <div class="footer">
    <div class="info">
      <div class="col-one">
        <div class="logo"></div>
        <div class="content">
          {{ bio }}
        </div>
      </div>
      <div class="col-two">
        <ul>
          <li>
            <router-link :to="'/about'"> درباره ما </router-link>
          </li>
          <li>
            <router-link :to="'/policy'"> شرایط استفاده </router-link>
          </li>
          <li>
            <router-link :to="'/register/technician'">
              ثبت‌نام متخصصین
            </router-link>
          </li>
          <li>
            <router-link :to="'/faq'"> سوالات متداول </router-link>
          </li>
          <li>
            <router-link :to="'/blog'"> بلاگ</router-link>
          </li>
        </ul>
      </div>
      <div class="col-three">
        <div class="title">تماس با ما</div>
        <div class="address">
          {{ address }}
        </div>
        <div class="phone-number">
          <label for="">تلفن :</label>
          <span>{{ phone_number }}</span>
        </div>
        <div class="email">
          <label for="">ایمیل :</label>
          <span>{{ email }}</span>
        </div>
      </div>
      <div class="col-four">
        <div class="e-symbol"></div>
      </div>
    </div>
    <Copyright />
  </div>
</template>

<script>
import Copyright from "./Copyright";
import Axios from "axios";

export default {
  name: "Footer",
  components: {
    Copyright,
  },
  data() {
    return {
      settings: null,
      phone_number: null,
      telephone: null,
      address: null,
      email: null,
      bio: null,
    };
  },
  mounted() {
    Axios.get(this.$hostname + "/settings")
      .then((resp) => {
        this.settings = resp.data.settings;
        this.settings.forEach((element) => {
          if (element.type == "phone_number") {
            this.phone_number = element.value;
          }
          if (element.type == "telephone") {
            this.telephone = element.value;
          }
          if (element.type == "address") {
            this.address = element.value;
          }
          if (element.type == "email") {
            this.email = element.value;
          }
          if (element.type == "bio") {
            this.bio = element.value;
          }
        });
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.footer {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  padding: 20px 11.5%;
}
.info {
  min-height: 230px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
}

.info .col-one {
  width: 27%;
  font-size: 14px;
  flex-direction: row;
}
.info .col-one .logo {
  background-image: url("../assets/logo.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  height: 70px;
  margin-bottom: 10px;
}

.info .col-two {
  width: 15%;
}

.info .col-two ul {
  margin: 0;
  padding: 0;
}
.info .col-two ul a {
  text-decoration: none;
  color: #000;
}
.info .col-two ul li {
  font-size: 14px;
  margin: 0px;
  padding: 0px;
  margin-bottom: 15px;
}
::marker {
  color: #5c438a;
  font-size: 14px;
  margin: 0px;
  padding: 0px;
}
.info .col-three {
  width: 25%;
  font-size: 14px;
}
.info .col-three div {
  margin-bottom: 15px;
}
.info .col-three .title {
  font-size: 21px;
  color: #5c438a;
  margin-bottom: 10px;
}
.info .col-three label {
  margin-left: 15px;
}

.info .col-four {
  width: 20%;
  margin-top: 10px;
  justify-content: center;
  align-items: center;
}
.e-symbol {
  background-image: url("../assets/enamad.png");
  background-size: contain;
  background-repeat: no-repeat;
  height: 90px;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .footer {
    padding: 15px 4%;
  }
  .info {
    height: fit-content;
    flex-direction: column;
  }
  .info .col-one {
    text-align: center;
    width: 100%;
    font-size: 0.9rem;
  }
  .info .col-two {
    width: 100%;
  }
  .info .col-two ul {
    margin: 20px 2rem;
  }
  .info .col-two ul li {
    font-size: 1.1rem;
    margin-bottom: 10px;
  }
  .info .col-three {
    width: 100%;
    font-size: 0.9rem;
  }

  .info .col-three .title {
    font-size: 1.4rem;
  }
  .info .col-four {
    width: 100%;
    height: 200px;
    margin: auto;
  }
  .e-symbol {
    /* background-size: 90px 200px; */
    width: 100%;
    height: 200px;
  }
}
@media screen and (max-width: 540px) {
  .footer {
    padding: 15px 4%;
  }
  .info {
    height: fit-content;
    flex-direction: column;
  }
  .info .col-one {
    text-align: center;
    width: 100%;
    font-size: 0.9rem;
  }
  .info .col-two {
    width: 100%;
  }
  .info .col-two ul {
    margin: 20px 2rem;
  }
  .info .col-two ul li {
    font-size: 1.1rem;
    margin-bottom: 10px;
  }
  .info .col-three {
    width: 100%;
    font-size: 0.9rem;
  }

  .info .col-three .title {
    font-size: 1.4rem;
  }
  .info .col-four {
    width: 100%;
    height: 200px;
    margin: auto;
  }
  .e-symbol {
    /* background-size: 90px 200px; */
    width: 100%;
    height: 200px;
  }
}
</style>