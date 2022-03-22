<template>
  <div>
    <div v-if="!loading" class="messages">
      <div class="message-list">
        <div
          :class="[
            'message',
            message.full_name_sender && message.unread === 1
              ? 'message_unread'
              : '',
            isSelect == message.id ? 'select' : '',
          ]"
          v-for="message in messages"
          :key="message.id"
          @click.prevent="selectedMessage(message.id, message.conversation_id)"
        >
          <div class="user">
            <div
              v-if="message.full_name_sender"
              class="avatar"
              :style="{
                'background-image': 'url(' + message.sender_picture + ')',
              }"
            ></div>
            <div
              v-else-if="message.full_name_receiver"
              class="avatar"
              :style="{
                'background-image': 'url(' + message.receiver_picture + ')',
              }"
            ></div>

            <div class="detail">
              <div v-if="message.full_name_sender" class="name">
                {{ message.full_name_sender.substring(0, 7) }}
                {{ message.full_name_sender.length > 7 ? "..." : "" }}
              </div>
              <div v-else-if="message.full_name_receiver" class="name">
                {{ message.full_name_receiver.substring(0, 7) }}
                {{ message.full_name_receiver.length > 7 ? "..." : "" }}
              </div>
              <div v-else class="name">پشتیبان</div>

              <div v-if="message.content != null" class="skill">
                {{ message.content.substring(0, 20) }}
                {{ message.content.length > 20 ? "..." : "" }}
              </div>
            </div>
          </div>
          <div class="date">
            {{
              momentJ(message.created_at)
                .locale("fa")
                .format(" YYYY/jMM/jDD HH:mm")
            }}
          </div>
        </div>
      </div>
      <div v-if="!loading_conversation" class="chat-box">
        <ChatBox :conversation_id="conversation_id" :chats="chats" />
      </div>
      <div v-else>
        <img
          class="conversation"
          src="../../../assets/loading_t.svg"
          alt="loading"
        />
      </div>
    </div>
    <div v-else>
      <img class="loading" src="../../../assets/loading_t.svg" alt="loading" />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import ChatBox from "./ChatBox";
import momentJ from "jalali-moment";

export default {
  name: "Messages",
  components: {
    ChatBox,
  },
  created() {
    this.fetchMessages();
  },
  methods: {
    fetchMessages() {
      Axios.get(this.$hostname + "/messages", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.messages = resp.data.messages;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    selectedMessage(id, conversation_id) {
      this.loading_conversation = true;
      this.conversation_id = conversation_id;
      this.isSelect = id;
      let data = {
        conversation_id: conversation_id,
      };
      Axios.patch(this.$hostname + "/read-message", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading_conversation = false;
          this.fetchMessages();
          this.chats = resp.data.message;
        })
        .catch((err) => {
          console.log(err);
        });
      this.messages.forEach((message) => {
        if (message.id == id) {
          message.unread = 0;
        }
      });
    },
  },
  data() {
    return {
      isSelect: null,
      chats: null,
      messages: [],
      momentJ: momentJ,
      conversation_id: null,
      loading: true,
      loading_conversation: false,
    };
  },
};
</script>

<style scoped>
img.loading {
  width: 70px;
  height: 70px;
  margin: 250px auto;
}
img.conversation {
  width: 70px;
  height: 70px;
  margin: auto;
}
.messages {
  padding: 50px 4.3%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  height: 500px;
}
.messages .message-list {
  width: 40%;
  padding: 10px;
  height: 500px;
  overflow-y: scroll;
  direction: ltr;
}
.message {
  direction: rtl;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  width: 100%;
  height: 80px;
  border-right: 7px solid #7ab38328;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(122, 179, 131, 0.15);
  margin-bottom: 10px;
  padding-top: 10px;
  cursor: pointer;
  transition: 0.3s ease;
}
.message_unread {
  border-right: 7px solid #7ab383;
  transition: 0.3s ease;
}
.select {
  background-color: #7ab38317;
  transition: 0.3s ease;
}
.messages .message-list .message .user {
  display: flex;
}
.messages .message-list .message .user .detail {
  margin-right: 10px;
}
.messages .message-list .message .user .name {
  font-size: 16px;
}
.messages .message-list .message .user .skill {
  font-size: 14px;
}
.messages .message-list .message .date {
  font-size: 14px;
  margin-left: 12px;
}
.messages .message-list .message .avatar {
  /* background-image: url("../../../assets/avatar.jpg"); */
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 50px;
  height: 50px;
  border-radius: 25px;
  margin-right: 15px;
}

.messages .chat-box {
  height: 400px;
  border-radius: 10px;
  margin-top: 10px;
  padding: 10px;
  box-shadow: 0 0 10px 1px rgba(122, 179, 131, 0.15);
  width: 58%;
}
/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 2px #7ab3831e;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #7ab3839f;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #7ab383;
}
@media screen and (max-width: 540px) {
  .messages {
    padding: 20px 4% 20px 1%;
    max-height: 1200px;
    height: 1000px;
    position: relative;
    overflow-y: scroll;
    flex-direction: column-reverse;
  }
  .messages .chat-box {
    width: 100%;
    padding: 10px 0;
    max-height: 400px;
    overflow-y: scroll;
  }
  .messages .message-list {
    width: 100%;
    padding: 10px 4px;
  }
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .messages {
    padding: 20px 4% 20px 1%;
    max-height: 450px;
    height: 450px;
    position: relative;
    overflow-y: scroll;
  }
  .messages .chat-box {
    width: 50%;
    padding: 10px 0;
    max-height: 400px;
    overflow-y: scroll;
  }
  .messages .message-list {
    width: 48%;
    padding: 10px 4px;
  }
}
</style>
