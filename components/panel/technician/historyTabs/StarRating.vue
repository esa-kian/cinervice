<template>
  <div class="rating">
    <input
      type="radio"
      class="green"
      name="rate"
      id="star-5"
      @click="vote(5)"
    />
    <input
      type="radio"
      class="orange"
      name="rate"
      id="star-4"
      @click="vote(4)"
    />
    <input
      type="radio"
      class="orange"
      name="rate"
      id="star-3"
      @click="vote(3)"
    />
    <input type="radio" class="red" name="rate" id="star-2" @click="vote(2)" />
    <input type="radio" class="red" name="rate" id="star-1" @click="vote(1)" />
  </div>
</template>

<script>
export default {
  name: "StarRating",
  methods: {
    vote(rate) {
      localStorage.setItem("vote", rate);
    },
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.rating {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  width: 40%;
}

.rating input {
  appearance: none;
  background-image: url("../../../../assets/panel/stars/empty.png");
  background-repeat: no-repeat;
  background-size: contain;
  margin: 0;
  width: 30px;
  height: 30px;
  cursor: pointer;
  transition: 0.4s ease;
  outline: none;
}

.red:hover,
.red:hover ~ input,
.red:checked,
.red:checked ~ input {
  background-image: url("../../../../assets/panel/stars/red.png");
  transition: 0.4s ease;
}
.orange:hover,
.orange:hover ~ input,
.orange:checked,
.orange:checked ~ input {
  background-image: url("../../../../assets/panel/stars/orange.png");
  transition: 0.4s ease;
}
.green:hover,
.green:hover ~ input,
.green:checked,
.green:checked ~ input {
  background-image: url("../../../../assets/panel/stars/green.png");
  transition: 0.4s ease;
}
</style>
