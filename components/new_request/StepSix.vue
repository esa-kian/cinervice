<template>
  <div>
    <div class="main">
      <div class="title">گزینه مورد نظر خود را انتخاب کنید.</div>
      <div class="plan">
        <label for="vip">
          <input
            type="radio"
            :checked="vip_mode == 1"
            @click="vipMode(1)"
            id="vip"
            name="plan"
          />
          میخواهم سرویس توسط نیروهای متخصص لِمِ کار در اولین فرصت انجام شود.
          (VIP)
        </label>
        <label for="regular">
          <input
            type="radio"
            :checked="vip_mode == 0"
            @click="vipMode(0)"
            id="regular"
            name="plan"
          />
          میخواهم از متخصصین مختلف قیمت دریافت کنم و بهترین را خودم انتخاب کنم.
          (عادی)
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StepSix",
  mounted() {
    this.init();
    if (localStorage.vip) {
      this.$emit("continue_btn", true);
    }
  },
  methods: {
    init() {
      this.vip_mode = parseInt(localStorage.vip);
    },
    vipMode(mode) {
      localStorage.setItem("vip", mode);
      this.$emit("continue_btn", true);
    },
  },
  data() {
    return {
      vip_mode: null,
    };
  },
};
</script>

<style scoped>
.plan {
  width: 103%;
}
label {
  display: flex;
  justify-content: flex-start;
  padding: 13px;
  border-radius: 5px;
  border: solid 2px #5c438a18;
  margin-top: 20px;
  font-size: 14px;
  font-weight: lighter;
  transition: 0.4s ease;
}

input {
  appearance: none;
  background-image: url("../../assets/radio_off.svg");
  background-repeat: no-repeat;
  background-size: cover;
  width: 20px;
  height: 20px;
  outline: none;
  margin: 5px 5px 0 12px;
}
input:checked {
  background-image: url("../../assets/radio_on.svg");
}

label:hover {
  border: solid 2px #5c438a;
  cursor: pointer;
  transition: 0.4s ease;
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
  .plan {
    width: 100%;
  }
}
</style>