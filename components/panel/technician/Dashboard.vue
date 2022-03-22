<template>
  <div class="dashboard">
    <div class="tabs">
      <div
        :class="{ active: isActive(1), current: !isActive(1) }"
        @click="setActive(1)"
      >
        نمودار هفتگی
      </div>
      <div
        :class="{ active: isActive(2), done: !isActive(2) }"
        @click="setActive(2)"
      >
        نمودار ماهانه
      </div>
      <div
        :class="{ active: isActive(3), canceled: !isActive(3) }"
        @click="setActive(3)"
      >
        نمودار سالانه
      </div>
    </div>
    <div v-if="!loading" class="content">
      <div v-if="isActive(1)">
        <WeeklyTab />
        <div class="statistics">
          <div class="total-income">
            <div class="caption">مجموع درآمد این هفته تا کنون:</div>
            <div class="value">{{ weeklyTotal }} تومان</div>
          </div>
          <div class="total-done">
            <div class="caption">درخواست های انجام شده در این هفته:</div>
            <div class="value">{{ weeklyCount }} درخواست</div>
          </div>
        </div>
      </div>
      <div v-if="isActive(2)">
        <MonthlyTab />
        <div class="statistics">
          <div class="total-income">
            <div class="caption">مجموع درآمد این ماه تا کنون:</div>
            <div class="value">{{ monthlyTotal }} تومان</div>
          </div>
          <div class="total-done">
            <div class="caption">درخواست های انجام شده در این ماه:</div>
            <div class="value">{{ monthlyCount }} درخواست</div>
          </div>
        </div>
      </div>
      <div v-if="isActive(3)">
        <AnnualTab />
        <div class="statistics">
          <div class="total-income">
            <div class="caption">مجموع درآمد این سال تا کنون:</div>
            <div class="value">{{ yearlyTotal }} تومان</div>
          </div>
          <div class="total-done">
            <div class="caption">درخواست های انجام شده در این سال:</div>
            <div class="value">{{ yearlyCount }} درخواست</div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <img class="loading" src="../../../assets/loading_t.svg" alt="loading" />
    </div>
  </div>
</template>

<script>
import WeeklyTab from "./dashboardTabs/WeeklyTab";
import MonthlyTab from "./dashboardTabs/MonthlyTab";
import AnnualTab from "./dashboardTabs/AnnualTab";
import Axios from "axios";

export default {
  name: "MyOrders",
  components: {
    WeeklyTab,
    MonthlyTab,
    AnnualTab,
  },
  mounted() {
    this.fetchTotalIncome();
  },
  methods: {
    fetchTotalIncome() {
      Axios.get(this.$hostname + "/total-income", {
        headers: {
          Authorization: "Bearer " + eval(localStorage.token),
        },
      })
        .then((resp) => {
          this.weeklyTotal = resp.data.weekly.total;
          this.weeklyCount = resp.data.weekly.count;
          this.monthlyTotal = resp.data.monthly.total;
          this.monthlyCount = resp.data.monthly.count;
          this.yearlyTotal = resp.data.yearly.total;
          this.yearlyCount = resp.data.yearly.count;
          this.loading = false;
        })
        .catch((err) => {});
    },
    setActive(x) {
      this.activeTab = x;
    },
    isActive(x) {
      return this.activeTab === x;
    },
  },
  data() {
    return {
      activeTab: 1,
      weeklyTotal: null,
      weeklyCount: null,
      monthlyTotal: null,
      monthlyCount: null,
      yearlyTotal: null,
      yearlyCount: null,
      loading: true,
    };
  },
};
</script>

<style scoped>
img.loading {
  width: 70px;
  height: 70px;
  margin: 150px auto;
}
.dashboard {
  display: flex;
  flex-direction: column;
  padding: 30px 102px;
  height: 550px;
  overflow-y: scroll;
}
.tabs {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  justify-items: center;
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 30px;
}

.active {
  display: flex;
  cursor: pointer;
  width: 100%;
  align-items: center;
  justify-content: center;
  padding-bottom: 15px;
  color: #7ab383;
  border-bottom: 4px solid #7ab383;
  border-radius: 4px;
  font-weight: bold;
}

.dashboard .tabs .current,
.dashboard .tabs .done,
.dashboard .tabs .canceled {
  display: flex;
  cursor: pointer;
  width: 100%;
  align-items: center;
  justify-content: center;
  padding-bottom: 15px;
  border-bottom: 2px solid #7ab38317;
}
.statistics {
  display: flex;
  justify-content: space-between;
}
.total-income,
.total-done {
  display: flex;
  justify-content: space-between;
  width: 48%;
  padding: 20px 10px;
  margin-top: 45px;
  border-radius: 10px;
  box-shadow: 0 0 10px 1px rgba(122, 179, 131, 0.15);
  font-size: 0.9rem;
}
.value {
  font-size: 0.8rem;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .dashboard {
    padding: 15px 3%;
  }
}
@media screen and (max-width: 540px) {
  .dashboard {
    padding: 20px 4%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }
  .tabs {
    text-align: center;
    font-size: 0.8rem;
  }
  .statistics {
    flex-direction: column;
  }
  .total-income,
  .total-done {
    flex-direction: column;
    width: 100%;
  }
}
</style>
