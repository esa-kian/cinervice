<template>
  <div>
    <div v-if="!loading" class="account">
      <div class="header">
        <div class="edit">
          <a @click.prevent="editable">ویرایش</a>
        </div>
        <label
          :style="{ 'background-image': 'url(' + avatar + ')' }"
          for="photo"
        ></label>

        <input
          type="file"
          id="photo"
          name="photo"
          @change="setProfilePic"
          hidden
          :disabled="edit == false"
        />
      </div>
      <div class="details">
        <span v-if="alert" @click="alert = false" class="success">{{
          message
        }}</span>
        <div class="row-one">
          <div class="first-name">
            <label for="first_name">نام</label>
            <input
              type="text"
              name="first_name"
              id="first_name"
              @change="edit_user(1)"
              v-model="account.first_name"
              :disabled="edit == false"
            />
          </div>
          <div class="last-name">
            <label for="last_name">نام خانوادگی</label>
            <input
              type="text"
              name="last_name"
              id="last_name"
              @change="edit_user(2)"
              v-model="account.last_name"
              :disabled="edit == false"
            />
          </div>
          <div class="birthday">
            <label for="birthday">تاریخ تولد</label>
            <input
              type="text"
              name="birthday"
              id="birthday"
              placeholder="روز/ماه/سال"
              @change="edit_user(3)"
              v-model="account.birthdate"
              :disabled="edit == false"
            />
          </div>
        </div>
        <div class="row-two">
          <div class="email">
            <label for="email">ایمیل</label>
            <input
              type="text"
              name="email"
              id="email"
              v-model="email.email"
              @change="edit_user(4)"
              :disabled="edit == false"
            />
          </div>
          <div class="phone">
            <label for="phone_number">شماره موبایل</label>
            <input
              type="text"
              name="phone_number"
              id="phone_number"
              v-model="account.phone_number"
              disabled
            />
          </div>
          <div class="gender">
            <label for="gender">جنسیت</label>
            <div class="radios">
              <input
                type="radio"
                name="gender"
                id="female"
                value="female"
                :checked="account.gender == 'female'"
                @focus="edit_user(6)"
                :disabled="edit == false"
              />
              <label for="female"> زن </label>
              <input
                type="radio"
                name="gender"
                id="male"
                value="male"
                @focus="edit_user(7)"
                :checked="account.gender == 'male'"
                :disabled="edit == false"
              />
              <label for="male"> مرد </label>
            </div>
          </div>
        </div>
        <div class="row-three">
          <div class="iban">
            <label for="iban">شماره شبا</label>

            <input
              type="text"
              name="iban"
              id="iban"
              v-model="iban"
              @focus="edit_user(8)"
              @input="ibandExplorer"
              :disabled="edit == false"
            />
          </div>

          <div class="bank">
            <label for="bank">بانک</label>
            <input v-model="bank" type="text" name="bank" id="bank" disabled />
          </div>
        </div>
      </div>
      <div class="address">
        <div class="title">
          <div class="my-address">آدرس های من</div>
          <div class="new-address">
            <a @click.prevent="add_address = true"> افزودن آدرس جدید</a>
          </div>
        </div>
        <div class="addresses" v-for="address in addresses" :key="address.id">
          <div class="desc">{{ address.description }}</div>
          <span class="delete" @click="deleteAddress(address.id)"></span>
        </div>
      </div>
      <!-- done bid modal  -->
      <transition name="fade">
        <div id="addressModal" class="modal" v-if="add_address">
          <div class="modal-content">
            <div class="content">
              <NewAddress />
              <div class="buttons">
                <button @click.prevent="new_address">ذخیره ی آدرس</button>
                <button @click.prevent="add_address = false">انصراف</button>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
    <div v-else>
      <img class="loading" src="../../../assets/loading.svg" alt="loading" />
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import NewAddress from "../../new_request/NewAddress";

