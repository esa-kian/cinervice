<template>
  <div class="container">
    <Navbar />
    <div class="requests">
      <div class="head">
        <div class="filter">فیلترها :</div>

        <div class="price">
          <label for="price" class="check-icon">قیمت </label>
          <input type="checkbox" name="price" id="price" />

          <div id="price-dropdwon" class="dropdown-content">
            <label for="asc">صعودی</label>
            <input @click="sort('asc')" type="checkbox" name="asc" id="asc" />
            <label for="des">نزولی</label>
            <input @click="sort('desc')" type="checkbox" name="des" id="des" />
          </div>
        </div>
        <div class="town">
          <label for="town" class="check-icon">محله </label>
          <input type="checkbox" name="town" id="town" />
          <div id="town-dropdwon" class="dropdown-content">
            <div class="town-opt" v-for="town in towns" :key="town.id">
              <label :for="'town' + town.id">
                {{ town.title }}
                <input
                  type="checkbox"
                  @click="setTown(town.id)"
                  :name="town.id"
                  :id="'town' + town.id"
                />
              </label>
            </div>
          </div>
        </div>
      </div>
      <div v-if="!loading" class="req-cards">
        <div class="req-card" v-for="project in projects" :key="project.id">
          <a :href="'/project/' + project.id">
            <div class="header">
              <div class="title">{{ project.proficiency.title }}</div>
              <div class="price">{{ parseInt(project.budget) }} تومان</div>
            </div>
            <div class="details">
              <div class="date">
                <i></i>
                {{
                  momentJ(project.start_at)
                    .locale("fa")
                    .format("dddd D jMMMM YYYY ساعت HH:mm")
                }}
              </div>
              <div class="address">
                <i></i>
                {{
                  project.address.city.title + ", " + project.address.town.title
                }}
              </div>
            </div>
          </a>
        </div>
      </div>

      <div v-else>
        <img
          class="loading"
          src="../../../assets/loading_t.svg"
          alt="loading"
        />
      </div>
    </div>

    <div class="copyright">
      <Copyright />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "./Navbar";
import Copyright from "./Copyright";
import momentJ from "jalali-moment";

export default {
  name: "Tasks",
  components: {
    Navbar,
    Copyright,
  },
  mounted() {
    this.fetchProjects();
    this.fetchTowns();
  },
  methods: {
    sort(order_by) {
      this.loading = true;
      Axios.get(
        this.$hostname +
          "/projects?order_by=" +
          order_by +
          "&towns=" +
          JSON.stringify(this.selected_town),
        {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        }
      )
        .then((resp) => {
          this.projects = resp.data.projects;
          this.loading = false;
        })
        .catch((err) => {
          console.log(err, "can not filter project");
        });
    },
    setTown(town) {
      const index = this.selected_town.indexOf(town);
      if (index > -1) {
        this.selected_town.splice(index, 1);
      } else {
        this.selected_town.push(town);
      }
      this.sort("");
    },
    fetchProjects() {
      Axios.get(this.$hostname + "/projects", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.projects = resp.data.projects;
        })
        .catch((err) => {
          this.$router.push("/register/technician");
        });
    },
    fetchTowns() {
      Axios.get(this.$hostname + "/towns", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.towns = resp.data.towns;
        })
        .catch((err) => {
          console.log(err, "can not fetch towns");
        });
    },
    checkSkill(id) {
      this.skills.forEach((skill) => {
        if (skill.id == id) {
          skill.check = true;
        }
      });
    },
  },
  data() {
    return {
      towns: [],
      selected_town: [],
      momentJ: momentJ,
      projects: [],
      loading: true,
    };
  },
};
</script>

<style scoped>
@import url("bootstrap/dist/css/bootstrap.css");
img.loading {
  width: 70px;
  height: 70px;
  margin: 25vh auto;
}
.copyright {
  padding: 0 11.5%;
}
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  padding: 0;
  background-color: #f7fff9;
  height: auto;
}
a {
  text-decoration: none;
  color: #000;
}
a:hover {
  text-decoration: none;
  color: #000;
}
.requests {
  width: 100%;
  padding: 110px 11.5% 50px 11.5%;
  margin: 0px 0px 0px 0px;
  background-color: #f7fff9;
  height: auto;
}
.head {
  display: flex;
  justify-content: space-between;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(122, 179, 131, 0.15);
  background-color: #ffffff;
  width: 60%;
  height: 45px;
  padding: 0;
}
.head .filter {
  display: flex;
  min-width: 100px;
  width: 10%;
  align-self: center;
  height: 100%;
  padding: 10px 30px 10px 0;
  border-left: solid 2px #f6faf7;
  background-image: url("../../../assets/panel/green/filter.svg");
  background-repeat: no-repeat;
  background-position-y: center;
  background-position-x: right;
  margin-right: 20px;
}

.head .price {
  display: flex;
  align-self: center;
  width: 30%;
  height: 100%;
  border-left: solid 2px #f6faf7;
  padding: 10px;
}
.head .town {
  display: flex;
  align-self: center;
  width: 60%;
  height: 100%;
  border-left: solid 2px #f6faf7;
  padding: 10px;
}

