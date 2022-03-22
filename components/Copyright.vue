<template>
  <div class="content-copy">
    <div class="copyright">{{ copyright }}</div>
    <div class="social-network">
      <div class="caption">{{ social_network }}</div>
      <div class="icons">
        <a :href="'https://twitter.com/' + twitter"
          ><div class="twitter"></div
        ></a>
        <a :href="'https://t.me/' + telegram"> <div class="telegram"></div></a>
        <a :href="'https://linkedin.com/' + linkedin"
          ><div class="linkedin"></div
        ></a>
        <a :href="'https://instagram.com/' + instagram"
          ><div class="instagram"></div
        ></a>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "Copyright",
  data() {
    return {
      copyright: "تمام حقوق متعلق به شرکت جوانفکران داده گستر (ویستا) میباشد.",
      social_network: "لِمِ کار در شبکه های اجتماعی:",
      settings: null,
      instagram: null,
      telegram: null,
      linkedin: null,
      twitter: null,
    };
  },
  mounted() {
    Axios.get(this.$hostname + "/settings")
      .then((resp) => {
        this.settings = resp.data.settings;
        this.settings.forEach((element) => {
          if (element.type == "instagram") {
            this.instagram = element.value;
          }
          if (element.type == "telegram") {
            this.telegram = element.value;
          }
          if (element.type == "linkedin") {
            this.linkedin = element.value;
          }
          if (element.type == "twitter") {
            this.twitter = element.value;
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
.content-copy {
  text-align: right;
  font-size: 0.8rem;
  font-weight: 300;
  width: 100%;
  max-width: 1366px;
  margin: auto;
  display: flex;
  justify-content: space-between;
  color: #5c438a;
  margin-top: 10px;
  border-top: #5c438a23 2px solid;
  padding: 10px 0;
}
.social-network {
  display: flex;
  align-items: center;
  width: 30%;
  justify-content: space-between;
}
.icons {
  display: flex;
  width: 40%;
  justify-content: space-between;
}
.icons div {
  background-size: 20px;
  background-repeat: no-repeat;
  width: 20px;
  height: 20px;
  cursor: pointer;
  transition: 0.4s ease;
}
.icons div:hover {
  transition: 0.4s ease;
}
.telegram {
  background-image: url("../assets/footer/Not_Hovered/Telegram.svg");
}
.twitter {
  background-image: url("../assets/footer/Not_Hovered/Twitter.svg");
}
.linkedin {
  background-image: url("../assets/footer/Not_Hovered/Linkedin.svg");
}
.instagram {
  background-image: url("../assets/footer/Not_Hovered/Instagram.svg");
}
.telegram:hover {
  background-image: url("../assets/footer/User_Hovered/Telegram.svg");
}
.twitter:hover {
  background-image: url("../assets/footer/User_Hovered/Twitter.svg");
}
.linkedin:hover {
  background-image: url("../assets/footer/User_Hovered/Linkedin.svg");
}
.instagram:hover {
  background-image: url("../assets/footer/User_Hovered/Instagram.svg");
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .social-network {
    width: 38%;
  }
}
@media screen and (max-width: 540px) {
  .content-copy {
    flex-direction: column;
  }
  .social-network {
    width: 100%;
  }
  .icons {
    width: 30%;
  }
}
</style>