<script setup>
import Button from "./StickyModal.vue";
</script>
<template>
  <div>
    <section class="pt-0">
      <div class="container">
        <div class="w-md-75 w-lg-50 text-center mx-md-auto mb-6">
          <h2 class="line-title">Discover and Create</h2>
        </div>
        <div class="row mt-n1-9">
          <div class="col-md-3 mt-1-9">
            <div class="card orange">
              <div class="card-body text-center">
                <h3 class="h5">Mystrey</h3>
                <p>
                  We provide quick and detailed answers for your awesome
                  business.
                </p>
                <button class="btn btn-outline-success">
                  read more<i class="ti-arrow-right align-middle ms-2"></i>
                </button>
              </div>
            </div>
          </div>

          <div class="col-md-3 mt-1-9">
            <div class="card orange">
              <div class="card-body text-center">
                <h3 class="h5">Adventure</h3>
                <p>
                  We provide quick and detailed answers for your awesome
                  business.
                </p>
                <button class="btn btn-outline-success">
                  read more<i class="ti-arrow-right align-middle ms-2"></i>
                </button>
              </div>
            </div>
          </div>

          <div class="col-md-3 mt-1-9">
            <div class="card orange">
              <div class="card-body text-center">
                <h3 class="h5">Sci-Fi</h3>
                <p>
                  We provide quick and detailed answers for your awesome
                  business.
                </p>
                <button @click="showModal" class="btn btn-outline-success">
                  Generate Story<i class="ti-arrow-right align-middle ms-2"></i>
                </button>
              </div>
            </div>
          </div>

          <div class="col-md-3 mt-1-9">
            <div class="card orange">
              <div class="card-body text-center">
                <h3 class="h5">Educational</h3>
                <p>
                  We provide quick and detailed answers for your awesome
                  business.
                </p>
                <button class="btn btn-outline-success">
                  read more<i class="ti-arrow-right align-middle ms-2"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <Button />
</template>
