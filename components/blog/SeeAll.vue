<template>
  <div>
    <div class="cats">
      <div class="cleaning">
        <h3>نظافت و خانه‌داری</h3>

        <div class="cat-post-container" v-for="cat in cats" :key="cat.id">
          <a href="/blog/post">
            <img src="../../assets/cat.png" class="cat-img" />
            <div class="title-mid-post">{{ cat.title }}</div>
            <div class="desc-mid-post">
              <div class="right-mid-post">{{ cat.time }}</div>
              <div class="left-mid-post">{{ cat.date }}</div>
              <div class="clearfix"></div>
            </div>
          </a>
        </div>
        <center>
          <a href="">مشاهده بیشتر</a>
        </center>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Blog",
  data() {
    return {
      cats: [
        {
          id: 1,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 2,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 3,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 4,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 5,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 6,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 7,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 8,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 9,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 10,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 11,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 12,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 13,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 14,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 15,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 16,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 17,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 18,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 19,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 20,
          title: "چک لیست ضدعفونی کردن خانه ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
      ],
    };
  },
};
</script>

<style scoped>
@import url("bootstrap/dist/css/bootstrap.css");
a img {
  filter: brightness(70%);
  transition: ease 0.5s;
}
a:hover img {
  filter: brightness(30%);
  transition: ease 0.5s;
}
.cats {
  width: 100%;
  padding: 50px 11.5% 50px 11.5%;
  margin: 0px 0px 0px 0px;
  background-color: #fafafa;
  height: 1474px;
}

/* cats posts */
div.cat-post-container {
  position: relative;
  width: 24%;
  float: left;
  margin: 0px 5px 0px 5px;
}
div.cat-post-container .title-mid-post {
  position: absolute;
  bottom: 4rem;
  right: 20px;
  font-size: 18px;
  color: white !important;
}
div.cat-post-container .desc-mid-post {
  position: absolute;
  font-size: 14px;
  bottom: 15px;
  color: white !important;
}
div.cat-post-container .right-mid-post {
  position: absolute;
  bottom: 0px;
  right: 2rem;
  width: max-content;
  float: right;
}
div.cat-post-container .left-mid-post {
  position: absolute;
  bottom: 0px;
  left: -15rem;
  float: left;
}
img.cat-img {
  padding: 0px;
  margin: 5px;
  border-radius: 10px;
  width: 100%;
  height: 234px;
  display: block;
}

a {
  text-decoration: none !important;
  font-size: 16px;
  font-weight: 500;
  color: #000000;
  opacity: 0.8;
}
a:hover {
  text-decoration: underline !important;
  color: #5c438a !important;
  opacity: 1;
}
h3 {
  font-size: 28px;
  color: #5c438a;
  text-align: right;
  margin-bottom: 30px;
}

@media screen and (max-width: 500px) {
  div.cat-post-container {
    width: 100%;
    float: left;
  }
}
</style>