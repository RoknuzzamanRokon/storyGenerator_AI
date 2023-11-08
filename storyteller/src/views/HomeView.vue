<script setup>
import Header from "../components/Header/Nav.vue";
import Banner from "../components/Main/Banner.vue";
import Core from "../components/Main/Core.vue";
import About from "../components/Main/About.vue";
import Contact from "../components/Main/Contact.vue";
import Team from "../components/Main/Team.vue";
</script>
<template>
  <div>
    <div class="main-wrapper">

      <Header />
      <!-- Banner -->
      <Banner />
      <!-- SERVICES -->
      <Core />
      <!-- ABOUT -->
      <About />
      <!-- TEAM -->
      <Team />
      <!-- CONTACT -->
      <Contact />
    </div>
  </div>
</template>
