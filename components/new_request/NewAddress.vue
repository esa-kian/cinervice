<template>
  <div class="main-address">
    <div class="city-town">
      <div class="city">
        <label for="">شهر</label>
        <select @change="setCity" name="city" id="cities" v-model="city">
          <option v-for="city in cities" :key="city.id" :value="city.id">
            {{ city.title }}
          </option>
        </select>
      </div>
      <div class="town">
        <label for="town">محله</label>
        <select @change="setTown" name="town" id="towns" v-model="town">
          <option v-for="town in towns" :key="town.id" :value="town.id">
            {{ town.title }}
          </option>
        </select>
      </div>
    </div>
    <div class="detail">
      <label for="">آدرس</label>
      <textarea
        @change="setDescription"
        v-model="state.desc"
        name="description"
        id="description"
        cols="30"
        rows="5"
      ></textarea>
    </div>

    <div id="mapir"></div>
  </div>
</template>

<script>
import Axios from "axios";
import { latLng, latLngBounds, icon } from "leaflet";
import { LMap, LTileLayer, LIcon, LMarker } from "vue2-leaflet";
import L from "leaflet";
import "leaflet-wms-header";

import Vue from "vue";
const setDescription = (e, lat, long) => {
  Vue.prototype.state.desc = e;
  localStorage.description = e;
  localStorage.lat = lat;
  localStorage.long = long;
};

export default {
  name: "NewAddress",
  mounted() {
    this.fetchCities();
    this.fetchTowns(localStorage.city);

    $(document).ready(function () {
      var app = new Mapp({
        element: "#mapir",
        presets: {
          latlng: {
            lat: 29.613029,
            lng: 52.516156,
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
      app.map.on("click", function (e) {
        var marker = app.addMarker({
          name: "advanced-marker",
          latlng: {
            lat: e.latlng.lat,
            lng: e.latlng.lng,
          },
          icon: app.icons.purple,

          pan: false,
          draggable: true,
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
        marker.on("dragend", function () {
          let lat = marker.getLatLng().lat;
          let long = marker.getLatLng().lng;
          let address = "";
          Axios.get("https://map.ir/reverse/no?lat=" + lat + "&lon=" + long, {
            headers: {
              "x-api-key":
                "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU3YmI4NzAxYmYzN2YxNzE1OWIwMjVkZjExNzVmZTllNDc2ODhkMjMxNDZhZTk2ZWRlODQyZTI4YWE1ZDQ2M2RhYzQxMDBhZmUxYzc5MWY1In0.eyJhdWQiOiIxMjI0NiIsImp0aSI6IjU3YmI4NzAxYmYzN2YxNzE1OWIwMjVkZjExNzVmZTllNDc2ODhkMjMxNDZhZTk2ZWRlODQyZTI4YWE1ZDQ2M2RhYzQxMDBhZmUxYzc5MWY1IiwiaWF0IjoxNjA5OTMzMDMxLCJuYmYiOjE2MDk5MzMwMzEsImV4cCI6MTYxMjQzODYzMSwic3ViIjoiIiwic2NvcGVzIjpbImJhc2ljIl19.sYdboDpN-QR4_0d5ViqyVY2oE8YCHcqlhBxhJb2o0PVnv9z-3rGA2pfEItBDLAFpYLn4rOLUpm48rBOhRXSii71iVaOojGSISyf0KHSXQ3E10JwGUsKw1u5aQYBGEvBtvsS-0CWGZ_tLtLOyU7XvS0UggWKTS8U043CDNCM9BZIYuGJWMBOdVsMRoXB0OepGdbP2bXBTCGH8JEoHEBMiZw8J-anOi_Jc_8P5vY1mSg82QdaoG-pieBV60dex5gwWRyYvkl6y-kjkhMY34qrluQ9hGpVXJHB2yTN5zpnA-PRpqanp37ZytjCPOzA-c-27FP9SRoypE9mdzPdsmNmIxg",
            },
          })
            .then((resp) => {
              address = resp.data.address;
              setDescription(address, lat, long);
            })
            .catch((err) => {
              console.log(err.response.data.message);
            });
        });
      });
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
  components: {
    LMap,
    LTileLayer,
    LIcon,
    LMarker,
  },
  methods: {
    fetchCities() {
      Axios.get(this.$hostname + "/cities", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.cities = resp.data.cities;
        })
        .catch((err) => {
          console.log(err, "can not fetch cities");
        });
    },
    setCity() {
      localStorage.setItem("city", this.city);
      let c = document.getElementById("cities");
      let city_title = c.options[c.selectedIndex].text;
      localStorage.setItem("city_title", city_title);
      this.fetchTowns(localStorage.city);
    },
    fetchTowns(city) {
      Axios.get(this.$hostname + "/cities/" + city + "/towns", {
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
    setTown() {
      localStorage.setItem("town", this.town);
      let t = document.getElementById("towns");
      let town_title = t.options[t.selectedIndex].text;
      localStorage.setItem("town_title", town_title);
    },
    setLatLong(e) {
      localStorage.setItem("lat", e.lat);
      localStorage.setItem("long", e.lng);
    },
    setDescription() {
      localStorage.setItem("description", this.description);
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
    innerClick() {
      alert("Click!");
    },
    handleClickMap(e) {
      localStorage.setItem("lat", e.latlng.lat);
      localStorage.setItem("long", e.latlng.lng);
    },
  },
  data() {
    return {
      cities: [],
      city: localStorage.city,
      towns: [],
      town: localStorage.town,
      description: "",
      lat: 29.613029,
      long: 52.516156,
    };
  },
};
</script>

<style scoped>
.main-address {
  display: flex !important;
  flex-direction: column !important;
  min-height: 340px !important;
  width: 100% !important;
  max-height: 320px !important;
  min-height: 320px !important;
  position: relative !important;
}
.main-address .city-town {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  padding: 10px;
}
.city,
.town {
  display: flex;
  flex-direction: column;
  width: 50%;
}
.city {
  padding-left: 15px;
}
.town {
  padding-right: 15px;
}
.detail {
  display: flex;
  flex-direction: column;
  width: 100%;
  padding: 10px;
}
.map {
  position: absolute;
  display: block;
  min-height: 100px;
}
select {
  background-image: url("../../assets/FAQ/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-x: 15px;
  background-position-y: 15px;
  background-size: 15px;
  outline: none;
  appearance: none;
  border: solid 2px #5c438a38;
  background-color: #fff;
  border-radius: 5px;
  height: 44px;
  font-size: 14px;
  font-weight: 500;
  margin-top: 10px;
  margin-bottom: 20px;
  font-family: IRANSans;
  padding-right: 10px;
  width: 100%;
  transition: 0.3s ease;
}
select:hover {
  border: solid 2px #5c438a;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.3s ease;
}
select option {
  background: #5c438a0a;
  color: #5c438a;
}
textarea {
  padding: 10px 10px;
  border-radius: 5px;
  font-family: IRANSans;
  outline: none;
  border: solid 2px #61488f2a;
  margin: 10px 0;
  width: 100%;
  height: 80px;
  resize: none;
}
textarea:hover {
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.055);
}
.mapouter {
  position: relative;
  text-align: right;
  height: 265px;
  width: 559px;
}
.gmap_canvas {
  overflow: hidden;
  background: none !important;
  height: 265px;
  width: 559px;
}

#mapir {
  display: block;
  min-height: 140px;
  border-radius: 10px;
  width: 100%;
  height: 70%;
  
}
@media screen and (max-width: 540px) {
  label {
    font-size: 0.9rem;
  }
}
</style>