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
              v-model="email"
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
          <div class="national-id">
            <label for="national_id">کد ملی</label>
            <input
              type="text"
              name="national_id"
              id="national_id"
              v-model="account.national_id"
              :disabled="edit == false"
            />
          </div>
        </div>
        <div class="row-three">
          <div class="phone">
            <label for="phone">شماره ثابت</label>
            <input
              type="text"
              name="phone"
              id="phone"
              v-model="account.telephone"
              :disabled="edit == false"
            />
          </div>
          <div class="address">
            <label for="address">آدرس</label>
            <input
              type="text"
              name="address"
              id="address"
              v-model="account.address"
              :disabled="edit == false"
            />
          </div>
        </div>
        <div class="row-four">
          <div class="gender">
            <label for="gender">جنسیت</label>
            <div class="radios">
              <input
                type="radio"
                name="gender"
                id="female"
                value="female"
                v-model="account.gender"
                :checked="account.gender == 'female'"
                :disabled="edit == false"
              />
              <label for="female"> زن </label>
              <input
                type="radio"
                name="gender"
                value="male"
                v-model="account.gender"
                :checked="account.gender == 'male'"
                id="male"
                :disabled="edit == false"
              />
              <label for="male"> مرد </label>
            </div>
          </div>
          <div class="skill">
            <label for="skill" class="check-icon">
              لطفا مهارت‌ های خود را انتخاب نمایید.
            </label>
            <input type="checkbox" name="skill" id="skill" />
            <div id="skill-dropdwon" class="dropdown-content">
              <div
                class="skill-opt"
                v-for="skill in skills"
                :key="skill.skill_id"
              >
                <label :for="'skill' + skill.id">
                  {{ skill.title }}

                  <input
                    @click="setSkills(skill.id)"
                    type="checkbox"
                    :name="skill.title"
                    :id="'skill' + skill.id"
                    :disabled="edit == false"
                    :checked="selected_skills.includes(skill.id)"
                /></label>
              </div>
            </div>
          </div>
        </div>
        <div class="row-five">
          <div class="iban">
            <label for="iban">شماره شبا</label>

            <input
              type="text"
              name="iban"
              id="iban"
              v-model="iban"
              @input="ibandExplorer"
              :disabled="edit == false"
            />
          </div>

          <div class="bank">
            <label for="bank">بانک</label>
            <input v-model="bank" type="text" name="bank" id="bank" disabled />
          </div>
        </div>
        <div class="photo-auth">
          <div class="caption">
            جهت تکمیل فرآیند ثبت‌نام، تصویری از خود در حال نگهداری کارت ملی خود
            بارگزاری نمایید.
          </div>
          <div class="upload">
            <div class="btn-upload">
              <label for="national-card"></label>
              <input
                @change="sendNationalCard"
                type="file"
                id="national-card"
                hidden
                :disabled="edit == false"
              />
              <span>بارگذاری تصویر</span>

              <img
                v-if="national_card"
                :src="national_card"
                width="300px"
                height="150px"
                alt=""
              />
            </div>
            <div class="guide"></div>
          </div>
        </div>
        <button @click="submit">ثبت و ارسال اطلاعات</button>
      </div>
    </div>
    <div v-else>
      <img class="loading" src="../../../assets/loading_t.svg" alt="loading" />
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "Account",
  mounted() {
    this.init();
  },
  methods: {
    fetchSkills(proficiency_id) {
      Axios.get(this.$hostname + "/proficiencies/" + proficiency_id + "/skills")
        .then((resp) => {
          this.skills = resp.data.skills;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    init() {
      Axios.get(this.$hostname + "/technician/edit-account", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.loading = false;
          this.account = resp.data.technician[0];
          if (this.account.profile_picture) {
            this.avatar = this.account.profile_picture;
          }
          if (this.account.national_card_picture) {
            this.national_card = this.account.national_card_picture;
          }
          this.email = resp.data.user.email;

          resp.data.skills.forEach((element) => {
            this.selected_skills.push(element.skill_id);
          });

          this.fetchSkills(resp.data.technician[0].proficiency_id);

          if (resp.data.technician[0].iban) {
            this.iban = resp.data.technician[0].iban;
          } else {
            this.iban = "";
          }
          this.ibandExplorer();
        })
        .catch((err) => {
          this.account = "";
          this.email = "";
          this.iban = "";
          console.log(err, "can not fetch account data");
        });
    },
    setSkills(skill) {
      const index = this.selected_skills.indexOf(skill);
      if (index > -1) {
        this.selected_skills.splice(index, 1);
      } else {
        this.selected_skills.push(skill);
      }
    },
    setProfilePic(e) {
      let file = e.target.files[0] || e.dataTransfer.files[0];

      this.sendProfilePic(file);
    },
    sendProfilePic(file) {
      let fd = new FormData();

      fd.append("photo", file);

      Axios.post(this.$hostname + "/technician-avatar", fd, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((response) => {
          this.init();
        })
        .catch((error) => {
          console.log("fail", error);
        });
    },
    sendNationalCard(e) {
      let file = e.target.files[0] || e.dataTransfer.files[0];

      let fd = new FormData();

      fd.append("national_card", file);

      Axios.post(this.$hostname + "/national-card", fd, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then(function (response) {
          this.national_card = response.data.message[0].national_card_picture;
        })
        .catch(function (error) {
          console.log("fail", error);
        });
    },
    submit() {
      let data = {
        first_name: this.account.first_name,
        last_name: this.account.last_name,
        birthdate: this.account.birthdate,
        email: this.email,
        gender: this.account.gender,
        phone_number: this.account.phone_number,
        national_id: this.account.national_id,
        telephone: this.account.telephone,
        address: this.account.address,
        iban: this.iban,
        skills: JSON.stringify(this.selected_skills),
      };

      Axios.post(this.$hostname + "/technician/edit-account", data, {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.edit = false;
          this.alert = true;
          this.message = resp.data.message;
        })
        .catch((err) => {
          console.log(err, "درخواست نامعتبر");
        });
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
  data() {
    return {
      edit: false,
      message: "",
      alert: false,
      account: null,
      email: null,
      iban: null,
      avatar: null,
      national_card: null,
      bank: "",
      image: [],
      skills: [],
      selected_skills: [],
      loading: true,
    };
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
  color: #7ab383;
}

.account .header label {
  border: 2px solid rgba(122, 179, 131, 0.15);
  background-image: url("../../../assets/panel/green/photo.svg");
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
  border: 2px solid rgba(122, 179, 131, 0.637);
  background-color: rgba(122, 179, 131, 0.068);
  transition: 0.3s ease;
}
.account .details {
  display: flex;
  flex-direction: column;
}
.account .details input {
  outline: none;
  border: none;
  border-bottom: 2px solid #7ab38317;
  margin-top: 10px;
  font-family: IRANsans;
  transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.account .details input:disabled {
  border-bottom: 2px solid #2f443217;
  background-color: transparent;
  opacity: 0.5;
}
.account .details input:focus {
  border-bottom: 2px solid #7ab383;
  transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.account .details label {
  color: #7ab383;
}
.row-one,
.row-two,
.row-three,
.row-four,
.row-five,
.photo-auth {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: baseline;
  flex-direction: row;
  margin-top: 50px;
}

.row-one div,
.row-two div {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 28%;
}

.row-three .phone {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 28%;
}
.row-three .address {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 64%;
}
.row-four .gender {
  display: flex;
  flex-direction: column;
  justify-self: end;
  width: 28%;
}
.row-four .gender .radios {
  display: flex;
  flex-direction: row;
  justify-content: right;
}
.row-four .gender .radios input {
  appearance: none;
  background-image: url("../../../assets/panel/green/radio_off.svg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: bottom;
  width: 18px;
  height: 18px;
  margin-top: 5px;
  border: none;
  cursor: pointer;
}
.row-four .gender label {
  padding-bottom: 1px;
}
.row-four .gender .radios input:checked {
  background-image: url("../../../assets/panel/green/radio_on.svg");
}
.row-four .gender .radios label {
  margin-left: 40px;
  font-size: 16px;
  color: #000;
  cursor: pointer;
}

.row-four .skill {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 64%;
}
.row-four label.check-icon {
  background-image: url("../../../assets/panel/green/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-y: center;
  width: 100%;
  cursor: pointer;
  margin: 0;
}
.row-four .dropdown-content {
  display: none;
  position: sticky;
  background-color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  border: solid 1px #e6e6e6;
  z-index: 999;
}
.dropdown-content label {
  height: 45px;
  width: 100%;
  padding: 10px 20px;
  margin-bottom: 0;
  font-size: 0.9rem;
}
.dropdown-content label:hover {
  background-color: #7ab3831f;
  color: #7ab383;
  cursor: pointer;
  width: 100%;
}
.dropdown-content input {
  appearance: none;
}
.skill-opt {
  height: 45px;
  width: 100%;
}

.skill .dropdown-content input {
  background-image: url("../../../assets/panel/green/unchecked.svg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: unset;
  width: 15px;
  height: 15px;
  margin: 12px 10px 0px 0px;
  outline: none;
  transition: 0.4s ease;
  cursor: pointer;
}
.skill .dropdown-content input:checked {
  background-image: url("../../../assets/panel/green/checked.svg");
  transition: 0.4s ease;
}
input#skill {
  appearance: none;
}
input#skill:checked ~ .dropdown-content {
  display: flex;
  flex-direction: column;
  padding: 0;
  width: 100%;
}

.row-five .iban {
  display: flex;
  flex-direction: column;
  justify-self: start;
  width: 64%;
}
.row-five .bank {
  display: flex;
  flex-direction: column;
  justify-self: end;
  width: 28%;
}
.photo-auth {
  display: flex;
  width: 100%;
  justify-content: space-between;
  flex-direction: column;
}
.upload {
  margin: auto;
  display: flex;
  justify-content: space-between;
  width: 75%;
  margin-top: 50px;
}
.btn-upload {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 14px;
  font-weight: 500;
  color: #000;
}
.btn-upload label {
  border: 2px dashed rgba(122, 179, 131, 0.192);
  background-image: url("../../../assets/plus_green.svg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 70px;
  width: 130px;
  height: 130px;
  cursor: pointer;
  display: inline-block;
  margin: 0 auto;
  margin-bottom: 10px;
  transition: 0.4s ease;
}
.btn-upload label:hover {
  border: 2px solid rgba(122, 179, 131, 0.637);
  border-radius: 10px;
  background-color: rgba(122, 179, 131, 0.068);
  transition: 0.3s ease;
}
.guide {
  background-image: url("../../../assets/panel/ath.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  width: 65%;
  height: 130px;
}
button {
  opacity: 0.5;
  border-radius: 5px;
  font-family: IRANsans;
  font-size: 14px;
  background-color: #7ab383;
  border: none;
  width: 30%;
  color: #fff;
  cursor: pointer;
  height: 45px;
  margin: 45px auto 0 auto;
  transition: 0.4s ease;
}
button:hover {
  opacity: 1;
  transition: 0.4s ease;
}
span.success {
  background-color: #7ab38328;
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
  .account .details .row-two,
  .account .details .row-three,
  .account .details .row-four,
  .account .details .row-five {
    flex-direction: column;
    margin-top: 0px;
  }
  .account .details div div {
    margin-top: 30px;
    width: 90%;
  }
  .caption {
    margin-top: 0 !important;
  }
  .upload {
    margin-top: 0 !important;
    flex-direction: column;
  }
  .guide {
    margin-top: 0 !important;
  }
  button {
    margin-top: 10px !important;
    width: 80%;
  }
  .skill-opt {
    margin-top: 5px !important;
  }
  input#skill:checked ~ .dropdown-content {
    margin-top: 5px !important;
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
  .account .details .row-two,
  .account .details .row-three,
  .account .details .row-four,
  .account .details .row-five {
    flex-direction: column;
    margin-top: 0px;
  }
  .account .details div div {
    margin-top: 30px;
    width: 90%;
  }
  .caption {
    margin-top: 0 !important;
  }
  .upload {
    margin-top: 0 !important;
    flex-direction: column;
  }
  .guide {
    margin-top: 0 !important;
  }
  button {
    margin-top: 10px !important;
    width: 80%;
  }
  .skill-opt {
    margin-top: 5px !important;
  }
  input#skill:checked ~ .dropdown-content {
    margin-top: 5px !important;
  }
}
</style>
