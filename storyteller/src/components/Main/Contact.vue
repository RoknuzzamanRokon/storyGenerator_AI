<template>
  <div>
    <section>
      <div class="container">
        <div class="w-md-75 w-lg-50 text-center mx-md-auto mb-6">
          <h2 class="line-title">Quick Contact</h2>
        </div>

        <div class="row mt-n5">
          <div class="col-lg-6 mt-5">
            <!-- start form here -->
            <form
              class="quform"
              action=""
              method="post"
              enctype="multipart/form-data"
              onclick=""
            >
              <div class="quform-elements">
                <div class="row">
                  <!-- Begin Text input element -->
                  <div class="col-md-6">
                    <div class="quform-element form-group">
                      <label for="name"
                        >Your Name <span class="quform-required">*</span></label
                      >
                      <div class="quform-input">
                        <input
                          class="form-control"
                          id="name"
                          type="text"
                          name="name"
                          placeholder="Your name here"
                        />
                      </div>
                    </div>
                  </div>
                  <!-- End Text input element -->

                  <!-- Begin Text input element -->
                  <div class="col-md-6">
                    <div class="quform-element form-group">
                      <label for="email"
                        >Your Email
                        <span class="quform-required">*</span></label
                      >
                      <div class="quform-input">
                        <input
                          class="form-control"
                          type="text"
                          name="email"
                          placeholder="Your email here"
                        />
                      </div>
                    </div>
                  </div>
                  <!-- End Text input element -->

                  <!-- Begin Text input element -->
                  <div class="col-md-6">
                    <div class="quform-element form-group">
                      <label for="subject"
                        >Your Subject
                        <span class="quform-required">*</span></label
                      >
                      <div class="quform-input">
                        <input
                          class="form-control"
                          type="text"
                          name="subject"
                          placeholder="Your subject here"
                        />
                      </div>
                    </div>
                  </div>
                  <!-- End Text input element -->

                  <!-- Begin Text input element -->
                  <div class="col-md-6">
                    <div class="quform-element form-group">
                      <label for="phone">Contact Number</label>
                      <div class="quform-input">
                        <input
                          class="form-control"
                          id="phone"
                          type="text"
                          name="phone"
                          placeholder="Your phone number"
                        />
                      </div>
                    </div>
                  </div>
                  <!-- End Text input element -->

                  <!-- Begin Textarea element -->
                  <div class="col-md-12">
                    <div class="quform-element form-group">
                      <label for="message"
                        >Message <span class="quform-required">*</span></label
                      >
                      <div class="quform-input">
                        <textarea
                          class="form-control"
                          id="message"
                          name="message"
                          rows="4"
                          placeholder="Tell us a few words"
                        ></textarea>
                      </div>
                    </div>
                  </div>
                  <!-- End Textarea element -->

                  <!-- Begin Submit button -->
                  <div class="col-md-12">
                    <div class="quform-submit-inner">
                      <button class="butn style-one fill" type="submit">
                        <span>Submit Comment</span>
                      </button>
                    </div>
                    <div class="quform-loading-wrap text-start">
                      <span class="quform-loading"></span>
                    </div>
                  </div>
                  <!-- End Submit button -->
                </div>
              </div>
            </form>
            <!-- end form here -->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
