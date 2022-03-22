<template>
  <div class="comments">
    <div class="title">نظرات ({{ comments.length }})</div>
    <div class="comment" v-for="comment in comments" :key="comment.id">
      <div class="body">
        <div
          class="avatar"
          :style="{
            'background-image': 'url(' + comment.profile_picture + ')',
          }"
        ></div>
        <div class="detail">
          <div class="name">
            {{ comment.full_name }}
          </div>
          <div class="desc">{{ comment.content }}</div>
        </div>
      </div>
      <div class="footer">
        <div class="time">
          {{
            momentJ(comment.created_at).locale("fa").format("HH:mm - YYYY/MM/D")
          }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import momentJ from "jalali-moment";

export default {
  name: "Comment",
  props: {
    comments: null,
  },
  data() {
    return {
      public_route: this.$public_backend,
      momentJ: momentJ,
    };
  },
};
</script>

<style scoped>
.comments {
  margin-top: 50px;
  border-top: 2px solid #5c438a1a;
  display: flex;
  flex-direction: column;
}
.comments .title {
  margin-top: -15px;
  width: 18%;
  background: #fff;
  margin-bottom: 20px;
  font-size: 20px;
  color: #5c438a;
}
.comments .comment {
  display: flex;
  flex-direction: column;
  margin-bottom: 30px;
}
.comments .comment .body {
  display: flex;
  justify-content: space-between;
}
.comments .comment .body .avatar {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 70px;
  height: 70px;
  border: 1px solid #5c438a17;
  border-radius: 60px;
}
.comments .comment .body .detail {
  display: flex;
  flex-direction: column;
  width: 88%;
}
.comments .comment .body .detail .name {
  opacity: 0.9;
  color: #000;
  font-size: 18px;
}
.votes {
  font-size: 14px;
  opacity: 0.5;
}

.comments .comment .footer {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
  font-size: 14px;
  color: #132135;
  opacity: 0.6;
}
</style>
