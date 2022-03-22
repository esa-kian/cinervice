<template>
  <div class="orders">
    <div class="tabs">
      <div
        :class="{ active: isActive(1), current: !isActive(1) }"
        @click="setActive(1)"
      >
        درخواست‌های جاری
      </div>
      <div
        :class="{ active: isActive(2), done: !isActive(2) }"
        @click="setActive(2)"
      >
        درخواست‌های انجام شده
      </div>
      <div
        :class="{ active: isActive(3), canceled: !isActive(3) }"
        @click="setActive(3)"
      >
        درخواست‌های لغو/منقضی شده
      </div>
    </div>
    <div class="content">
      <div v-if="isActive(1)">
        <CurrentTab />
      </div>
      <div v-if="isActive(2)">
        <DoneTab />
      </div>
      <div v-if="isActive(3)">
        <CanceledTab />
      </div>
    </div>
  </div>
</template>

<script>
import CurrentTab from "./orderTabs/CurrentTab";
import DoneTab from "./orderTabs/DoneTab";
import CanceledTab from "./orderTabs/CanceledTab";

export default {
  name: "MyOrders",
  components: {
    CurrentTab,
    DoneTab,
    CanceledTab,
  },
  methods: {
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
    };
  },
};
</script>

<style scoped>
.orders {
  display: flex;
  flex-direction: column;
  padding: 70px 102px;
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
  color: #5c438a;
  border-bottom: 4px solid #5c438a;
  border-radius: 4px;
  font-weight: bold;
}

.orders .tabs .current,
.orders .tabs .done,
.orders .tabs .canceled {
  display: flex;
  cursor: pointer;
  width: 100%;
  align-items: center;
  justify-content: center;
  padding-bottom: 15px;
  border-bottom: 2px solid #5c438a17;
}
@media screen and (min-width: 540px) and (max-width: 768px) {
  .orders {
    padding: 20px 4%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }
  .tabs {
    text-align: center;
    font-size: 0.7rem;
  }
}
@media screen and (max-width: 540px) {
  .orders {
    padding: 20px 4%;
    max-height: 470px;
    height: 700px;
    position: relative;
    overflow-y: scroll;
  }
  .tabs {
    text-align: center;
    font-size: 0.7rem;
  }
}
</style>