export default {
  name: "Account",
  components: {
    NewAddress,
  },
  data() {
    return {
      edit: false,
      account: null,
      avatar: null,
      email: null,
      iban: null,
      bank: "",
      addresses: [],
      add_address: false,
      alert: false,
      message: "",
      loading: true,
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    setProfilePic(e) {
      let file = e.target.files[0] || e.dataTransfer.files[0];

      this.sendProfilePic(file);
    },
    sendProfilePic(file) {
      let fd = new FormData();

      fd.append("photo", file);

      Axios.post(this.$hostname + "/client-avatar", fd, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((response) => {
          this.fetch();
        })
        .catch((error) => {
          console.log("fail", error);
        });
    },
    fetch() {
      Axios.get(this.$hostname + "/client/edit-account", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.account = resp.data.client[0];
          this.email = resp.data.user;
          if (this.account.profile_picture) {
            this.avatar = this.account.profile_picture;
          }
          if (resp.data.client[0].bank_information) {
            this.iban = resp.data.client[0].bank_information.iban;
          } else {
            this.iban = "";
          }
        })
        .catch((err) => {
          this.account = "";
          this.email = "";
        });
      Axios.get(this.$hostname + "/addresses", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.addresses = resp.data.addresses;
        })
        .catch((err) => {
          console.log(err, "can not fetch addresses");
        });
    },

    new_address() {
      let data = {
        city_id: localStorage.city,
        town_id: localStorage.town,
        description: localStorage.description,
        lat: localStorage.lat,
        long: localStorage.long,
      };

      Axios.post(this.$hostname + "/addresses", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((data) => {
          this.add_address = false;
          localStorage.removeItem("city");
          localStorage.removeItem("town");
          localStorage.removeItem("description");
          this.init();
        })
        .catch((err) => {
          console.log(err.message, "درخواست نامعتبر");
        });
    },
    deleteAddress(address_id) {
      Axios.delete(this.$hostname + "/addresses/" + address_id, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.fetch();
        })
        .catch((err) => {
          console.log(err, "درخواست نامعتبر");
        });
    },
    edit_user(val) {
      if (val === 1) {
        let data = {
          first_name: this.account.first_name,
        };
        Axios.patch(this.$hostname + "/client/edit-account", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.message = resp.data.message;
          })
          .catch((err) => {
            console.log(err, "درخواست نامعتبر");
          });
      }
      if (val === 2) {
        let data = {
          last_name: this.account.last_name,
        };
        Axios.patch(this.$hostname + "/client/edit-account", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.message = resp.data.message;
          })
          .catch((err) => {
            console.log(err, "درخواست نامعتبر");
          });
      }
      if (val === 3) {
        let data = {
          birthdate: this.account.birthdate,
        };
        Axios.patch(this.$hostname + "/client/edit-account", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.message = resp.data.message;
          })
          .catch((err) => {
            console.log(err, "درخواست نامعتبر");
          });
      }
      if (val === 4) {
        let data = {
          email: this.email.email,
        };
        Axios.patch(this.$hostname + "/client/edit-account", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.message = resp.data.message;
          })
          .catch((err) => {
            console.log(err, "درخواست نامعتبر");
          });
      }

      if (val === 6) {
        let data = {
          gender: "female",
        };
        Axios.patch(this.$hostname + "/client/edit-account", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.message = resp.data.message;
          })
          .catch((err) => {
            console.log(err, "درخواست نامعتبر");
          });
      }
      if (val === 7) {
        let data = {
          gender: "male",
        };
        Axios.patch(this.$hostname + "/client/edit-account", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.message = resp.data.message;
          })
          .catch((err) => {
            console.log(err, "درخواست نامعتبر");
          });
      }
      if (val === 8) {
        let data = {
          iban: this.iban,
        };
        Axios.patch(this.$hostname + "/client/edit-account", data, {
          headers: {
            Authorization: "Bearer " + eval(localStorage.token),
          },
        })
          .then((resp) => {
            this.message = resp.data.message;
          })
          .catch((err) => {
            console.log(err, "درخواست نامعتبر");
          });
      }
      this.alert = true;
    },
    editable() {
      if (this.edit == false) {
        this.edit = true;
      } else {
        this.edit = false;
      }
    },
    ibandExplorer() {
      if (this.iban.length > 4) {
        switch (this.iban.substring(5, 8)) {
          case "011":
            this.bank = "بانک صنعت و معدن";
            break;
          case "012":
            this.bank = "بانک ملت";
            break;
          case "013":
            this.bank = "بانک رفاه";
            break;
          case "014":
            this.bank = "بانک مسکن";
            break;
          case "015":
            this.bank = "بانک سپه";
            break;
          case "016":
            this.bank = "بانک کشاورزی";
            break;
          case "017":
            this.bank = "بانک ملّی ایران";
            break;
          case "018":
            this.bank = "بانک تجارت";
            break;
          case "019":
            this.bank = "بانک صادرات ایران";
            break;
          case "020":
            this.bank = "بانک توسعه صادرات ایران";
            break;
          case "021":
            this.bank = "پست بانک ایران";
            break;
          case "051":
            this.bank = " موسسه اعتباری توسعه";
            break;
          case "053":
            this.bank = "بانک کارآفرین";
            break;
          case "054":
            this.bank = "بانک پارسیان";
            break;
          case "055":
            this.bank = "بانک اقتصاد نوین";
            break;
          case "056":
            this.bank = "بانک سامان";
            break;
          case "057":
            this.bank = "بانک پاسارگاد";
            break;
          case "058":
            this.bank = "بانک سرمایه";
            break;
          default:
            this.bank = "شماره شبا نامعتبر می باشد";
            break;
        }
      }
    },
  },
};
</script>

