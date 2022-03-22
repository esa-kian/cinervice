<template>
  <div>
    <div class="main">
      <div class="title">
        در صورت نیاز، تصاویر مرتبط با درخواست خود را آپلود کنید.
      </div>
      <img
        v-if="loading"
        class="loading"
        src="../../assets/loading.svg"
        alt="loading"
      />
      <div v-else class="image">
        <div class="upload-btn">
          <label for="photo"></label>
          <input
            type="file"
            id="photo"
            ref="file"
            @change="onFileChange"
            hidden
          />
          <span>بارگذاری تصویر</span>
        </div>
        <div class="images" v-if="images">
          <div class="img" v-for="(image, index) in images" :key="index">
            <div @click="removeImage(index, image.id)" class="image-done"></div>

            <img :src="image.url" width="100" height="auto" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "StepFour",
  mounted() {
    this.$emit("continue_btn", true);
  },
  methods: {
    onFileChange(e) {
      this.loading = true;

      let file = e.target.files[0] || e.dataTransfer.files[0];

      this.createImage(file);
    },
    createImage(file) {
      let fd = new FormData();
      this.$emit("continue_btn", false);

      fd.append("photo", file);

      Axios.post(this.$hostname + "/upload-photo", fd, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.$emit("continue_btn", true);

          var vm = this;
          var reader = new FileReader();
          reader.onload = function (event) {
            const imageUrl = event.target.result;
            vm.images.push({ url: imageUrl, id: resp.data.photo_id });
            vm.selectedFiles.push(resp.data.photo_id);

            localStorage.setItem("photos", vm.selectedFiles);
          };
          reader.readAsDataURL(file);
        })
        .catch((err) => {
          this.$router.push("/register/user");
        });
    },
    removeImage(index, photo_id) {
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
        })
        .catch((err) => {
          console.log(err, this.images);
        });
    },
  },
  data() {
    return {
      images: [],
      showImage: false,
      selectedFiles: [],
      loading: false,
    };
  },
};
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}
img.loading {
  width: 80px;
  height: 80px;
  margin: auto;
}
.main label {
  border: 2px dashed rgba(92, 67, 138, 0.15);
  background-image: url("../../assets/plus.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 70px;
  width: 100px;
  height: 100px;
  cursor: pointer;
  display: inline-block;
  margin: 30px 5%;
  margin-bottom: 10px;
  transition: 0.4s ease;
}
.main label:hover {
  border: 2px solid rgba(92, 67, 138, 0.637);
  border-radius: 10px;
  background-color: rgba(105, 71, 167, 0.068);
  transition: 0.3s ease;
}
.main span {
  margin-right: 7%;
  font-size: 14px;
  font-weight: 500;
  color: #000;
}
div.image {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.images {
  display: flex;
  flex-wrap: wrap;
  margin: 30px auto;
  width: 80%;
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
.upload-btn {
  display: flex;
  flex-direction: column;
}
img {
  width: 100px;
  height: 100px;
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
  transform: translate(50%, -50%);
  border-radius: 50%;
  background-image: url("../../assets/delete.svg");
  padding: 10px;
  background-position: center;
  background-color: rgba(255, 255, 255, 0.459);
  background-repeat: no-repeat;
  background-size: 30px;
  transition: 0.4s ease;
  cursor: pointer;
  opacity: 0;
}

@media screen and (max-width: 540px) {
  .title {
    font-size: 1rem;
  }
}
</style>