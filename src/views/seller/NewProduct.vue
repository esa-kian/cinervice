<template>
  <div>
    <div class="header">
      <h1>Create new product</h1>
      <router-link to="/seller/profile">
        <v-btn class="mx-2" fab dark color="indigo">
          <v-icon dark> mdi-chevron-left </v-icon>
        </v-btn>
      </router-link>
    </div>

    <div class="body">
      <v-form>
        <v-container>
          <div class="photo">
            <input @change="setPhoto" type="file" name="photo" id="photo" />
            <label
              v-if="url"
              for="photo"
              @click.prevent="deletePhoto"
              :style="{ 'background-image': 'url(' + url + ')' }"
            ></label>
            <label v-else for="photo" id="upload"></label>
          </div>
          <v-row>
            <v-col cols="12" sm="6" md="3">
              <v-text-field v-model="name" label="Name"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="3">
              <v-text-field
                v-model="description"
                label="Description"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="3">
              <v-text-field v-model="number" label="Number"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" sm="6" md="3">
              <v-text-field v-model="price" label="Price"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="3">
              <v-text-field
                v-model="price_with_discount"
                label="Price with discount"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-btn @click="submit" class="mx-8" fab dark color="indigo">
            submit
          </v-btn>
        </v-container>
      </v-form>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    submit() {
      let fd = new FormData();
      fd.append("photo", this.photo);
      fd.append("name", this.name);
      fd.append("description", this.description);
      fd.append("number", this.number);
      fd.append("price", this.price);
      fd.append("priceWithDiscount", this.price_with_discount);

      this.$http
        .post(this.$hostname + "/seller/product", fd, this.$config)
        .then((resp) => {
          console.log(resp.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

    setPhoto(e) {
      this.photo = e.target.files[0] || e.dataTransfer.files[0];

      this.url = URL.createObjectURL(this.photo);
    },
    deletePhoto() {
      this.photo = "";
    },
  },
  data() {
    return {
      items: [],
      photo: "",
      url: "",
      name: "",
      description: "",
      number: "",
      price: "",
      price_with_discount: "",
    };
  },
};
</script>

<style scoped>
.header {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}
.photo {
  width: 100%;
  height: 116px;
  border-radius: 8px;
  padding: 10px;
  border: 1px solid rgba(38, 50, 56, 0.5);
  margin: 10px 0;
}
.photo label {
  border: 1px dashed #e8505b;
  border-radius: 8px;
  width: 100%;
  background-position: center;
  min-height: 85px;
  background-size: cover;
}
</style>