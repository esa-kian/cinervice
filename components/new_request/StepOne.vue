<template>
  <div>
    <div class="main">
      <div class="title">دسته بندی درخواست</div>

      <img
        v-if="loading"
        class="loading"
        src="../../assets/loading.svg"
        alt="loading"
      />

      <select
        v-else
        @change="setProficiency"
        name="cats"
        class="cats"
        id="cats"
        v-model="proficiency"
      >
        <option
          v-for="proficiency in proficiencies"
          :key="proficiency.id"
          :value="proficiency.id"
        >
          {{ proficiency.title }}
        </option>
      </select>
      <div class="title">
        جزئیات درخواست یا هر موردی که متخصص نیاز است بداند را توضیح دهید.
      </div>
      <textarea
        @input="setDetails"
        name="details"
        id="details"
        v-model="details"
      ></textarea>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "StepOne",
  mounted() {
    this.fetchProficiencies();
    if (localStorage.proficiency && localStorage.details) {
      this.$emit("continue_btn", true);
    }
  },
  methods: {
    fetchProficiencies() {
      this.details = localStorage.details;
      Axios.get(this.$hostname + "/proficiencies")
        .then((resp) => {
          this.proficiencies = resp.data.proficiencies;
          this.loading = false;
        })
        .catch((err) => {
          console.log(err, "can not fetch proficiencies");
        });
    },
    setProficiency() {
      localStorage.setItem("proficiency", this.proficiency);
      let p = document.getElementById("cats");
      let proficiency_title = p.options[p.selectedIndex].text;
      localStorage.setItem("proficiency_title", proficiency_title);
    },
    setDetails() {
      localStorage.setItem("details", this.details);
      if (localStorage.proficiency && localStorage.details) {
        this.$emit("continue_btn", true);
      }
    },
  },
  data() {
    return {
      proficiencies: null,
      proficiency: localStorage.proficiency,
      details: null,
      loading: true,
    };
  },
};
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.main .title {
  font-size: 16px;
  font-weight: 500;
  width: 100%;
}

img.loading {
  width: 40px;
  height: 40px;
  margin: 0 auto;
}
select {
  background-image: url("../../assets/FAQ/arrow_down.svg");
  background-repeat: no-repeat;
  background-position-x: 15px;
  background-position-y: 15px;
  background-size: 15px;
  width: 500px;
  outline: none;
  appearance: none;
  border: solid 2px #5c438a70;
  background-color: #fff;
  border-radius: 5px;
  height: 44px;
  font-size: 14px;
  font-weight: 500;
  margin-top: 10px;
  margin-bottom: 20px;
  font-family: IRANSans;
  padding-right: 10px;
  width: 100%;
  transition: 0.3s ease;
}
select:hover {
  border: solid 2px #5c438a;
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.15);
  transition: 0.3s ease;
}
select option {
  background: #5c438a0a;
  color: #5c438a;
}
textarea {
  padding: 10px 10px;
  border-radius: 5px;
  font-family: IRANSans;
  outline: none;
  border: solid 2px #61488f2a;
  margin: 10px 0;
  width: 100%;
  height: 135px;
  resize: none;
}
textarea:hover {
  box-shadow: 0 0 10px 1px rgba(92, 67, 138, 0.055);
}
@media screen and (max-width: 540px) {
  .main {
    width: 100%;
  }
}
</style>