<template>
  <v-container class="lighten-1 md-3 lg-3 sm-3 xs-3">
    <v-row no-gutters>
      <v-col cols="12">
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field
                v-model="firstname"
                :rules="nameRules"
                label="نام"
                required
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="4">
              <v-text-field
                v-model="lastname"
                :rules="nameRules"
                label="نام خانوادگی"
                required
              ></v-text-field>
            </v-col>

            <v-col cols="12" md="4">
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="ایمیل"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
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
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="about" label="درباره"></v-text-field>
            </v-col>
            <v-col cols="6" md="2">
              <v-text-field v-model="birthday" label="تاریخ تولد"></v-text-field>
            </v-col>
            <v-col cols="6" md="2">
              <v-select v-model="sex" :items="gender" label="جنسیت"></v-select>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12" md="4">
              <v-text-field v-model="address" label="آدرس"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="city" label="شهر"></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="phone" label="تلفن"></v-text-field>
            </v-col>
          </v-row>

          <v-btn
            :disabled="!valid"
            color="primary"
            class="mr-4"
            @click="submit"
          >
            ثبت نام
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
        firstName: this.firstname,
        lastName: this.lastname,
        password: this.password,
        email: this.email,
        address: this.address,
        phone: this.phone,
        city: this.city,
        sex: this.sex,
        about: this.about,
        birthday: this.birthday,
      };

      this.$http.post(this.$hostname + "/register", data)
        .then((resp) => {
          console.log(resp.data);
          localStorage.setItem("token", resp.data.token);
          this.$router.push("/client/profile");
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
  },
  data: () => ({
    valid: false,
    firstname: "",
    lastname: "",
    nameRules: [(v) => !!v || "Name is required"],
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+/.test(v) || "E-mail must be valid",
    ],
    password: "",
    show1: false,
    passwordRules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 8 || "Min 8 characters",
      emailMatch: () => `The email and password you entered don't match`,
    },
    address: "",
    phone: "",
    city: "",
    about: "",
    birthday: "",
    gender: ["مرد", "زن"],
    sex: "",
  }),
};
</script>
