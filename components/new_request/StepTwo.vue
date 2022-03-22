<template>
  <div>
    <div class="main">
      <div class="title">نوع مهارت‌های مورد نیاز را مشخص کنید.</div>
      <img
        v-if="loading"
        class="loading"
        src="../../assets/loading.svg"
        alt="loading"
      />
      <div v-else-if="skills.length === 0">
        <i> مهارتی برای این تخصص یافت نشد</i>
      </div>
      <div v-else>
        <div v-for="skill in skills" :key="skill.id" class="skill">
          <input
            @click="setSkills(skill.id, skill.title)"
            :checked="checked_skills.includes(skill.id)"
            :name="'skill_' + skill.id"
            type="checkbox"
            :id="skill.id"
          />
          <label for="skill">{{ skill.title }}</label>
          <label for="skill_1" id="skill"></label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from "axios";

export default {
  name: "StepTwo",
  mounted() {
    this.fetchSkills();
  },
  methods: {
    fetchSkills() {
      Axios.get(
        this.$hostname +
          "/proficiencies/" +
          localStorage.proficiency +
          "/skills"
      )
        .then((resp) => {
          this.skills = resp.data.skills;
          
          if (localStorage.skills) {
            this.checked_skills = localStorage.skills;
          }
          this.loading = false;
        })
        .catch((err) => {
          console.log(err, "can not fetch skills");
        });
    },
    setSkills(skill, title) {
      let skills_local = [];
      const index = this.selected_skills.indexOf(skill);
      if (index > -1) {
        this.selected_skills.splice(index, 1);
        this.skills_title.splice(index, 1);
        skills_local.splice(index, 1);
      } else {
        this.selected_skills.push(skill);
        skills_local.push(skill);
        this.skills_title.push(title);
      }

      localStorage.setItem("skills", this.selected_skills);
      localStorage.setItem("skill_title", this.skills_title);
    },
  },
  data() {
    return {
      skills: null,
      selected_skills: [],
      skills_title: [],
      checked_skills: [],
      loading: true,
    };
  },
};
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
}
.main .title {
  font-size: 16px;
  font-weight: 500;
  margin-bottom: 21px;
}
.main .skill {
  font-size: 14px;
  font-weight: 500;
  margin: 7px 0;
  opacity: 0.8;
  color: #162133;
  display: flex;
}

img.loading {
  width: 40px;
  height: 40px;
}
div.skill input {
  appearance: none;
  background-image: url("../../assets/unchecked.svg");
  background-repeat: no-repeat;
  background-size: cover;
  width: 18px;
  height: 18px;
  outline: none;
  margin: 0 0 0 12px;
  transition: 0.4s ease;
}

div.skill input:checked {
  background-image: url("../../assets/checked.svg");
  transition: 0.4s ease;
}

@media screen and (max-width: 500px) {
}
</style>