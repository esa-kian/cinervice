<template>
  <div class="posts">
    <div class="post">
      <div class="photo"></div>
      <div class="detail">
        <div class="title">ثبت پیشنهاد</div>
        <div class="desc">
          نوع درخواست و قیمت پیشنهادی خود را انتخاب نموده و سفارش خود را ثبت
          نمایید…
        </div>
        <div class="date-time">
          <div class="time">۱۰ دقیقه</div>
          <div class="date">۴ ۱۳۹۹ مرداد</div>
        </div>
      </div>
    </div>
    <div class="post">
      <div class="photo"></div>
      <div class="detail">
        <div class="title">ثبت پیشنهاد</div>
        <div class="desc">
          نوع درخواست و قیمت پیشنهادی خود را انتخاب نموده و سفارش خود را ثبت
          نمایید…
        </div>
        <div class="date-time">
          <div class="time">۱۰ دقیقه</div>
          <div class="date">۴ ۱۳۹۹ مرداد</div>
        </div>
      </div>
    </div>
    <div class="post">
      <div class="photo"></div>
      <div class="detail">
        <div class="title">ثبت پیشنهاد</div>
        <div class="desc">
          نوع درخواست و قیمت پیشنهادی خود را انتخاب نموده و سفارش خود را ثبت
          نمایید…
        </div>
        <div class="date-time">
          <div class="time">۱۰ دقیقه</div>
          <div class="date">۴ ۱۳۹۹ مرداد</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LastPostBlog",
  components: {},
  data() {
    return {};
  },

  methods: {},
};
</script>
<style scoped>
.posts {
  display: flex;
  justify-content: space-between;
  flex-wrap: nowrap;
}
.post {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-wrap: nowrap;
  height: 385px;
  max-height: 385px;
  width: 32%;
  padding: 0;
  border-radius: 15px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
}
.photo {
  display: flex;
  background-image: url("../../assets/cat.png");
  background-position: left;
  background-repeat: no-repeat;
  background-size: cover;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  width: 100%;
  height: 256px;
  max-height: 256px;
}
.detail {
  display: flex;
  flex-direction: column;
  padding: 10px;
}
.title {
  font-weight: bold;
}
.desc {
  font-size: 0.9rem;
}
.date-time {
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
  font-weight: 300;
  color: rgba(0, 0, 0, 0.5);
}
@media screen and (max-width: 540px) {
  .posts {
    flex-direction: column;
  }
  .post {
    margin-top: 20px;
    width: 100%;
  }
}
</style>