<template>
  <div>
    <header>
      <nav class="navigation">
        <ul class="nav__right">
          <li class="logo"><a href="#"></a></li>
          <li>
            <a href="#">
              خانه و سلامت
              <i class="dropdown-icon"></i
            ></a>
          </li>
          <li>
            <a href="#"> سلامت و پزشکی<i class="dropdown-icon"></i></a>
          </li>
          <li>
            <a href="#"> مد و زیبایی<i class="dropdown-icon"></i></a>
          </li>
        </ul>
        <ul class="nav__left">
          <form class="search" action="#">
            <div class="form-group">
              <input type="text" placeholder="جستجو در مطالب بلاگ…" />
              <button type="submit">
                <i class="search"></i>
              </button>
            </div>
          </form>
        </ul>
      </nav>
    </header>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {};
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
}

ul {
  margin: 0px;
}

.navigation {
  background-color: #fff;
  display: flex;
  justify-content: space-between;
  position: fixed;
  z-index: 999;
  width: 100%;
}

.navigation .logo {
  background-image: url("../../assets/logo.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  height: 30px;
  width: 120px;
  margin-top: 15px;
}

.navigation a {
  color: #000;
}

.navigation a:hover {
  opacity: 0.8;
}

.navigation .nav__right,
.navigation .nav__left {
  display: flex;
}

.navigation .nav__right li,
.navigation .nav__left li {
  list-style: none;
  padding: 19px 0px;
  margin-left: 44px;
  font-size: 14px;
}
.navigation .nav__right li.logo {
  margin-right: 126px;
}
.dropdown-icon {
  background-image: url("../../assets/Blog/arrow_down.svg");
  background-repeat: round;
  display: inline-flex;
  width: 7px;
  height: 5px;
  margin-right: 9px;
}

/*
 *    Search Box
 */

.navigation .nav__left {
  margin-left: 12%;
  padding-top: 8px;
  padding-right: 0px;
}

.search .form-group {
  margin-right: 20px;
  display: flex;
  border-bottom: 1px solid #5c438a;
}

.search input {
  border: none;
  outline: none;
  padding: 12px;
  width: 350px;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px;
  opacity: 0.5;
}

.search button {
  border: none;
  outline: none;
  background-color: transparent;
}

.search button i {
  background-image: url("../../assets/Blog/search.svg");
  background-repeat: no-repeat;
  display: inline-flex;
  padding: 10px;
}
</style>