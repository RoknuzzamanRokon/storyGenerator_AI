<template>
  <div>
    <header class="transparent-header bg-transparent fixed-top">
      <div class="navbar-default">
        <div class="container lg-container">
          <div class="row align-items-center">
            <div class="col-12 col-lg-12">
              <div class="menu_area alt-font">
                <div class="container">
                  <nav class="navbar navbar-expand-lg navbar-light p-0">
                    <div class="navbar-header navbar-header-custom">
                      <!-- start logo -->
                      <router-link to="/" class="navbar-brand"
                        >
                    <h3>
                        StoryTeller AI
                    </h3>
                    </router-link>
                      <!-- end logo -->
                    </div>

                    <div class="navbar-toggler"></div>

                    <!-- start menu area -->
                    <ul class="navbar-nav ms-auto" id="nav">
                      <li>
                        <router-link to="/" style="color: black"
                          >Home</router-link
                        >
                      </li>
                      <li>
                        <router-link to="/Main" style="color: black"
                          >Create Story</router-link
                        >
                      </li>
                      <li>
                        <router-link to="" style="color: black" href="#!"
                          >Services</router-link
                        >
                      </li>
                      <li>
                        <router-link to="" style="color: black" href="#!"
                          >Elements</router-link
                        >
                      </li>
                    </ul>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>
<style>
@import "../../assets/css/styles.css";
@import "../../assets/css/plugins.css";
@import "../../assets/search/search.css";
@import "../../assets/quform/css/base.css";
</style>
