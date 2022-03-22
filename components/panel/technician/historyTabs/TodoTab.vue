<template>
  <div>
    <div v-if="!loading">
      <div
        @mouseenter="location = project.id"
        @mouseleave="location = null"
        class="project"
        v-for="project in projects"
        :key="project.id"
      >
        <a
          :href="[
            project.technician_id != null
              ? '/project/todo/' + project.id
              : '/project/' + project.id,
          ]"
        >
          <div class="row-one">
            <div class="title-offer">
              <div class="title">{{ project.proficiency }}</div>
              <div class="offer" v-if="project.technician_id == null">
                ( در انتظار تایید)
              </div>
              <div class="offer" v-else>(تایید شده)</div>
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

            <div
              @click.prevent="cancelProjectModal(project.id)"
              v-if="location === project.id"
              class="cancel"
            >
              لغو درخواست
            </div>

            <div v-else class="location">
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
    <!-- Modal Cancel Project -->
    <div id="current" class="modal">
      <div class="modal-content">
        <div class="header">
          <div class="title">لغو درخواست</div>
          <span class="closecurrent"></span>
        </div>
        <div class="content">
          <div class="logout-icon"></div>
          <p>آیا از لغو درخواست خود اطمینان دارید؟</p>
          <div class="yes-no">
            <button class="acceptcurrent">خیر</button>
            <button @click="cancel(wanna_cancel)" class="acceptcurrent">
              بله
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import momentJ from "jalali-moment";

export default {
  name: "TodoTab",
  mounted() {
    this.fetchProjects();
  },
  methods: {
    fetchProjects() {
      Axios.get(this.$hostname + "/todo-projects", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.projects = resp.data.projects;
          this.loading = false;
        })
        .catch((err) => {
          console.log(err, "can not fetch todo projects");
        });
    },
    cancelProjectModal(project_id) {
      this.wanna_cancel = project_id;

      let modal = document.getElementById("current");

      // Get the <span> element that closes the modal
      let span = document.getElementsByClassName("closecurrent")[0];
      let accept = document.getElementsByClassName("acceptcurrent")[0];

      // When the user clicks the button, open the modal

      modal.style.display = "block";

      // When the user clicks on <span> (x), close the modal
      span.onclick = function () {
        modal.style.display = "none";
      };
      accept.onclick = function () {
        modal.style.display = "none";
      };

      // When the user clicks anywhere outside of the modal, close it
      window.onclick = function (event) {
        if (event.target == modal) {
          modal.style.display = "none";
        }
      };
    },
    cancel(project_id) {
      let data = {
        project_id: project_id,
      };
      Axios.patch(this.$hostname + "/cancel-project", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.fetchProjects();

          let modal = document.getElementById("current");

          modal.style.display = "none";
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  data() {
    return {
      projects: [],
      momentJ: momentJ,
      location: null,
      wanna_cancel: null,
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
.project .row-one .title-offer .offer {
  color: #b6485a;
  font-size: 16px;
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

.cancel:hover {
  text-decoration: underline;
  color: #7ab383;
  transition: 0.4s ease;
}
/* Modal Cancel Order style */
/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: #7ab38349; /* Fallback color */
  backdrop-filter: blur(2px) saturate(110%);
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  border: 1px solid #888;
  width: 33%; /* Full width */
  height: 330px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  justify-content: center;
  flex-direction: column;
  box-shadow: 0 0 10px 1px #7ab383;
}
.modal-content .content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 245px;
}
.modal-content .content p {
  font-size: 16px;
  margin-top: 0;
}
/* The Close Button */
.header {
  display: flex;
  color: #000;
  font-size: 22px;
  font-weight: 500;
  justify-content: space-between;
  align-items: center;
  border-bottom: solid 2px #7ab38318;
  padding-bottom: 15px;
}
.header .title {
  display: flex;
  justify-self: center;
  align-self: flex-end;
  margin: 0 auto;
}
.closecurrent {
  display: flex;
  justify-self: flex-end;
  background-image: url("../../../../assets/panel/green/Close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  margin-left: 3%;
}
.closecurrent:hover {
  cursor: pointer;
}
.logout-icon {
  background-image: url("../../../../assets/panel/green/warning.svg");
  display: flex;
  /* margin: 30px; */
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 100px;
  height: 100px;
}
.yes-no {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  align-items: center;
  width: 60%;
}
.yes-no button {
  margin-top: 50px;
  align-self: center;
  cursor: pointer;
  outline: none;
  padding: 0;
  border-radius: 5px;
  font-size: 18px;
  font-weight: 500;
  background-color: #fff;
  border: 2px solid #7ab383;
  font-family: "IRANSans";
  color: #7ab383;
  transition: 0.4s ease;
  height: 50px;
  width: 45%;
}
.yes-no button:hover {
  background-color: #7ab383;
  color: #fff;
  transition: 0.4s ease;
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
  .modal {
    z-index: 999;
  }
  .modal-content {
    width: 90%;
  }
}
</style>
