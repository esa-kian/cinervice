<template>
  <div class="container">
    <Navbar />
    <div class="done">
      <div class="done-card">
        <div class="header">
          <div class="title">{{ project.proficiency }}</div>
          <div class="budget">
            <div class="caption">مبلغ کل:</div>
            <div class="budget-val">{{ parseInt(project.budget) }} تومان</div>
          </div>
        </div>
        <div class="body">
          <div class="technician">
            <div class="info">
              <div
                class="photo"
                :style="{
                  'background-image': 'url(' + project.client_picture + ')',
                }"
              ></div>
              <div class="details">
                <div class="name">
                  <a
                    :href="
                      '/panel/technician/user_profile/' + project.client_id
                    "
                  >
                    {{ project.client_name }}</a
                  >
                </div>
              </div>
            </div>
            <div class="vote">
              <div class="title">امتیاز شما به این درخواست‌دهنده:</div>
              <div class="star">
                <div v-for="index in rate" :key="index" class="fill"></div>
                <i v-for="index in 5 - rate" :key="index" class="empty"></i>
              </div>
            </div>
          </div>
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
            {{ project.details }}
          </div>
          <div class="address">
            <i></i>
            {{ project.address }}
          </div>
          <l-map
            v-if="showMap"
            :zoom="zoom"
            :center="center"
            :options="mapOptions"
            style="height: 240px; width: 100%;border-radius: 10px;"
            @update:center="centerUpdate"
            @update:zoom="zoomUpdate"
          >
            <l-tile-layer :url="url" :attribution="attribution" />
            <l-marker :lat-lng="withPopup" :icon="icon">
              <l-popup>
                <div class="info">
                  <div
                    class="photo"
                    :style="{
                      'background-image': 'url(' + project.client_picture + ')',
                    }"
                  ></div>
                  {{ project.client_name }}
                </div>
              </l-popup>
            </l-marker>
          </l-map>
          <div class="photos">
            <img
              v-for="photo in project.photos"
              :key="photo.id"
              :src="photo.url"
              alt=""
              width="110px"
              height="110px"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="copyright">
      <Copyright />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import Navbar from "../Navbar";
import Copyright from "../Copyright";
import { latLng, icon } from "leaflet";
import {
  LMap,
  LTileLayer,
  LMarker,
  LPopup,
  LTooltip,
  LIcon,
} from "vue2-leaflet";

export default {
  name: "Done",
  components: {
    Navbar,
    Copyright,
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip,
    LIcon,
  },
  mounted() {
    this.fetchProject();
  },
  methods: {
    fetchProject() {
      Axios.get(this.$hostname + "/done-projects/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.project = resp.data.project.detail[0];
          this.lat = parseFloat(resp.data.project.detail[0].lat);
          this.long = parseFloat(resp.data.project.detail[0].long);
          this.center = latLng(this.lat, this.long);
          this.withPopup = latLng(this.lat, this.long);
          this.currentCenter = latLng(this.lat, this.long);
          this.rate = resp.data.project.rate;
          this.skills = resp.data.project.skills;
          this.start_at = moment(this.project.start_at).format(
            "dddd jD jMMMM jYYYY ساعت HH:mm"
          );
        })
        .catch((err) => {
          this.$router.push("/");
        });
    },
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    },
    
  },
  props: {
    id: null,
  },
  data() {
    return {
      lat: 0,
      long: 0,
      rate: null,
      project: null,
      start_at: null,
      skills: [],
      zoom: 13,
      center: latLng(0, 0),
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution: "طراحی شده توسط ویستا",
      withPopup: latLng(0, 0),
      currentZoom: 11.5,
      currentCenter: latLng(0, 0),
      showParagraph: false,
      mapOptions: {
        zoomSnap: 0.5,
      },
      showMap: true,
      icon: icon({
        iconUrl: require("../../../../assets/logo.png"),
        iconSize: [36, 36],
        iconAnchor: [16, 37],
      }),
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
  background-color: #f7fff9;
  height: auto;
}
.done {
  min-height: 1000px;
  height: 100%;
  width: 100%;
  max-width: 1366px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
  padding-top: 50px;
}

.done .done-card {
  min-height: 650px;
  height: auto;
  padding: 20px 20px 30px;
  display: flex;
  flex-direction: column;
  position: absolute;
  align-content: space-between;
  background-color: #fff;
  width: 58%;
  max-width: 800px;
  border-radius: 5px;
  box-shadow: 0 0 10px 1px rgba(122, 179, 131, 0.15);
  margin: 130px;
}
.header {
  display: flex;
  justify-content: space-between;
}
.header .title {
  font-size: 24px;
  font-weight: bold;
  color: #7ab383;
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
.body .technician {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  margin: 30px 0;
}
.body .technician .info {
  display: flex;
  align-items: center;
}
.info .photo {
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 120px;
  height: 120px;
  border-radius: 50%;
}
.body .technician .info .details {
  margin-right: 20px;
  font-size: 20px;
  line-height: 40px;
  font-weight: bold;
}
a {
  color: #000;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
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
  color: #7ab383;
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
  border: 2px dashed #7ab38342;
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
  background-image: url("../../../../assets/panel/green/location.svg");
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
  background-image: url("../../../../assets/panel/green/event.svg");
  margin-left: 10px;
  background-repeat: round;
  width: 20px;
  height: 20px;
}

.star {
  display: flex;
  flex-direction: row-reverse;
  margin-top: 10px;
}
.star .fill {
  background-image: url("../../../../assets/panel/stars/fill.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 25px;
  height: 25px;
}
.star .empty {
  background-image: url("../../../../assets/panel/stars/empty.png");
  background-repeat: no-repeat;
  background-size: contain;
  width: 25px;
  height: 25px;
}
@media screen and (max-width: 540px) {
  .copyright {
    padding: 0 4%;
  }
  .done {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }

  .done .done-card {
    width: 90%;
    height: 85%;
    min-height: fit-content;
    position: relative;
    padding: 10px;
  }
  .header {
    flex-direction: column;
  }
  .header .client .info .details .register-date {
    font-size: 0.9rem;
  }
  .body .title {
    margin-top: 20px;
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
  .actions {
    width: 90%;
  }
  .actions button {
    margin-top: 20px;
    height: 40px;
    font-size: 0.9rem;
    width: 47%;
  }
  .copyright {
    padding: 0 4%;
  }
  .body .photos img {
    margin-top: 10px;
  }
  .body .technician {
    flex-direction: column;
  }
  .header .budget {
    margin-top: 20px;
  }
}
</style>
