<template>
  <div>
    <div class="main">
      <div class="title">آدرس مورد نظر را انتخاب کنید.</div>
      <img
        v-if="loading"
        class="loading"
        src="../../assets/loading.svg"
        alt="loading"
      />
      <div v-else class="addresses">
        <div v-for="(address, index) in addresses" :key="address.id">
          <label :for="'address_' + index">
            <input
              @click="
                setAddress(
                  address.id,
                  address.city.id,
                  address.town.title,
                  address.city.title,
                  address.description
                )
              "
              type="radio"
              :id="'address_' + index"
              name="address"
              :checked="address_id == address.id"
            />
            {{
              address.city.title +
              ", " +
              address.town.title +
              ", " +
              address.description
            }}
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "StepFive",
  mounted() {
    this.fetchAddresses();
    if (localStorage.address) {
      this.$emit("continue_btn", true);
    }
  },
  methods: {
    fetchAddresses() {
      Axios.get(this.$hostname + "/addresses", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.addresses = resp.data.addresses;
          this.loading = false;
        })
        .catch((err) => {
          console.log(err, "can not fetch addresses");
        });
    },
    setAddress(address, city_id, town, city_title, description) {
      this.address_id = address;
      this.$emit("continue_btn", true);
      localStorage.setItem("address", this.address_id);
      localStorage.setItem("city", city_id);
      localStorage.setItem("town", town);
      localStorage.setItem("city_title", city_title);
      localStorage.setItem("description", description);
    },
  },
  data() {
    return {
      addresses: [],
      loading: true,
      address_id: localStorage.address,
      city_id: localStorage.city_id,
    };
  },
};
</script>

<style scoped>
.addresses {
  display: flex;
  flex-direction: column;
  max-height: 220px;
  overflow: scroll;
}
img.loading {
  width: 100px;
  height: 100px;
  margin: 0 auto;
}
label {
  display: flex;
  justify-content: flex-start;
  padding: 20px;
  border-radius: 5px;
  border: solid 2px #5c438a18;
  margin-top: 20px;
  transition: 0.4s ease;
}

input {
  appearance: none;
  background-image: url("../../assets/radio_off.svg");
  background-repeat: no-repeat;
  background-size: 20px;
  width: 30px;
  height: 30px;
  outline: none;
  margin: 5px 5px 0 12px;
}
input:checked {
  background-image: url("../../assets/radio_on.svg");
}

label:hover {
  border: solid 2px #5c438a;
  transition: 0.4s ease;
  cursor: pointer;
}

@media screen and (max-width: 540px) {
  .title {
    font-size: 1rem;
  }
  label {
    padding: 10px 5px;
    font-size: 0.8rem;
  }
  input {
    background-size: contain;
    width: 25px;
    height: 25px;
    margin: 5px 7px;
  }
}
</style>