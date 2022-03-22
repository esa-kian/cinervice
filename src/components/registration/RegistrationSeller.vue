<template>
  <v-card>
    <v-tabs
      v-model="tab"
      background-color="deep-purple accent-4"
      centered
      dark
      icons-and-text
    >
      <v-tabs-slider></v-tabs-slider>

      <v-tab href="#tab-1">
        ورود
        <v-icon>mdi-login</v-icon>
      </v-tab>

      <v-tab href="#tab-2">
        عضویت
        <v-icon>mdi-account-plus</v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="i in 2" :key="i" :value="'tab-' + i">
        <v-card flat>
          <v-card-text>
            <login v-if="i == 1"></login>
            <signup v-if="i == 2"></signup>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
import Login from "./LoginSeller";
import Signup from "./SignupSeller";

export default {
  components: {
    Login,
    Signup,
  },
  data() {
    return {
      tab: null,
    };
  },
};
</script>