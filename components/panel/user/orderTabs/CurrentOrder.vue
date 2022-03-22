<template>
  <div class="container">
    <Navbar />
    <div class="current">
      <div class="current-card">
        <div class="header">
          <div class="title">{{ order.proficiency.title }}</div>
          <div class="budget">
            <div class="caption">بودجه شما :</div>
            <div class="budget-val">{{ parseInt(order.budget) }} تومان</div>
          </div>
        </div>
        <div class="body">
          <div class="date">
            <i></i>
            {{ start_at }}
          </div>
          <div class="skills">
            <ul>
              <li v-for="skill in skills" :key="skill.skill_id">
                {{ skill.title }}
              </li>
            </ul>
          </div>
          <div class="detail">
            {{ order.details }}
          </div>
          <div class="address">
            <i></i>
            {{
              order.address.city.title +
              ", " +
              order.address.town.title +
              ", " +
              order.address.description
            }}
          </div>
          <div class="photos">
            <img
              v-for="photo in order.photos"
              :key="photo.id"
              :src="photo.url"
              alt=""
              width="110px"
              height="110px"
            />
          </div>
        </div>
        <Suggest :bids="bids" :project_id="id" />
        <Comment :comments="comments" />
      </div>
    </div>
    <div class="copyright">
      <Copyright />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "../../../Navbar";
import Suggest from "./Suggest";
import Comment from "./Comment";
import Copyright from "../../../Copyright";

export default {
  name: "Current",
  components: {
    Navbar,
    Suggest,
    Copyright,
    Comment,
  },
  mounted() {
    this.fetchOrder();
  },
  methods: {
    fetchOrder() {
      Axios.get(this.$hostname + "/current-orders/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.comments = resp.data.order.comments;
          this.bids = resp.data.order.bids;
          this.order = resp.data.order.detail[0];
          this.start_at = moment(this.order.start_at).format(
            "dddd jD jMMMM jYYYY ساعت HH:mm"
          );
          this.skills = resp.data.order.skills;
        })
        .catch((err) => {
          this.$router.push("/");
        });
    },
  },
  props: {
    id: null,
  },
  data() {
    return {
      order: null,
      skills: [],
      bids: [],
      comments: [],
      start_at: null,
      public_route: this.$public_backend,
    };
  },
};
</script>

<style scoped>
.copyright {
  padding: 0 11.5%;
}
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  background-color: #f8f5fc;
  height: auto;
}
.current {
  height: 100%;
  width: 100%;
  max-width: 1366px;
  display: flex;
  justify-content: center;
  margin: auto;
}

.current .current-card {
  height: auto;
  padding: 20px 20px 30px;
  display: flex;
  flex-direction: column;
  align-content: space-between;
  background-color: #fff;
  width: 58%;
  max-width: 800px;
  border-radius: 5px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  margin-top: 110px;
  margin-bottom: 50px;
}
.header {
  display: flex;
  justify-content: space-between;
}
.header .title {
  font-size: 24px;
  font-weight: bold;
  color: #5c438a;
}
.header .budget {
  border-radius: 5px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  color: #000;
  padding: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: 500;
  width: 250px;
}
.body .date {
  font-size: 18px;
  font-weight: 500;
}
ul {
  display: flex;
}
ul li {
  justify-content: space-between;
  margin-left: 30px;
  display: list-item;
}

::marker {
  color: #5c438a;
  font-size: 24px;
  display: flex;
  justify-content: flex-start;
  margin: 0 !important;
  padding: 0 !important;
}
.detail {
  margin-top: 10px;
  display: list-item;
  margin-right: 30px;
}
.body .address {
  margin-top: 20px;
}
.photos {
  display: flex;
  justify-content: center;
  margin: 5px;
  flex-wrap: wrap;
}
.photos img {
  margin-left: 10px;
  border: 2px dashed #5c438a42;
  padding: 2px;
  outline: none;
}
.body .photos img {
  display: flex;
}
.address {
  display: flex;
  justify-content: flex-start;
  margin: 20px 0;
}
.address i {
  background-image: url("../../../../assets/Tasks/Location.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
.date {
  display: flex;
  justify-content: flex-start;
  margin: 20px 0;
}
.date i {
  background-image: url("../../../../assets/Tasks/Event.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .current {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }

  .current .current-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
    margin-top: 0;
  }
  
  .copyright {
    padding: 0 4%;
  }
}
@media screen and (max-width: 540px) {
  .current {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }

  .current .current-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
    margin-top: 0;
  }
  .header {
    flex-direction: column;
  }
  .copyright {
    padding: 0 4%;
  }
  .body .technician {
    flex-direction: column;
  }
  ul {
    display: block;
  }
  .address i {
    background-repeat: no-repeat;
    background-size: contain;
    width: 30px;
    height: 20px;
  }
  .photos {
    flex-direction: column;
    align-items: center;
  }
  .body .photos img {
    margin-top: 10px;
  }
  .header .budget {
    margin-top: 20px;
  }
}
</style>
