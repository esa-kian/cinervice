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
        به عنوان مشتری
        <v-icon>mdi-heart</v-icon>
      </v-tab>

      <v-tab href="#tab-2">
       به عنوان فروشنده
        <v-icon>mdi-shopping</v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="i in 2" :key="i" :value="'tab-' + i">
        <v-card flat>
          <v-card-text>
            <client v-if="i == 1"></client>
            <seller v-if="i == 2"></seller>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
import Client from "../components/registration/RegistrationClient";
import Seller from "../components/registration/RegistrationSeller";

export default {
  components: {
    Client,
    Seller,
  },
  data() {
    return {
      tab: null,
    };
  },
};
</script>