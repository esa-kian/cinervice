<template>
  <div class="body">
    <h1>سلام {{ first_name }}</h1>
    <v-form>
      <v-container>
        <v-row>
          <v-col cols="12" sm="6" md="3">
            <v-text-field
              v-model="first_name"
              label="نام"
            ></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="3">
            <v-text-field v-model="last_name" label="نام خانوادگی"></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="3">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              required
              label="ایمیل"
            ></v-text-field>
          </v-col>
          <v-btn @click="submit" class="mx-8" fab dark color="indigo">
            <v-icon dark> mdi-check </v-icon>
          </v-btn>
        </v-row>
      </v-container>
    </v-form>

    <div class="header">
      <h1>فاکتور ها</h1>
    </div>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">وضعیت</th>
            <th class="text-left">جمع مبلغ</th>
            <th class="text-left">تعداد</th>
        
          </tr>
        </thead>
        <tbody>
          <tr v-for="factor in factors" :key="factor._id">
            <td>{{ factor.condition }}</td>
            <td>{{ factor.totalPrice }}</td>
            <td>{{ factor.items.length }}</td>
           
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  mounted() {
    this.fetch();
  },
  methods: {
    fetch() {
      this.$http
        .get(this.$hostname + "/customer/profile", this.$config)
        .then((resp) => {
          console.log(resp.data);
          this.first_name = resp.data.item.firstName;
          this.last_name = resp.data.item.lastName;
          this.email = resp.data.item.email;
        })
        .catch((err) => {
          if (err.response.status == 403) {
            this.$router.push("/seller/profile");
          }
        });
      this.$http
        .get(this.$hostname + "/customer/userfactors", this.$config)
        .then((resp) => {
          console.log(resp, "hey");
          this.factors = resp.data.items;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    submit() {
      let data = {
        firstName: this.first_name,
        lastName: this.last_name,
        password: this.password,
        email: this.email,
      };

      this.$http
        .put(this.$hostname + "/customer/editprofile", data, this.$config)
        .then((resp) => {
          console.log(resp.data);
        })
        .catch((err) => {
          console.log(err.response.data);
        });
    },
  },
  data() {
    return {
      factors: [],
      first_name: "",
      last_name: "",
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
      email: "",
    };
  },
};
</script>
<style scoped>
.body {
  padding: 20px;
}
</style>