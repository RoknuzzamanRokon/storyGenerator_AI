<style>
@import "../../assets/vendor/bootstrap/css/bootstrap.min.css";
@import "../../assets/vendor/bootstrap-icons/bootstrap-icons.css";
@import "../../assets/vendor/boxicons/css/boxicons.min.css";
@import "../../assets/vendor/quill/quill.snow.css";
@import "../../assets/vendor/quill/quill.bubble.css";
@import "../../assets/vendor/remixicon/remixicon.css";
@import "../../assets/vendor/simple-datatables/style.css";
@import "../../assets/css/style.css";
</style>
<template>
  <main>
    <div class="container">
      <section
        class="section register min-vh-100 d-flex flex-column align-items-center justify-content-center py-4"
      >
        <div class="container">
          <div class="row justify-content-center">
            <div
              class="col-lg-4 col-md-6 d-flex flex-column align-items-center justify-content-center"
            >
              <!-- End Logo -->

              <div class="card mb-3">
                <div class="card-body">
                  <div class="pt-4 pb-2">
                    <h5 class="card-title text-center pb-0 fs-4">
                      Login to Your Account
                    </h5>
                    <p class="text-center small">
                      Enter your username & password to login
                    </p>
                  </div>

                  <div class="row g-3">
                    <div class="col-12">
                      <label for="yourUsername" class="form-label"
                        >E-Mail</label
                      >
                      <div class="input-group has-validation">
                        <span class="input-group-text" id="inputGroupPrepend"
                          >@</span
                        >
                        <input
                          type="email"
                          class="form-control"
                          v-model="email"
                          required
                        />
                        <div class="invalid-feedback">
                          Please enter your email.
                        </div>
                      </div>
                    </div>

                    <div class="col-12">
                      <label for="yourPassword" class="form-label"
                        >Password</label
                      >
                      <input
                        type="password"
                        v-model="password"
                        class="form-control"
                        required
                      />
                      <div class="invalid-feedback">
                        Please enter your password!
                      </div>
                    </div>

                    <div class="col-12">
                      <div class="form-check">
                        <input
                          class="form-check-input"
                          type="checkbox"
                          name="remember"
                          value="true"
                          id="rememberMe"
                        />
                        <label class="form-check-label" for="rememberMe"
                          >Remember me</label
                        >
                      </div>
                    </div>
                    <div class="col-12">
                      <button
                        @click="login"
                        class="btn btn-primary w-100"
                        type="submit"
                      >
                        Login
                      </button>
                    </div>
                    <div class="col-12">
                      <p class="small mb-0">
                        Don't have account?
                        <router-link to="/Register"
                          >Create an account</router-link
                        >
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </main>
  <!-- End #main -->
</template>
<script>
import axios from "axios";
import Swal from "sweetalert2";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("http://localhost:5000/login", {
          email: this.email,
          password: this.password,
        });

        // Successful login
        if (response.data.access_token) {
          localStorage.setItem("token", response.data.access_token); // Save token to local storage
          this.showSuccess("Logged in successfully!", () => {
            this.$router.push('/Admin');
          });
        } else {
          this.showError("Login failed. Please try again.");
        }
      } catch (error) {
        this.showError("There was an error during login.");
        console.error("There was an error:", error.response);
      }
    },
    showSuccess(message, callback) {
      Swal.fire({
        position: "top-end",
        icon: "success",
        title: message,
        showConfirmButton: false,
        timer: 1500,
        onClose: callback,
      });
    },
    showError(message) {
      Swal.fire({
        position: "top-end",
        icon: "error",
        title: message,
        showConfirmButton: true,
      });
    },
  },
};
</script>
