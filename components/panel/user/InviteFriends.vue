<template>
  <div class="invite">
    <div class="user">
      <div class="title">با معرفی مشتری به لِمِ کار کسب درآمد کنید.</div>
      <div class="body">
        شما می‌توانید با ارسال لینک دعوت به دوستان خود، به تعداد نامحدود با هر
        ثبت سفارش آنها درآمد کسب کنید. لِمِ کار در هر سفارش دوستان شما، ۲۰ درصد
        درآمد خود را به عنوان اعتبار به شما پرداخت می‌کند. تمامی درآمدی که کسب
        می‌کنید، در اعتبار شما شارژ می‌شود که هم می‌توانید از آن برای دریافت
        خدمات لِمِ کار استفاده کنید و هم مبلغ افزوده را در صورتی که بیش از ۱۰۰
        هزار تومان شود، برداشت نمایید.
      </div>
      <div class="discount">
        <div class="invite">کد دعوت</div>
        <div @click.prevent="copyTextUser" class="discount_code">
          <div>
            <input id="discount_user" v-model="invite_code" readonly />
          </div>
          <div class="copy-icon">کپی</div>
        </div>
        <div class="social">
          <a :href="'https://telegram.me/share/url?url=' + invite_code">
            <div class="telegram"></div
          ></a>

          <a :href="'whatsapp://send?text=' + invite_code"
            ><div class="whatsapp"></div>
          </a>
        </div>
      </div>
    </div>
    <div class="technician">
      <div class="title">با معرفی متخصص به لِمِ کار کسب درآمد کنید.</div>
      <div class="body">
        شما می‌توانید با ارسال لینک دعوت به دوستان متخصص خود، به محض ثبت نام
        متخصص در لِمِ کار ۲,۰۰۰ تومان دریافت کنید. همچنین پس از انجام اولین
        سفارش توسط متخصص، در صورتی که او تخصص نظافت داشته باشد، ۳۰,۰۰۰ تومان و
        در غیر این صورت ۱۵ هزار تومان به شما تعلق میگیرد.
      </div>
      <div class="discount">
        <div class="invite">کد دعوت</div>
        <div @click.prevent="copyTextTechnician" class="discount_code">
          <input id="discount_technician" v-model="invite_code" readonly />
          <span class="copy-icon">کپی</span>
        </div>
        <div class="social">
          <a :href="'https://telegram.me/share/url?url=' + invite_code">
            <div class="telegram"></div
          ></a>

          <a :href="'whatsapp://send?text=' + invite_code"
            ><div class="whatsapp"></div>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "InviteFriends",
  data() {
    return {
      invite_code: null,
    };
  },
  mounted() {
    this.inviteCode();
  },
  methods: {
    inviteCode() {
      Axios.get(this.$hostname + "/invite-code", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.invite_code =
            "https://lemekar.ir/" + resp.data.invite_code[0].code;
        })
        .catch((err) => {
          console.log(err, "can not fetch invite code");
        });
    },
    copyTextUser: () => {
      let copiedText = document.getElementById("discount_user");
      copiedText.select();
      document.execCommand("copy");
    },
    copyTextTechnician: () => {
      let copiedText = document.getElementById("discount_technician");
      copiedText.select();
      document.execCommand("copy");
    },
  },
};
</script>

<style scoped>
.invite {
  padding: 50px 8.5%;
}
.title {
  margin-bottom: 15px;
  font-size: 22px;
  font-weight: 500;
  color: #5c438a;
}
.discount {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
  flex-wrap: wrap;
  width: 55%;
  margin-top: 30px;
  margin-bottom: 50px;
}
.discount .invite {
  display: flex;
  padding: 0;
}
.discount .discount_code {
  display: flex;
  justify-content: space-between;
  flex-direction: row-reverse;
  border: #5c438a6c 2px solid;
  opacity: 0.8;
  border-radius: 5px;
  width: 250px;
  padding: 5px 35px 5px 10px;
  background-image: url("../../../assets/copy.svg");
  background-repeat: no-repeat;
  background-position: right;
  background-position-x: 220px;
  cursor: pointer;
  transition: 0.4s ease;
}
.discount .discount_code:hover {
  border: #5c438a 2px solid;
  transition: 0.4s ease;
  opacity: 1;
}
.discount .discount_code input {
  text-align: left;
  outline: none;
  border: none;
  background: none;
}
.discount .discount_code .copy-icon {
  display: flex;
}
.telegram {
  background-image: url("../../../assets/panel/telegram.png");
  background-size: contain;
  background-repeat: no-repeat;
  height: 25px;
  width: 25px;
}
.whatsapp {
  background-image: url("../../../assets/panel/whatsapp.svg");
  background-size: contain;
  background-repeat: no-repeat;
  height: 25px;
  width: 25px;
}
.social {
  display: flex;
  flex-wrap: wrap;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .invite {
    padding: 30px 4%;
  }
}
@media screen and (max-width: 540px) {
  .invite {
    padding: 30px 4%;
  }
  .discount {
    flex-direction: column;
    width: 80%;
  }
  .discount .discount_code {
    padding: 5px 10px 5px 10px;
    width: 100%;
    background-position-x: right;
  }
  .discount .discount_code input {
    width: 100%;
  }
  .discount .discount_code .copy-icon {
    display: flex;
    padding-right: 10%;
  }
}
</style>
