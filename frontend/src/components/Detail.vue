<template>
  <div class="bg-white base  overflow-auto" style="overflow-auto overflow: ;">
    <sidebar-component></sidebar-component>
    <div class="relative md:ml-64 ">
      <!-- Header -->
      <!-- <div class="relative  md:pt-32 pb-32 pt-12"></div> -->
      <div class="relative news md:pt-32 pb-32 pt-12  ">
        <navbar-component></navbar-component>
        <div class="px-2 my-10">
          <div class="flex flex-wrap justify-center w-full">
            <div class="relative">
              <img
                :src="this.new.image"
                class="shadow-xl w-full h-auto align-middle border-none  "
                style="max-width: 60rem;"
              />
            </div>
          </div>

          <div class="text-center mt-12 py-10">
            <h3
              class="text-4xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
            >
              {{ this.new.title }}
            </h3>
            <div
              class="text-sm leading-normal mt-0 mb-2 text-gray-500 font-bold uppercase"
            >
              <i class="fas fa-briefcase mr-2 text-lg text-gray-500"></i>
              AUTHOR: {{ this.new.author[0] }}
            </div>
            <div
              class="text-sm leading-normal mt-0 mb-2 text-gray-500 font-bold uppercase"
            >
              DATE:
              {{
                this.new.publish_date
                  ? Date(this.new.publish_date["$date"])
                  : ""
              }}
            </div>
            <div class="flex flex-wrap justify-center">
              <div class="w-full lg:w-9/12 px-4">
                <p class="mb-4 text-lg leading-relaxed text-gray-800">
                  {{ this.new.summary }}
                </p>
              </div>
            </div>
          </div>
          <div class="mt-10 py-10 border-t border-gray-300 text-center">
            <div class="flex flex-wrap justify-center">
              <div class="w-full lg:w-9/12 px-4">
                <p class="mb-4 text-lg leading-relaxed text-gray-800">
                  {{ this.new.description }}
                </p>
              </div>
              <div class="px-4 py-4">
                <span
                  v-for="(key, i) in this.new.keywords"
                  :key="i"
                  class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2"
                  >#{{ key }}
                </span>
              </div>
            </div>
          </div>
        </div>
        <router-link :to="{ name: 'Home' }">
          <button
            class="bg-red-700 text-white active:bg-red-900 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 "
            type="button"
            style="transition: all 0.15s ease 0s;"
          >
            Go Back
            <i class="fa fa-chevron-right" aria-hidden="true"></i>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
import NavbarComponent from "./nav.vue";
import SidebarComponent from "./SideBar.vue";
import axios from "axios";
export default {
  name: "dashboard-page",
  components: {
    NavbarComponent,
    SidebarComponent,
  },
  data() {
    return {
      date: new Date().getFullYear(),
      new: [],
    };
  },
  created: function() {
    this.id = this.$route.params.id;
    axios
      .get("http://127.0.0.1:5000/api/v1/new/" + this.id)
      .then((response) => {
        this.new = response.data;
        console.log(response.data);
      })
      .catch((error) => this.errors.push(error));
  },
};
</script>

<style>
.base {
  top: 5vh;
  height: 90vh !important;
  width: 95vw !important;
  display: block;
  margin: auto;
  padding: 2rem;
  position: relative;
  border-radius: 2rem !important;
  box-shadow: 0 25px 35px -3px rgba(0, 0, 0, 0.507),
    0 6px 8px -4px rgba(0, 0, 0, 0.178);
}
.backnews {
  height: 95% !important;
  border-radius: 2rem !important;
  z-index: 2;
  margin-top: 15rem;
  position: absolute;
  width: 100% !important;
}

.news {
  z-index: 90;
}
</style>
