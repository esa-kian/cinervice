<template>
  <v-app>
    <v-toolbar align-items="baseline" flat height="75">
      <v-switch
        v-model="$vuetify.theme.dark"
        inset
        label="حالت شب"
        persistent-hint
      ></v-switch>

      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-icon @click="logout" color="primary" dark v-bind="attrs" v-on="on">
            mdi-logout
          </v-icon>
        </template>
        <span>خروج</span>
      </v-tooltip>

      <router-link to="/">
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-icon color="primary" dark v-bind="attrs" v-on="on">
              mdi-home
            </v-icon>
          </template>
          <span>خانه</span>
        </v-tooltip>
      </router-link>

      <router-link to="/client/profile">
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-icon color="primary" dark v-bind="attrs" v-on="on">
              mdi-human
            </v-icon>
          </template>
          <span>پروفایل</span>
        </v-tooltip>
      </router-link>

      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-icon @click="shop" color="primary" dark v-bind="attrs" v-on="on">
            mdi-cart
          </v-icon>
        </template>
        <span>خرید</span>
      </v-tooltip>
      <v-alert
        v-if="success"
        @click="success = false"
        dense
        text
        type="success"
      >
        {{ message }}
      </v-alert>
    </v-toolbar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/registration");
    },
    async shop() {
      await this.$http
        .get(this.$hostname + "/customer/buyproducts", this.$config)
        .then((resp) => {
          this.success = true;
          this.message = resp.data.msg;
        
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
  },
  data: () => ({
    success: false,
    message: "",
  }),
};
</script>
<style scoped>
.primary--text {
  margin: 0 10px;
}
</style>