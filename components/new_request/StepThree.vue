<template>
  <div>
    <div class="main">
      <div class="date">
        روز و ساعت مورد نظر برای انجام سرویس را تعیین کنید.
      </div>
      <date-picker
        color="#5c438a"
        :style="{
          width: '100%',
          border: '2px solid #5c438a53',
          'border-radius': '5px',
          'margin-top': '20px',
        }"
        display-format=" jYYYY   jMMMM   jD   HH:mm:ss "
        format="YYYY-MM-DD HH:mm:ss"
        v-model="datetime"
        type="datetime"
        @change="setDatetime"
      />

      <div class="budget">
        <div class="title">بودجه مد نظر خود را وارد نمایید.</div>
        <div class="budget-input">
          <label for="budget">تومان</label>
          <input
            @input="setBudget"
            type="text"
            name="budget"
            v-model="budget"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StepThree",
  components: {
    DatePicker: VuePersianDatetimePicker,
  },
  mounted() {
    this.init();
  },
  methods: {
    init() {
      this.datetime = localStorage.datetime;
      this.budget = localStorage.budget;
      if (localStorage.datetime && localStorage.budget) {
        this.$emit("continue_btn", true);
      }
    },
    setDatetime() {
      localStorage.setItem("datetime", this.datetime);
      if (localStorage.datetime && localStorage.budget) {
        this.$emit("continue_btn", true);
      }
    },
    setBudget() {
      localStorage.setItem("budget", this.budget);
      if (localStorage.datetime && localStorage.budget) {
        this.$emit("continue_btn", true);
      }
    },
  },
  data() {
    return {
      datetime: "",
      budget: null,
    };
  },
};
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
}
.main .date {
  font-size: 16px;
  font-weight: 500;
  color: #162133;
}

.budget {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}
.title {
  display: flex;
}

.budget-input {
  display: flex;
  opacity: 0.8;
  align-items: center;
  border-radius: 5px;
  border: solid 2px #5c438a23;
  height: 44px;
  padding: 10px;
}

.budget-input input {
  font-size: 16px;
  outline: none;
  border: none;
  text-align: left;
  font-family: IRANsans;
}

@media screen and (max-width: 540px) {
  .budget {
    flex-direction: column;
  }
}
</style>