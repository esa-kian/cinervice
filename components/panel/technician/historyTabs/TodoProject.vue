<template>
  <div class="container">
    <Navbar />
    <div class="project">
      <div class="project-card">
        <div class="header">
          <div class="client">
            <div class="info">
              <div
                class="photo"
                :style="{
                  'background-image': project.client_picture
                    ? 'url(' + project.client_picture + ')'
                    : 'none',
                }"
              ></div>
              <div class="details">
                <div class="name">
                  <a href="/panel/technician/user_profile">
                    {{ project.client_name || "" }}
                  </a>
                </div>
                <div class="register-date">
                  عضو لِمِ کار از {{ created_at }}
                </div>
              </div>
            </div>
          </div>
          <div class="budget">
            <div class="caption">بودجه :</div>
            <div class="budget-val">{{ parseInt(project.budget) }} تومان</div>
          </div>
        </div>
        <div class="body">
          <div class="title">{{ project.proficiency }}</div>

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
          <div id="mapirt"></div>

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
          <div class="actions">
            <button>آغاز چت</button>
            <button @click="doneProjectModal">اتمام انجام سرویس</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal done project -->
    <transition name="fade">
      <div id="myModal" class="modal" v-if="show">
        <div class="modal-content">
          <div class="header">
            <div class="title">اتمام انجام سرویس</div>
            <span class="close" @click="show = false"></span>
          </div>
          <div class="content">
            <div class="logout-icon"></div>
            <p>آیا انجام سرویس با موفقیت به پایان رسید؟</p>
            <div class="yes-no">
              <button class="accept" @click="show = false">خیر</button>
              <button @click.prevent="uploadPicModal" class="next">بله</button>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <!-- Modal done upload pic -->
    <transition name="fade">
      <div id="uploadpic" class="modal" v-if="show_upload">
        <div class="modal-content">
          <div class="header">
            <div class="title">ثبت عکس</div>
            <span
              class="close-upload"
              @click.prevent="show_upload = false"
            ></span>
          </div>
          <div class="content">
            <p>
              در صورت تمایل، تصاویر مرتبط با درخواست انجام شده را برای افزودن به
              رزومه آپلود کنید.
            </p>
            <div v-if="!loading_photos" class="upload">
              <div class="btn-upload">
                <label for="photo"></label>
                <input
                  type="file"
                  id="photo"
                  hidden
                  ref="file"
                  @change="onFileChange"
                />
                <span>بارگذاری تصویر</span>
              </div>
              <div class="images" v-if="images">
                <div class="img" v-for="(image, index) in images" :key="index">
                  <div
                    @click="removeImage(index, image.id)"
                    class="image-done"
                  ></div>
                  <img :src="image.url" width="100" height="auto" />
                </div>
              </div>
            </div>
            <div v-else>
              <img
                class="loading"
                src="../../../../assets/loading_t.svg"
                alt="loading"
              />
            </div>
            <div class="yes-no">
              <button
                v-if="!loading_submit"
                @click.prevent="doneModal"
                class="done"
              >
                ثبت تصاویر
              </button>
              <div v-else>
                <img
                  class="loading-submit"
                  src="../../../../assets/loading_t.svg"
                  alt="loading"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </transition>
    <!-- done upload modal  -->
    <transition name="fade">
      <div id="doneModal" class="modal" v-if="show_done">
        <div class="modal-content">
          <div class="content">
            <div class="logout-icon"></div>
            <p>تصاویر شما با موفقیت ثبت شد.</p>
          </div>
        </div>
      </div>
    </transition>
    <!-- Modal rate -->
    <transition name="fade">
      <div id="rate-modal" class="modal" v-if="show_rate">
        <div class="modal-content">
          <div class="header">
            <div class="title">افزودن نظر</div>
            <span class="close" @click.prevent="show_rate = false"></span>
          </div>
          <div class="content">
            <div class="rate">
              <p>به میزان رضایت خود از این درخواست دهنده امتیاز دهید.</p>
              <StarRating />
            </div>
            <div class="comment">
              <p>نظرات خود را درباره این درخواست دهنده ثبت نمایید.</p>
              <textarea
                v-model="comment"
                name="comment"
                id="comment"
              ></textarea>
            </div>
          </div>
          <div class="actions">
            <button
              v-if="!loading_submit"
              @click.prevent="rateModal"
              class="done"
            >
              ثبت نظر
            </button>
            <div v-else>
              <img
                class="loading-submit"
                src="../../../../assets/loading_t.svg"
                alt="loading"
              />
            </div>
          </div>
        </div>
      </div>
    </transition>
    <div class="copyright">
      <Copyright />
    </div>
  </div>
