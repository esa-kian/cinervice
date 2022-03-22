<template>
  <div>
    <Navbar />
    <div class="blog">
      <div class="top-right">
        <div class="post-container">
          <a href="/blog/post">
            <img src="../../assets/post.png" class="big-top" />
            <div class="title-big-post">راهنمای تمیز کردن کفپوش چوبی</div>
            <div class="desc-big-post">
              <div class="right-big-post">۱۰ دقیقه</div>
              <div class="left-big-post">۴ مرداد ۱۳۹۹</div>
              <div class="clearfix"></div>
            </div>
          </a>
        </div>
      </div>
      <div class="top-left">
        <div class="post-container">
          <a href="/blog/post">
            <img src="../../assets/post.png" class="mid-top" />
            <div class="title-mid-post">راهنمای تمیز کردن کفپوش چوبی</div>
            <div class="desc-mid-post">
              <div class="right-mid-post">۱۰ دقیقه</div>
              <div class="left-mid-post">۴ مرداد ۱۳۹۹</div>
              <div class="clearfix"></div>
            </div>
          </a>
        </div>
        <div class="post-container">
          <a href="/blog/post">
            <img src="../../assets/post.png" class="mid-top" />
            <div class="title-mid-post">راهنمای تمیز کردن کفپوش چوبی</div>
            <div class="desc-mid-post">
              <div class="right-mid-post">۱۰ دقیقه</div>
              <div class="left-mid-post">۴ مرداد ۱۳۹۹</div>
              <div class="clearfix"></div>
            </div>
          </a>
        </div>
      </div>
      <div class="clearfix"></div>
    </div>

    <div class="chief">
      <h3>منتخب سردبیر</h3>
      <div class="post-container" v-for="post in chief_post" :key="post.id">
        <a href="/blog/post">
          <img src="../../assets/chief.png" class="chief-img" />
          <div class="title-mid-post">{{ post.title }}</div>
          <div class="desc-mid-post">
            <div class="right-mid-post">{{ post.time }}</div>
            <div class="left-mid-post">{{ post.date }}</div>
            <div class="clearfix"></div>
          </div>
        </a>
      </div>
    </div>

    <div class="cats">
      <div class="cleaning">
        <div class="header">
          <h3>نظافت و خانه‌داری</h3>
        </div>
        <div class="show-all">
          <a href="/blog/all">مشاهده دسته‌بندی</a>
        </div>
        <div class="clearfix"></div>

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
      </div>
      <div class="decoration">
        <div class="header">
          <h3>دکوراسیون و چیدمان</h3>
        </div>
        <div class="show-all">
          <a href="/blog/all">مشاهده دسته‌بندی</a>
        </div>
        <div class="clearfix"></div>

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
      </div>

      <div class="mind-health">
        <div class="header">
          <h3>سلامت ذهن</h3>
        </div>
        <div class="show-all">
          <a href="/blog/all">مشاهده دسته‌بندی</a>
        </div>
        <div class="clearfix"></div>

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
      </div>

      <div class="skincare">
        <div class="header">
          <h3>مراقبت پوست و مو</h3>
        </div>
        <div class="show-all">
          <a href="/blog/all">مشاهده دسته‌بندی</a>
        </div>
        <div class="clearfix"></div>

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
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "./Navbar";

