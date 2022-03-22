import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Registration from "../views/Registration.vue";
import ClientProfile from "../views/client/Profile.vue";
import SellerProfile from "../views/seller/Profile.vue";
import NewProduct from "../views/seller/NewProduct";
import EditProduct from "../views/seller/EditProduct.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/registration",
    name: "Registration",
    component: Registration,
  },
  {
    path: "/client/profile",
    name: "ClientProfile",
    component: ClientProfile,
  },
  {
    path: "/seller/profile",
    name: "SellerProfile",
    component: SellerProfile,
  },
  {
    path: "/new-product",
    name: "NewProduct",
    component: NewProduct,
  },
  {
    path: "/edit-product/:id",
    name: "EditProduct",
    component: EditProduct,
    props: true,
  },
 
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
