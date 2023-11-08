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
              <div class="card mb-3">
                <div class="card-body">
                  <div class="pt-4 pb-2">
                    <h5 class="card-title text-center pb-0 fs-4">
                      Create an Account
                    </h5>
                    <p class="text-center small">
                      Enter your personal details to create account
                    </p>
                    <div v-if="error" class="error">{{ error }}</div>
                  </div>

                  <form
                    @submit.prevent="register"
                    class="row g-3 needs-validation"
                    novalidate
                  >
                    <div class="col-12">
                      <label for="yourName" class="form-label"
                        >Your Username</label
                      >
                      <input
                        type="text"
                        v-model="username"
                        class="form-control"
                        required
                      />
                      <div class="invalid-feedback">
                        Please, enter your name!
                      </div>
                    </div>

                    <div class="col-12">
                      <label for="yourEmail" class="form-label"
                        >Your Email</label
                      >
                      <input
                        type="email"
                        v-model="email"
                        class="form-control"
                        required
                      />
                      <div class="invalid-feedback">
                        Please enter a valid Email adddress!
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
                      <label for="yourPassword" class="form-label"
                        >Confirm Password</label
                      >
                      <input
                        type="password"
                        v-model="confirmPassword"
                        class="form-control"
                        required
                      />
                      <div class="invalid-feedback">
                        Please re-enter your password!
                      </div>
                    </div>

                    <div class="col-12">
                      <div class="form-check">
                        <input
                          class="form-check-input"
                          name="terms"
                          type="checkbox"
                          value=""
                          id="acceptTerms"
                          required
                        />
                        <label class="form-check-label" for="acceptTerms"
                          >I agree and accept the
                          <router-link to="#"
                            >terms and conditions</router-link
                          ></label
                        >
                        <div class="invalid-feedback">
                          You must agree before submitting.
                        </div>
                      </div>
                    </div>
                    <div class="col-12">
                      <button class="btn btn-primary w-100" type="submit">
                        Create Account
                      </button>
                    </div>
                    <div class="col-12">
                      <p class="small mb-0">
                        Already have an account?
                        <router-link to="/">Log in</router-link>
                      </p>
                    </div>
                  </form>
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
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      error: null,
    };
  },
  methods: {
    async register() {
      if (this.password !== this.confirmPassword) {
        this.showError("Passwords do not match!");
        return;
      }

      try {
        const response = await axios.post("http://localhost:5000/register", {
          username: this.username,
          email: this.email,
          password: this.password,
        });

        if (response.data.message === "User registered!") {
          this.showSuccess("Registration successful!", () => {
            // After user clicks 'Ok' on the alert, redirect to login page
            this.$router.push("/Admin"); // Redirect to admin page after successful registration
          });
        } else {
          this.showError("Registration failed");
        }
      } catch (error) {
        this.showError(
          error.response.data.message || "Error occurred while registering"
        );
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