export default {
  name: "Blog",
  components: {
    Navbar,
  },
  data() {
    return {
      chief_post: [
        {
          id: 1,
          title: "بهترین زمان کود دهی درختان و باغچه و آموزش آن ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 2,
          title: "بهترین زمان کود دهی درختان و باغچه و آموزش آن ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 3,
          title: "بهترین زمان کود دهی درختان و باغچه و آموزش آن ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 4,
          title: "بهترین زمان کود دهی درختان و باغچه و آموزش آن ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
        {
          id: 5,
          title: "بهترین زمان کود دهی درختان و باغچه و آموزش آن ",
          time: "۱۰ دقیقه",
          date: "۴ ۱۳۹۹ مرداد",
        },
      ],
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
.blog {
  width: 100%;
  padding: 110px 11.5% 50px 11.5%;
  margin: 0px 0px 0px 0px;
  background-color: #fafafa;
}
.cats {
  width: 100%;
  padding: 50px 11.5% 50px 11.5%;
  margin: 0px 0px 0px 0px;
  background-color: #fafafa;
  height: 1474px;
}
.chief {
  width: 100%;
  height: 471px;
  padding: 50px 11.5% 50px 11.5%;
  margin: 0px 0px 0px 0px;
  background-color: #f8f5fc;
}
img.big-top {
  padding: 0px;
  margin: 5px;
  border-radius: 10px;
  width: 100%;
  height: 450px;
  display: block;
}

img.mid-top {
  padding: 0px;
  margin: 5px;
  border-radius: 10px;
  width: 100%;
  height: 220px;
  display: block;
}

.top-right {
  width: 60%;
  float: right;
}
.top-left {
  width: 40%;
  float: left;
}

.title-big-post {
  position: absolute;
  bottom: 44px;
  right: 20px;
  font-size: 28px;
  color: white !important;
}
.desc-big-post {
  position: absolute;
  font-size: 16px;
  bottom: 10px;
  color: white !important;
}
.right-big-post {
  position: absolute;
  bottom: 0px;
  right: 2rem;
  width: max-content;
  float: right;
}
.left-big-post {
  position: absolute;
  bottom: 0px;
  left: -36rem;
  float: left;
}
.title-mid-post {
  position: absolute;
  bottom: 44px;
  right: 20px;
  font-size: 28px;
  color: white !important;
}
.desc-mid-post {
  position: absolute;
  font-size: 16px;
  bottom: 10px;
  color: white !important;
}
.right-mid-post {
  position: absolute;
  bottom: 0px;
  right: 2rem;
  width: max-content;
  float: right;
}
.left-mid-post {
  position: absolute;
  bottom: 0px;
  left: -24rem;
  float: left;
}
div.post-container {
  position: relative;
  margin: 5px;
}

/* top chief editor posts */
img.chief-img {
  padding: 0px;
  margin: 5px;
  border-radius: 10px;
  width: 100%;
  height: 300px;
  display: block;
}

div.chief div.post-container {
  width: 19%;
  float: left;
}
div.chief .title-mid-post {
  position: absolute;
  bottom: 44px;
  right: 20px;
  font-size: 18px;
  color: white !important;
}
div.chief .desc-mid-post {
  position: absolute;
  font-size: 14px;
  bottom: 10px;
  color: white !important;
}
div.chief .right-mid-post {
  position: absolute;
  bottom: 0px;
  right: 2rem;
  width: max-content;
  float: right;
}
div.chief .left-mid-post {
  position: absolute;
  bottom: 0px;
  left: -12rem;
  float: left;
}

/* cats posts */
div.cat-post-container {
  position: relative;
  width: 24%;
  float: left;
  margin: 5px;
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

h3 {
  font-size: 28px;
  color: #5c438a;
  text-align: right;
  margin-bottom: 30px;
}
div.decoration {
  padding-top: 18.5rem;
}
div.mind-health {
  padding-top: 18.5rem;
}

div.skincare {
  padding-top: 18.5rem;
}
.header {
  float: right;
}
.show-all {
  float: left;
}
.show-all a {
  font-size: 14px;
  color: #000000;
  opacity: 0.8;
  text-decoration: none !important;
}
.show-all a:hover {
  text-decoration: underline !important;
  color: #5c438a !important;
  opacity: 1;
}
@media screen and (max-width: 500px) {
  div.top-right {
    width: 100%;
    float: right;
  }
  div.top-left {
    width: 100%;
    float: left;
  }
  img.big-top {
    height: 200px;
  }
  img.mid-top {
    height: 200px;
  }
  div.chief div.post-container {
    width: 100%;
    float: left;
  }
  div.cat-post-container {
    width: 100%;
    float: left;
  }
  div.chief .left-mid-post {
    left: -16rem;
  }
}
</style>