</template>

<script>
import Navbar from "../Navbar";
import StarRating from "./StarRating";
import Copyright from "../Copyright";
import Axios from "axios";
import { latLng, latLngBounds, icon } from "leaflet";
import { LMap, LTileLayer, LIcon, LMarker } from "vue2-leaflet";
import L from "leaflet";
import "leaflet-wms-header";

import Vue from "vue";
var lat, long;

const setDescription = (x, y) => {
  Vue.prototype.latlong.lat = x;
  Vue.prototype.latlong.long = y;
  lat = x;
  long = y;
};

export default {
  name: "Todo",
  components: {
    Navbar,
    StarRating,
    Copyright,
    LMap,
    LTileLayer,
    LIcon,
    LMarker,
  },
  async mounted() {
    await this.fetchProject();
    var app = new Mapp({
      element: "#mapirt",
      presets: {
        latlng: {
          lat: lat,
          lng: long,
        },
        zoom: 13,
      },
      i18n: {
        fa: {
          "marker-title": "عنوان",
          "marker-description": "توضیح",
        },
        en: {
          "marker-title": "Title",
          "marker-description": "Description",
        },
      },
      locale: "fa",
      apiKey:
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU3YmI4NzAxYmYzN2YxNzE1OWIwMjVkZjExNzVmZTllNDc2ODhkMjMxNDZhZTk2ZWRlODQyZTI4YWE1ZDQ2M2RhYzQxMDBhZmUxYzc5MWY1In0.eyJhdWQiOiIxMjI0NiIsImp0aSI6IjU3YmI4NzAxYmYzN2YxNzE1OWIwMjVkZjExNzVmZTllNDc2ODhkMjMxNDZhZTk2ZWRlODQyZTI4YWE1ZDQ2M2RhYzQxMDBhZmUxYzc5MWY1IiwiaWF0IjoxNjA5OTMzMDMxLCJuYmYiOjE2MDk5MzMwMzEsImV4cCI6MTYxMjQzODYzMSwic3ViIjoiIiwic2NvcGVzIjpbImJhc2ljIl19.sYdboDpN-QR4_0d5ViqyVY2oE8YCHcqlhBxhJb2o0PVnv9z-3rGA2pfEItBDLAFpYLn4rOLUpm48rBOhRXSii71iVaOojGSISyf0KHSXQ3E10JwGUsKw1u5aQYBGEvBtvsS-0CWGZ_tLtLOyU7XvS0UggWKTS8U043CDNCM9BZIYuGJWMBOdVsMRoXB0OepGdbP2bXBTCGH8JEoHEBMiZw8J-anOi_Jc_8P5vY1mSg82QdaoG-pieBV60dex5gwWRyYvkl6y-kjkhMY34qrluQ9hGpVXJHB2yTN5zpnA-PRpqanp37ZytjCPOzA-c-27FP9SRoypE9mdzPdsmNmIxg",
    });

    app.addLayers();

    var marker = app.addMarker({
      name: "advanced-marker",
      latlng: {
        lat: lat,
        lng: long,
      },
      icon: app.icons.purple,
      pan: false,
      history: false,
      on: {
        click: function () {
          console.log("Click callback");
        },
        contextmenu: function () {
          console.log("Contextmenu callback");
        },
      },
    });

    L.TileLayer.wmsHeader(
      "https://map.ir/shiveh",
      {
        layers: "Shiveh:Shiveh",
        format: "image/png",
        minZoom: 1,
        maxZoom: 20,
        tileSize: 128,
      },
      [
        {
          header: "x-api-key",
          value:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU3YmI4NzAxYmYzN2YxNzE1OWIwMjVkZjExNzVmZTllNDc2ODhkMjMxNDZhZTk2ZWRlODQyZTI4YWE1ZDQ2M2RhYzQxMDBhZmUxYzc5MWY1In0.eyJhdWQiOiIxMjI0NiIsImp0aSI6IjU3YmI4NzAxYmYzN2YxNzE1OWIwMjVkZjExNzVmZTllNDc2ODhkMjMxNDZhZTk2ZWRlODQyZTI4YWE1ZDQ2M2RhYzQxMDBhZmUxYzc5MWY1IiwiaWF0IjoxNjA5OTMzMDMxLCJuYmYiOjE2MDk5MzMwMzEsImV4cCI6MTYxMjQzODYzMSwic3ViIjoiIiwic2NvcGVzIjpbImJhc2ljIl19.sYdboDpN-QR4_0d5ViqyVY2oE8YCHcqlhBxhJb2o0PVnv9z-3rGA2pfEItBDLAFpYLn4rOLUpm48rBOhRXSii71iVaOojGSISyf0KHSXQ3E10JwGUsKw1u5aQYBGEvBtvsS-0CWGZ_tLtLOyU7XvS0UggWKTS8U043CDNCM9BZIYuGJWMBOdVsMRoXB0OepGdbP2bXBTCGH8JEoHEBMiZw8J-anOi_Jc_8P5vY1mSg82QdaoG-pieBV60dex5gwWRyYvkl6y-kjkhMY34qrluQ9hGpVXJHB2yTN5zpnA-PRpqanp37ZytjCPOzA-c-27FP9SRoypE9mdzPdsmNmIxg",
        },
      ]
    ).addTo(map);
  },
  methods: {
    async fetchProject() {
      await Axios.get(this.$hostname + "/todo-projects/" + this.id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.project = resp.data.project.detail[0];
          this.skills = resp.data.project.skills;
          this.lat = parseFloat(resp.data.project.detail[0].lat);
          this.long = parseFloat(resp.data.project.detail[0].long);
          setDescription(this.lat, this.long);

          this.created_at = moment(this.project.client_date).format(
            " jD jMMMM jYYYY "
          );
          this.start_at = moment(this.project.start_at).format(
            "dddd jD jMMMM jYYYY ساعت HH:mm"
          );
        })
        .catch((err) => {
          this.$router.push("/");
        });
    },
    doneProjectModal(event) {
      this.show = true;
    },
    uploadPicModal() {
      this.show_upload = true;
      this.show = false;
    },
    doneModal() {
      this.loading_submit = true;
      let data = {
        project_id: this.id,
        photos: this.selectedFiles,
      };
      Axios.post(this.$hostname + "/submit-photos", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading_submit = false;
          this.show_done = true;
          setTimeout(
            () => ((this.show_done = false), (this.show_rate = true)),
            3000
          );
        })
        .catch((err) => {
          console.log(err, "خطایی رخ داد");
        });

      this.show_upload = false;
    },
    rateModal() {
      this.loading_submit = true;

      let data = {
        comment: this.comment,
        project_id: this.id,
        client_id: this.project.client_id,
        vote: localStorage.vote,
      };
      Axios.post(this.$hostname + "/rate-comment/technician", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading_submit = false;
          localStorage.removeItem("vote");
          this.show_rate = false;
          this.$router.push("/panel/technician/2");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    onFileChange(e) {
      this.loading_photos = true;
      let file = e.target.files[0] || e.dataTransfer.files[0];

      this.createImage(file);
    },
    createImage(file) {
      let fd = new FormData();

      fd.append("photo", file);

      Axios.post(this.$hostname + "/upload-photo", fd, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading_photos = false;
          var vm = this;
          var reader = new FileReader();
          reader.onload = function (event) {
            const imageUrl = event.target.result;
            vm.images.push({ url: imageUrl, id: resp.data.photo_id });
            vm.selectedFiles.push(resp.data.photo_id);
          };
          reader.readAsDataURL(file);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    removeImage(index, photo_id) {
      this.loading_photos = true;

      let data = {
        photo_id: photo_id,
      };
      Axios.post(this.$hostname + "/delete-photo", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.images.splice(index, 1);
          this.loading_photos = false;
        })
        .catch((err) => {
          console.log(err, this.images);
        });
    },
  },
  props: {
    id: null,
  },
  data() {
    return {
      loading_photos: false,
      loading_submit: false,
      rate: 0,
      project: {},
      skills: [],
      show: false,
      show_upload: false,
      show_done: false,
      show_rate: false,
      created_at: "",
      start_at: "",
      comment: "",
      images: [],
      selectedFiles: [],
    };
  },
};
</script>

<style scoped>
img.loading-submit {
  width: 40px;
  height: 40px;
  margin: auto;
}
.copyright {
  background-color: #f7fff9;
  padding: 0 11.5%;
}
.container {
  width: 100%;
  max-width: 1366px;
  margin: auto;
  background-color: #f7fff9;
  height: 100vh;
}
.project {
  background-color: #f7fff9;
  min-height: 876px;
  height: 100%;
  width: 100%;
  max-width: 1366px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto;
  padding-top: 30px;
}

.project .project-card {
  min-height: 690px;
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
  align-items: center;
}
.body .title {
  font-size: 24px;
  font-weight: bold;
  color: #7ab383;
}
.header .budget {
  border-radius: 5px;
  box-shadow: 0 0 10px 0 rgba(92, 67, 138, 0.15);
  background-color: #ffffff;
  color: #7ab383;
  padding: 8px;
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: 500;
  width: 250px;
  max-height: 47px;
  margin-left: 50px;
}
.header .client {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  margin: 30px 0;
}
.header .client .info {
  display: flex;
}
.header .client .info .photo {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 120px;
  height: 120px;
  border-radius: 50%;
}
.header .client .info .details {
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

.header .client .info .details .register-date {
  color: #000;
  font-size: 16px;
  font-weight: 500;
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
.actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: auto;
  width: 50%;
}
.actions button {
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
.actions button:hover {
  background-color: #7ab383;
  color: #fff;
  transition: 0.4s ease;
}

/* Modal general style */
/* The Modal (background) */
.modal {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgba(122, 179, 131, 0.2); /* Fallback color */
  background-color: rgba(122, 179, 131, 0.2); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  width: 37%; /* Full width */
  height: 330px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  justify-content: center;
  flex-direction: column;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
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
.modal-content .header {
  display: flex;
  color: #000;
  font-size: 22px;
  font-weight: 500;
  justify-content: space-between;
  align-items: center;
  border-bottom: solid 2px #7ab38318;
  padding-bottom: 15px;
}
.modal-content .header .title {
  display: flex;
  justify-self: center;
  align-self: flex-end;
  margin: 0 auto;
}
.close,
.close-upload {
  display: flex;
  justify-self: flex-end;
  background-image: url("../../../../assets/panel/green/Close.svg");
  background-repeat: no-repeat;
  background-size: contain;
  width: 15px;
  height: 15px;
  margin-left: 3%;
}
.close-upload {
  height: 55px;
}
.close:hover,
.close-upload:hover {
  cursor: pointer;
}
.logout-icon {
  background-image: url("../../../../assets/panel/green/done.svg");
  display: flex;
  margin: 30px;
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
button.accept,
button.next,
button.done {
  background-color: #fff;
  border-radius: 5px;
  border: 2px solid #7ab383;
  outline: none;
  font-size: 16px;
  font-weight: bold;
  width: 150px;
  color: #7ab383;
  height: 40px;
  width: 40%;
  transition: 0.4s ease;
  cursor: pointer;
}
button.accept:hover,
button.next:hover,
button.done:hover {
  background-color: #7ab383;
  color: #fff;
  transition: 0.4s ease;
}
/* 
* styles for upload pic modal 
*/
#uploadpic .modal-content {
  width: 50%;
  height: 370px;
}
#uploadpic .modal-content .header {
  height: 30px;
}
#uploadpic .content {
  align-items: flex-start;
  padding-top: 30px;
}
#uploadpic p {
  text-align: right;
  padding: 20px;
  margin: 0;
}
#uploadpic .modal-content .header .title {
  color: #7ab383;
}
.upload {
  margin: auto;
  display: flex;
  justify-content: space-between;
  width: 93%;
}
.btn-upload {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 14px;
  font-weight: 500;
  color: #000;
}
.btn-upload label {
  border: 2px dashed rgba(122, 179, 131, 0.192);
  background-image: url("../../../../assets/plus_green.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 70px;
  width: 130px;
  height: 130px;
  cursor: pointer;
  display: inline-block;
  margin: 10px auto;
  margin-bottom: 10px;
  transition: 0.4s ease;
}
.btn-upload label:hover {
  border: 2px solid rgba(122, 179, 131, 0.637);
  border-radius: 10px;
  background-color: rgba(122, 179, 131, 0.068);
  transition: 0.3s ease;
}

/* 
* style done modal 
*/

#doneModal .modal-content {
  width: 30%;
  height: 290px;
}
/* 
* styles rate modal 
*/
#rate-modal .modal-content .header {
  height: 70px;
  color: #7ab383;
}
#rate-modal .modal-content {
  justify-content: space-between;
  height: 390px;
  width: 50%;
}
#rate-modal .modal-content .content {
  justify-content: space-between;
  align-items: unset;
}
#rate-modal p {
  text-align: right;
}
#rate-modal .yes-no {
  margin-bottom: 40px;
  margin-top: 45px;
}
.comment,
.rate {
  width: 94% !important;
  margin: 10px 20px;
}
.rate {
  display: flex;
  justify-content: space-between;
}
.comment p,
.rate p {
  padding: 0 !important;
  margin: 0;
  display: flex;
  justify-content: space-between;
  width: 60%;
}
textarea {
  height: 194px;
  width: 100%;
  padding: 10px;
  opacity: 0.2;
  border-radius: 5px;
  outline: none;
  border: solid 1px #7ab383;
  resize: none;
  transition: 0.4s ease;
  font-family: IRANsans;
}
textarea:focus {
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  opacity: 1;
  transition: 0.4s ease;
}