.head label.check-icon {
  background-image: url("../../../assets/panel/green/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-y: center;
  width: 100%;
  cursor: pointer;
  margin: 0;
}
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #fff;
  margin-top: 35px;
  padding: 10px 20px 10px 159px;
  border-radius: 5px;
  border: solid 1px #e6e6e6;
  z-index: 1;
}
input#price {
  appearance: none;
}
input#price:checked ~ .dropdown-content {
  display: flex;
  flex-direction: column;
  padding: 0;
  width: 23%;
}
.dropdown-content label {
  height: 45px;
  width: 100%;
  padding: 10px 20px;
  margin-bottom: 0;
  direction: initial;
  cursor: pointer;
}
.dropdown-content label:hover {
  background-color: #7ab3831f;
  color: #7ab383;
}
.dropdown-content input {
  appearance: none;
}
.town .dropdown-content input {
  background-image: url("../../../assets/panel/green/unchecked.svg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 18px;
  height: 18px;
  outline: none;
  transition: 0.4s ease;
}
.town .dropdown-content input:checked {
  background-image: url("../../../assets/panel/green/checked.svg");
  transition: 0.4s ease;
}
.town .dropdown-content input:checked ~ label {
  color: #7ab383;
}
input#town {
  appearance: none;
  background-image: url("../../../assets/panel/green/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-y: center;
}
input#town:checked ~ .dropdown-content {
  display: flex;
  flex-direction: column;
  padding: 0;
  width: 19%;
}
.town-opt {
  height: 45px;
  cursor: pointer;
}
input#skill {
  appearance: none;
  background-image: url("../../../assets/panel/green/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-y: center;
}
input#skill:checked ~ .dropdown-content {
  display: flex;
  flex-direction: column;
  padding: 0;
  width: 19%;
}

.head .town {
  display: flex;
  align-self: center;
  width: 33%;
  height: 100%;
  border-left: solid 2px #f6faf7;
  padding: 10px;
}
.head .type {
  display: flex;
  align-self: center;
  width: 33%;
  height: 100%;
  padding: 10px;
}
.form-group {
  display: flex;
  padding: 0;
  margin-bottom: 0;
}

.req-cards {
  width: 100%;
  max-width: 1100px;
  flex-wrap: wrap;
  margin-top: 46px;
  display: flex;
  align-content: center;
  flex-direction: row;
  justify-content: flex-start;
}

.req-card {
  display: flex;
  margin: 10px;
  height: 150px;
  width: 31.2%;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  border: 2px solid transparent;
  transition: 0.4s ease;
}

.req-card:hover {
  border: 2px solid #7ab383;
  cursor: pointer;
  transition: 0.4s ease;
}

.req-cards .req-card .header {
  display: flex;
  justify-content: space-between;
  color: #7ab383;
  opacity: 0.9;
}

.req-cards .req-card .header .title {
  font-size: 20px;
  font-weight: bold;
}
.req-cards .req-card .header .price {
  font-size: 18px;
  font-weight: bold;
}

.req-cards .req-card .details {
  font-size: 1.07rem;
  font-weight: 500;
  opacity: 0.8;
}

.req-cards .req-card .details .date {
  display: flex;
  align-items: center;
}
.req-cards .req-card .details .address {
  display: flex;
  align-items: center;
}
.req-cards .req-card .details i {
  display: flex;
  justify-content: flex-start;
  margin-left: 10px;
  background-size: contain;
  background-repeat: no-repeat;
  width: 20px;
  height: 20px;
}
.req-cards .req-card .details .date i {
  background-image: url("../../../assets/panel/green/event.svg");
}
.req-cards .req-card .details .address i {
  background-image: url("../../../assets/panel/green/location.svg");
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .copyright {
    padding: 0 4%;
  }
  .requests {
    padding: 80px 3% 0px 3%;
  }
  .req-cards {
    justify-content: center;
    padding-top: 20px;
  }
  .req-card {
    width: 47%;
  }
  .head {
    width: 100%;
  }
  input#town:checked ~ .dropdown-content {
    width: 30%;
  }
}
@media screen and (max-width: 540px) {
  .copyright {
    padding: 0 4%;
  }
  .requests {
    padding: 80px 4% 0px 4%;
  }
  .req-cards {
    width: 100%;
    margin-top: 40px;
    flex-direction: column;
  }
  .req-card {
    width: 100%;
  }
  .head {
    width: 100%;
  }
  .head .filter {
    display: none;
  }

  .head .price {
    width: 30%;
    font-size: 0.8rem;
    padding: 10px;
    justify-content: flex-start;
  }

  .head .town {
    width: 70%;
    font-size: 0.8rem;
    padding: 10px;
    justify-content: flex-start;
  }
  .town-opt {
    width: 120px;
  }
  input#town:checked ~ .dropdown-content {
    width: 120px;
  }
  .skill-opt {
    width: 100%;
  }
  input#skill:checked ~ .dropdown-content {
    width: 50%;
  }
}
</style>