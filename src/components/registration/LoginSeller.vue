<template>
  <v-container class="lighten-1 md-3 lg-3 sm-3 xs-3">
    <v-row no-gutters>
      <v-col cols="12">
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="ایمیل"
            required
          ></v-text-field>
          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[passwordRules.required, passwordRules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="رمز"
            hint="At least 8 characters"
            counter
            @click:append="show1 = !show1"
          ></v-text-field>

          <v-checkbox
            v-model="checkbox"
            label="مرا بخاطر بسپار"
            required
          ></v-checkbox>

          <v-btn
            :disabled="!valid"
            color="primary"
            class="mr-4"
            @click="submit"
          >
            ورود
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    submit() {
      let data = {
        email: this.email,
        password: this.password,
      };

      this.$http
        .post(this.$hostname + "/sellerlogin", data)
        .then((resp) => {
          console.log(resp.data);
          localStorage.setItem("token", resp.data.token);
          this.$router.push("/seller/profile");
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
  },
  data: () => ({
    valid: true,
    password: "",
    show1: false,
    passwordRules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 8 || "Min 8 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    checkbox: false,
  }),
};
</script>
