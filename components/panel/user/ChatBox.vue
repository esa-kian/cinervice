<template>
  <div>
    <div class="messages" id="messages">
      <div class="message" v-for="chat in chats" :key="chat.id">
        <div
          v-if="
            chat.technician_id ||
            chat.sender.technician_id ||
            chat.sender.id === 11
          "
          class="technician"
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
        placeholder="یک پیام بنویسید…"
        @keyup.enter="send"
      />
      <button v-if="!loading" @click.prevent="send"></button>
      <img
        v-else
        class="loading"
        src="../../../assets/loading.svg"
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
      momentJ: momentJ,
      content_message: "",
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

      if (data.user.technician_id) {
        vm.message.technician_id = data.user.technician_id;
      } else {
        vm.message.technician_id = true;
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
.technician {
  display: flex;
  flex-direction: column;
  align-self: flex-end;
  border-radius: 10px;
  padding: 10px 10px 5px 7px;
  background-color: rgba(0, 0, 0, 0.05);
  color: rgba(0, 0, 0, 0.8);
  margin-bottom: 10px;
  max-width: 70%;
}
.self {
  display: flex;
  flex-direction: column;
  align-self: flex-start;
  border-radius: 10px;
  background-color: #5c438a1f;
  color: rgba(0, 0, 0, 0.8);
  padding: 6px 10px 9px;
  margin-bottom: 10px;
  max-width: 70%;
}
.self .time {
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
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  font-family: IRANsans;
  outline: none;
}
.send-box button {
  background-color: #5c438a;
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
</style>