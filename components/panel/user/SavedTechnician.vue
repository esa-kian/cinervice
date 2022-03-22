<template>
  <div>
    <div v-if="!loading" class="technicians">
      <div
        class="technician"
        v-for="technician in technicians"
        :key="technician.id"
      >
        <div @click="unsave(technician.id)" class="unsave"></div>
        <a :href="'/technician_profile/' + technician.id" target="_blank">
          <div class="detail">
            <div
              class="avatar"
              :style="{
                'background-image': 'url(' + technician.profile_picture + ')',
              }"
            ></div>
            <div class="name">
              {{ technician.full_name }}
            </div>
            <div class="rate">{{ technician.rate.substring(0, 3) }}</div>
            <div class="skill">{{ technician.proficiency }}</div>
          </div>
        </a>
      </div>
    </div>
    <div v-else>
      <img class="loading" src="../../../assets/loading.svg" alt="loading" />
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "SavedTechnician",
  mounted() {
    this.fetchTechnicians();
  },
  methods: {
    fetchTechnicians() {
      Axios.get(this.$hostname + "/saved-technicians", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.technicians = resp.data.technicians;
        })
        .catch((err) => {
          console.log(err, "can not fetch transactions");
        });
    },
    unsave(id) {
      Axios.delete(this.$hostname + "/saved-technicians/" + id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.fetchTechnicians();
        })
        .catch((err) => {
          console.log(err, "درخواست نامعتبر");
        });
    },
  },
  data() {
    return {
      technicians: [],
      loading: true,
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

a,
a:hover {
  text-decoration: none;
  color: #000;
}
.technicians {
  display: flex;
  flex-wrap: wrap;
  padding: 50px 7% 50px 3%;
  width: 100%;
  height: 550px;
  overflow-y: scroll;
}
.technicians .technician {
  margin: 0 0 10px 10px;
  height: 220px;
  width: 23%;
  border-radius: 10px;
  border: 2px solid transparent;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.4s ease;
}
.technicians .technician:hover {
  border: 2px solid #5c438a;
  transition: 0.4s ease;
}
.avatar {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 90px;
  height: 90px;
  border: 1px solid #5c438a17;
  border-radius: 45px;
  margin-bottom: 10px;
}
.technicians .technician .detail {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: -20px;
}
.name {
  opacity: 0.9;
}
.rate {
  background-image: url("../../../assets/panel/stars/fill.svg");
  background-repeat: no-repeat;
  background-position-x: right;
  background-position-y: center;
  padding-right: 20px;
  font-size: 14px;
}
.skill {
  font-size: 18px;
  color: #5c438a;
}
.unsave {
  background-image: url("../../../assets/panel/saved.svg");
  background-repeat: no-repeat;
  background-size: contain;
  margin: 10px;
  width: 15px;
  height: 20px;
  position: relative;
  cursor: pointer;
  transition: 0.4s ease;
}
.unsave:hover {
  background-image: url("../../../assets/panel/save.svg");
  transition: 0.4s ease;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .technicians {
    padding: 20px 3%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }
  .technicians .technician {
    margin: 0 0 15px 3%;
    height: 220px;
    width: 30%;
  }
  .skill {
    font-size: 0.9rem;
    color: #5c438a;
  }
  .unsave {
    width: 20px;
    height: 25px;
  }
}
@media screen and (max-width: 540px) {
  .technicians {
    padding: 20px 3%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }
  .technicians .technician {
    margin: 0 0 15px 4%;
    height: 220px;
    width: 45%;
  }
  .skill {
    font-size: 0.9rem;
    color: #5c438a;
  }
  .unsave {
    width: 20px;
    height: 25px;
  }
}
</style>