<style scoped>
img.loading {
  width: 70px;
  height: 70px;
  margin: 250px auto;
}
.account {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  padding: 50px 100px 44px 100px;
  height: 550px;
  overflow-y: scroll;
}
.account .header {
  display: flex;
  width: 100%;
  justify-content: space-between;
  flex-direction: row-reverse;
}
a {
  text-decoration: none;
  color: #000;
  font-size: 14px;
  cursor: pointer;
}
a:hover {
  text-decoration: underline;
  color: #5c438a;
}
.account .header label {
  border: 2px solid #5c438a17;
  background-image: url("../../../assets/panel/purple/photo.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  border-radius: 60px;
  width: 120px;
  height: 120px;
  cursor: pointer;
  justify-self: flex-end;
  margin: 0 auto;
  transition: 0.4s ease;
}
.account .header label:hover {
  border: 2px solid #5c438aaf;
  background-color: #5c438a17;
  transition: 0.3s ease;
}

.account .details {
  display: flex;
  flex-direction: column;
}
.account .details input {
  outline: none;
  border: none;
  border-bottom: 2px solid #5c438a17;
  margin-top: 10px;
  font-family: IRANsans;
  transition: 0.4s ease;
}
.account .details input:disabled {
  border-bottom: 2px solid #2e224623;
  opacity: 0.5;
  background-color: transparent;
}

.account .details input:focus {
  border-bottom: 2px solid #5c438a;
  transition: 0.4s ease;
}
.account .details label {
  color: #5c438a;
}
.account .details .row-one {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  flex-direction: row;
  margin-top: 50px;
}

.account .details .row-one .first-name {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 28%;
}
.account .details .row-one .last-name {
  display: flex;
  flex-direction: column;
  justify-self: center;
  width: 28%;
}
.account .details .row-one .birthday {
  display: flex;
  flex-direction: column;
  justify-self: end;
  width: 28%;
}

.account .details .row-two {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  flex-direction: row;
  margin-top: 50px;
}
.account .details .row-two .email {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 28%;
}
.account .details .row-two .phone {
  display: flex;
  flex-direction: column;
  justify-self: center;
  width: 28%;
}
.account .details .row-two .gender {
  display: flex;
  flex-direction: column;
  justify-self: end;
  width: 28%;
}
.account .details .row-two .gender .radios {
  display: flex;
  flex-direction: row;
  justify-content: right;
}
.account .details .row-two .gender .radios input {
  appearance: none;
  background-image: url("../../../assets/radio_off.svg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: bottom;
  width: 18px;
  height: 18px;
  margin-top: 5px;
  border: none;
  cursor: pointer;
}

.account .details .row-two .gender label {
  padding-bottom: 1px;
}
.account .details .row-two .gender .radios input:checked {
  background-image: url("../../../assets/radio_on.svg");
}
.account .details .row-two .gender .radios label {
  margin-left: 40px;
  font-size: 16px;
  color: #000;
  cursor: pointer;
}

.account .details .row-three {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  flex-direction: row;
  margin-top: 50px;
}
.row-three .iban {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 64%;
}
.row-three .bank {
  display: flex;
  flex-direction: column;
  justify-self: end;
  width: 28%;
}
.account .address {
  display: flex;
  flex-direction: column;
  margin-top: 50px;
}
.account .address .title {
  display: flex;
  width: 100%;
  justify-content: space-between;
  font-size: 14px;
}
.account .address .title .my-address {
  color: #5c438a;
}

.account .address .addresses {
  display: flex;
  width: 100%;
  justify-content: space-between;
  margin: 10px 0;
  font-size: 14px;
  border-bottom: 2px solid #5c438a17;
  padding-bottom: 5px;
}
.account .address .addresses .delete {
  background-image: url("../../../assets/delete.svg");
  background-repeat: no-repeat;
  background-size: cover;
  width: 18px;
  height: 18px;
}
.account .address .addresses .delete:hover {
  background-image: url("../../../assets/delete_hover.svg");
  cursor: pointer;
}
/* 
* style address modal 
*/
.modal {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgba(92, 67, 138, 0.25); /* Fallback color */
  background-color: rgba(92, 67, 138, 0.25); /* Fallback color */
}
/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  width: 80%; /* Full width */
  height: 930px; /* Full height */
  border-radius: 10px;
  text-align: center;
  font-size: 18px;
  font-weight: 500;
  display: flex;
  justify-content: center;
  flex-direction: column;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
}

.modal-content .content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  padding: 15px;
  min-height: 590px;
}
#addressModal .modal-content {
  width: 60%;
  height: 560px;
}
.buttons {
  display: flex;
  margin: 0 auto;
  justify-content: space-between;
  width: 60%;
}
.buttons button {
  display: flex;
  background-color: #fff;
  border: 2px solid #5c438a;
  margin: 10px 15px;
  width: 35%;
  outline: none;
  cursor: pointer;
  justify-content: center;
  border-radius: 5px;
  color: #5c438a;
  font-size: 18px;
  font-weight: 500;
  transition: 0.4s ease;
  padding: 10px 20px;
  font-family: IRANsans;
}
.buttons button:hover {
  background-color: #5c438a;
  color: #fff;
  transition: 0.4s ease;
}
span.success {
  background-color: #5c438a28;
  color: rgba(0, 0, 0, 0.774);
  border-radius: 5px;
  padding: 10px;
  width: 100%;
  height: 40px;
  margin: 10px 0;
  text-align: center;
  cursor: pointer;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .account {
    padding: 20px 4%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }

  .account .details .row-one,
  .account .details .row-two {
    flex-direction: column;
    margin-top: 0px;
  }

  .account .details .row-one .first-name,
  .account .details .row-one .last-name,
  .account .details .row-one .birthday,
  .account .details .row-two .email,
  .account .details .row-two .phone,
  .account .details .row-two .gender {
    margin-top: 30px;
    width: 90%;
  }

  .account .address .addresses .desc {
    width: 90%;
  }

  #addressModal .modal-content {
    width: 100%;
  }
}
@media screen and (max-width: 540px) {
  .account {
    padding: 20px 4%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }
  .account .details .row-one,
  .account .details .row-two {
    flex-direction: column;
    margin-top: 0px;
  }
  .account .details .row-one .first-name,
  .account .details .row-one .last-name,
  .account .details .row-one .birthday,
  .account .details .row-two .email,
  .account .details .row-two .phone,
  .account .details .row-two .gender {
    margin-top: 30px;
    width: 90%;
  }
  .account .address .addresses .desc {
    width: 90%;
  }
  #addressModal .modal-content {
    width: 100%;
  }
}
</style>
