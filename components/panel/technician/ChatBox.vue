<template>
  <div>
    <div class="messages" id="messages">
      <div class="message" v-for="chat in chats" :key="chat.id">
        <div
          v-if="
            chat.client_id || chat.sender.client_id || chat.sender.id === 11
          "
          class="user"
        >
          <div class="content">{{ chat.content }}</div>
          <div class="time">
            {{
              momentJ(chat.created_at)
                .locale("fa")
                .format(" YYYY/jMM/jDD HH:mm")
            }}
          </div>
        </div>
        <div v-else class="self">
          <div class="content">{{ chat.content }}</div>
          <div class="time">
            {{
              momentJ(chat.created_at)
                .locale("fa")
                .format(" YYYY/jMM/jDD HH:mm")
            }}
          </div>
        </div>
      </div>
    </div>
    <div class="send-box">
      <input
        type="text"
        v-model="content_message"
        @keyup.enter="send"
        placeholder="یک پیام بنویسید…"
      />
      <button v-if="!loading" @submit="send" @click.prevent="send"></button>
      <img
        v-else
        class="loading"
        src="../../../assets/loading_t.svg"
        alt="loading"
      />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "ChatBox",
  data() {
    return {
      content_message: "",
      momentJ: momentJ,
      loading: false,
      message: [],
    };
  },
  props: {
    chats: null,
    conversation_id: null,
  },
  updated() {
    this.scrollToEnd();
  },
  methods: {
    scrollToEnd() {
      let messages = document.getElementById("messages");
      messages.scrollTop = messages.scrollHeight;
    },
    send() {
      this.loading = true;
      let data = {
        content: this.content_message,
        receiver_id: this.chats[0].receiver_id,
        sender_id: this.chats[0].sender_id,
      };
      Axios.post(this.$hostname + "/send-message", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          Axios.get(
            this.$hostname +
              "/conversation?conversation_id=" +
              resp.data.sent.conversation_id,
            {
              headers: {
                Authorization: "Bearer " + eval(localStorage.token),
              },
            }
          )
            .then((resp) => {
              this.chats = resp.data.messages;
            })
            .catch((err) => {
              console.log(err);
            });
          this.content_message = "";
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    Pusher.logToConsole = false;
    let pusher = new Pusher("b40520ebddd87ccd24c7", {
      cluster: "ap1",
    });
    const vm = this;
    let channel = pusher.subscribe("chat-" + this.conversation_id);
    channel.bind("chat", function (data) {
      vm.message = data.message;

      if (data.user.client_id) {
        vm.message.client_id = data.user.client_id;
      } else {
        vm.message.client_id = true;
      }
      vm.chats.push(vm.message);
    });
  },
};
</script>

<style scoped>
img.loading {
  width: 40px;
  height: 40px;
  margin: auto;
}
.messages {
  display: flex;
  flex-direction: column;
  height: 325px;
  overflow-y: scroll;
}
.message {
  display: flex;
  flex-direction: column;
}
.messages .user {
  display: flex;
  flex-direction: column;
  align-self: flex-end;
  border-radius: 10px;
  padding: 10px 10px 5px 7px;
  background-color: rgba(0, 0, 0, 0.05);
  margin-bottom: 10px;
  max-width: 70%;
}
.messages .self {
  display: flex;
  flex-direction: column;
  align-self: flex-start;
  border-radius: 10px;
  background-color: #7ab383;
  color: #fff;
  padding: 6px 10px 9px;
  margin-bottom: 10px;
  max-width: 70%;
}
.time {
  display: flex;
  align-self: flex-end;
  font-size: 14px;
}
.send-box {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
}
.send-box input {
  width: 88%;
  padding: 13px 20px 13px 20px;
  border: none;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(122, 179, 131, 0.15);
  font-family: IRANsans;
  outline: none;
}
.send-box button {
  background-color: #7ab383;
  border: none;
  width: 10%;
  height: 50px;
  background-image: url("../../../assets/panel/send.svg");
  background-repeat: no-repeat;
  background-position: center;
  border-radius: 10px;
  cursor: pointer;
  transition: 0.4s ease;
}
.send-box button:hover {
  opacity: 0.9;
  transition: 0.4s ease;
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
    padding: 0 3% 0 0;
  }
  .send-box input {
    width: 82%;
    padding: 0 2%;
  }
  .send-box button {
    width: 15%;
  }
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .messages {
    padding: 0 3% 0 0;
  }
  .send-box input {
    width: 82%;
    padding: 0 2%;
  }
  .send-box button {
    width: 15%;
  }
  .self {
    max-width: 80%;
  }
  .technician {
    max-width: 80%;
  }
}
</style>