input#cost {
  border-radius: 5px;
  border: solid 1px #7ab383;
  outline: none;
  width: 35%;
  text-align: left;
  font-size: 20px;
  font-family: IRANsans;
  padding: 10px;
  transition: 0.4s ease;
  height: 44px;
  opacity: 0.6;
}
input#cost:focus {
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.4s ease;
  opacity: 1;
}
.images {
  display: flex;
  margin: 0px auto;
  width: 80%;
  overflow-x: scroll;
  flex-wrap: nowrap;
}
.img {
  position: relative;
  height: 100px;
  margin: 5px;
}
.img:hover img {
  filter: blur(3px);
}
.img:hover .image-done {
  opacity: 1;
}
img {
  width: 130px;
  height: 130px;
  border-radius: 10px;
  transition: 0.4s ease;
  z-index: 1;
}

.image-done {
  z-index: 999;
  width: 50px;
  height: 50px;
  position: absolute;
  top: 50%;
  right: 50%;
  transform: translate(50%, -25%);
  border-radius: 50%;
  background-image: url("../../../../assets/delete.svg");
  padding: 10px;
  background-position: center;
  background-color: rgba(255, 255, 255, 0.459);
  background-repeat: no-repeat;
  background-size: 30px;
  transition: 0.4s ease;
  cursor: pointer;
  opacity: 0;
}
/* 
* effect show/hide modals 
*/
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
@media screen and (max-width: 540px) {
  .project {
    padding-top: 72px;
    min-height: 700px;
    height: auto;
  }
  .project .project-card {
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
  .modal-content {
    width: 90%;
  }
  #uploadpic .modal-content {
    width: 90%;
    height: fit-content;
  }
  #uploadpic .modal-content .header {
    flex-direction: row;
    height: 60px;
  }
  .close-upload {
    height: 20px;
  }
  #uploadpic .content {
    align-items: center;
    height: fit-content;
    margin: 0 auto;
    padding-top: 0;
  }
  #uploadpic p {
    padding: 0 4%;
    margin: 0;
  }
  #uploadpic button {
    width: 90%;
    margin: 10px 10px;
  }
  #doneModal .modal-content {
    width: 90%;
    height: fit-content;
  }
  #rate-modal .modal-content {
    height: fit-content;
    width: 90%;
  }
  #rate-modal .content {
    align-items: center;
    height: fit-content;
    margin: 0 auto;
    padding-top: 0;
  }
  #rate-modal .modal-content .header {
    flex-direction: row;
    height: 60px;
  }
  .rate {
    flex-direction: column;
  }
  textarea {
    width: 90%;
  }
  #rate-modal .yes-no {
    margin: 10px auto;
  }
  #rate-modal button.done {
    width: 100%;
  }
}

#mapirt {
  min-height: 100px;
  border-radius: 10px;
  width: 95%;
  position: absolute !important;
  height: 27%;
  display: block;
}
</style>
