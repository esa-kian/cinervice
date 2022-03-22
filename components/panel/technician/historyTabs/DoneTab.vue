<template>
  <div>
    <div v-if="!loading">
      <div class="project" v-for="project in projects" :key="project.id">
        <a :href="'/project/done/' + project.id">
          <div class="row-one">
            <div class="title-offer">
              <div class="title">{{ project.proficiency }}</div>
            </div>
            <div class="price">{{ parseInt(project.budget) }} تومان</div>
          </div>
          <div class="row-two">
            <div class="date">
              {{
                momentJ(project.start_at)
                  .locale("fa")
                  .format("dddd D jMMMM YYYY ساعت HH:mm")
              }}
            </div>
            <div class="location">
              {{ project.city + ", " + project.town }}
            </div>
          </div>
        </a>
      </div>
    </div>

    <div v-else>
      <img
        class="loading"
        src="../../../../assets/loading_t.svg"
        alt="loading"
      />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "DoneTab",
  mounted() {
    this.fetchProjects();
  },
  methods: {
    fetchProjects() {
      Axios.get(this.$hostname + "/done-projects", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.projects = resp.data.projects;
          this.loading = false;
        })
        .catch((err) => {
          console.log(err, "can not fetch done projects");
        });
    },
  },
  data() {
    return {
      projects: [],
      momentJ: momentJ,
      loading: true,
    };
  },
};
</script>

<style scoped>
img.loading {
  width: 70px;
  height: 70px;
  margin: 50px auto;
}
a {
  text-decoration: none;
  color: #2c3e50;
}
.row-two a {
  text-decoration: none;
  color: #000;
}
.row-two a:hover {
  text-decoration: underline;
  color: #7ab383;
}
.project {
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(122, 179, 131, 0.15);
  margin-bottom: 10px;
  border: 2px solid transparent;
  height: 120px;
  transition: 0.4s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: 18px;
  cursor: pointer;
}
.project:hover {
  border: 2px solid #7ab383;
  transition: 0.4s ease;
}
.project .row-one,
.project .row-two {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.project .row-one .title-offer {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}
.project .row-one .title-offer .title {
  color: #7ab383;
  font-size: 22px;
}
.project .row-two {
  margin-top: 20px;
  font-size: 1rem;
}
.project .row-two .date {
  background-image: url("../../../../assets/panel/green/event.svg");
  background-repeat: no-repeat;
  background-size: 20px;
  background-position: right;
  padding-right: 33px;
}
.project .row-two .location {
  background-image: url("../../../../assets/panel/green/location.svg");
  background-repeat: no-repeat;
  background-size: 16px;
  background-position: right;
  padding-right: 33px;
}
@media screen and (max-width: 540px) {
  .project {
    padding: 10px;
    min-height: 120px;
    font-size: 0.9rem;
  }

  .project .row-two {
    flex-direction: column;
  }
  .project .row-one .title-offer .title {
    font-size: 1rem;
  }
}
</style>
