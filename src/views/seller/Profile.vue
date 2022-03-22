<template>
  <div>
    <div class="header">
      <h1>محصولات</h1>
      <router-link to="/new-product">
        <v-btn class="mx-2" fab dark color="indigo">
          <v-icon dark> mdi-plus </v-icon>
        </v-btn>
      </router-link>
    </div>

    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">عنوان</th>
            <th class="text-left">گالری</th>
            <th class="text-left">ویرایش</th>
            <th class="text-left">حذف</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item._id">
            <td>{{ item.name }}</td>
            <td>{{ item.gallery.address }}</td>
            <td>
              <router-link :to="'/edit-product/' + item._id">
                <v-btn class="mx-2" fab dark color="indigo">
                  <v-icon dark> mdi-pencil </v-icon>
                </v-btn>
              </router-link>
            </td>
            <td>
              <v-btn
                @click="deleteProduct(item._id)"
                class="mx-2"
                fab
                dark
                color="indigo"
              >
                <v-icon dark> mdi-delete </v-icon>
              </v-btn>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
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
            <td>
              <router-link :to="'/edit-product/' + factor._id">
                <v-btn class="mx-2" fab dark color="indigo">
                  <v-icon dark> mdi-pencil </v-icon>
                </v-btn>
              </router-link>
            </td>
            <td>
              <v-btn
                @click="deleteProduct(factor._id)"
                class="mx-2"
                fab
                dark
                color="indigo"
              >
                <v-icon dark> mdi-delete </v-icon>
              </v-btn>
            </td>
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
        .get(this.$hostname + "/products")
        .then((resp) => {
          this.items = resp.data.items;
          console.log(resp.data);
        })
        .catch((err) => {
          console.log(err.response.data);
        });

      this.$http
        .get(this.$hostname + "/seller/galleryfactors", this.$config)
        .then((resp) => {
          this.factors = resp.data.items;
          console.log(resp.data);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    deleteProduct(id) {
      this.$http
        .delete(this.$hostname + "/seller/product?id=" + id, this.$config)
        .then((resp) => {
          console.log(resp);
          this.fetch();
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
  },
  data() {
    return {
      items: [],
      factors: [],
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
</style>