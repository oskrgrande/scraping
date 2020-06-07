<template>
  <div class="bg-white base  overflow-auto" style="overflow-auto overflow: ;">
    <sidebar-component></sidebar-component>
    <div class="relative md:ml-64 ">
      <!-- Header -->
      <div class="backnews bg-gray-200 w-full"></div>
      <!-- <div class="relative  md:pt-32 pb-32 pt-12"></div> -->
      <div class="relative news md:pt-32 pb-32 pt-12  ">
        <navbar-component></navbar-component>
        <div class="flex flex-wrap ">
          <div class=" py-4   lg:w-8/12 xl:w-8/12 px-4">
            <div
              class="relative px-8 flex flex-col min-w-4 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
            >
              <img
                class="w-full py-4"
                :src="this.daily.image"
                style="
              position:relative; align-self: center;max-width: 30rem;"
              />
              <div class="px-4 py-4">
                <div class="font-bold text-xl mb-2">{{ this.daily.title }}</div>
                <p class="text-gray-700 text-base">
                  {{ this.daily.summary }}
                </p>
              </div>
              <div class="px-4 py-4">
                <span
                  class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2"
                  >Author: {{ this.daily.author[0] }}</span
                >
              </div>
              <div class="px-4 py-4">
                <span
                  class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2"
                  >Date:
                  {{
                    this.daily.publish_date
                      ? Date(this.daily.publish_date["$date"])
                      : ""
                  }}
                </span>
              </div>
              <div class="px-4 py-4">
                <router-link
                  :to="{ name: 'Detail', params: { id: this.daily._id.$oid } }"
                >
                  <button
                    class="bg-red-700 text-white active:bg-red-900 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full"
                    type="button"
                    style="transition: all 0.15s ease 0s;"
                  >
                    Show More
                    <i class="fa fa-chevron-right" aria-hidden="true"></i>
                  </button>
                </router-link>
              </div>
            </div>
          </div>
          <div class=" py-4  lg:w-4/12 xl:w-4/12 px-4">
            <div
              class="  flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg my-10"
            >
              <div class="px-6">
                <div class="flex flex-wrap justify-center">
                  <div
                    class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center"
                  >
                    <div class="relative">
                      <img
                        alt="..."
                        src="../assets/img/escritor.png"
                        class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16"
                        style="max-width: 150px;"
                      />
                    </div>
                  </div>
                </div>
                <div class="text-center mt-12 py-10">
                  <h3
                    class="text-4xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
                  >
                    {{ this.author.author[0] }}
                  </h3>
                  <div
                    class="text-sm leading-normal mt-0 mb-2 text-gray-500 font-bold uppercase"
                  >
                    BEST AUTHOR OF WEEK
                  </div>
                </div>
                <div
                  class="mt-10 py-10 border-t border-gray-300 text-center"
                ></div>
              </div>
            </div>
          </div>
        </div>
        <div class="flex flex-wrap ">
          <div
            class=" py-4  lg:w-6/12 xl:w-4/12 px-4"
            v-for="article in news"
            :key="article.id"
          >
            <div
              class="relative px-8 flex flex-col min-w-4 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
            >
              <img
                class="w-full py-4"
                style=" position:relative; align-self: center;"
                :src="article.image"
                alt="Sunset in the mountains"
              />
              <div class="px-4 py-4">
                <div class="font-bold text-xl mb-2">{{ article.title }}</div>
                <p class="text-gray-700 text-base">
                  {{ article.summary }}
                </p>
              </div>
              <div class="px-4 py-4">
                <span
                  class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2"
                  >Author: {{ article.author[0] }}</span
                >
              </div>
              <div class="px-4 py-4">
                <span
                  class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2"
                  >Date:
                  {{
                    article.publish_date
                      ? Date(article.publish_date["$date"])
                      : ""
                  }}
                </span>
              </div>
              <div class="px-4 py-4">
                <router-link
                  :to="{ name: 'Detail', params: { id: article._id.$oid } }"
                >
                  <button
                    class="bg-red-700 text-white active:bg-red-900 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full"
                    type="button"
                    style="transition: all 0.15s ease 0s;"
                  >
                    Show More
                    <i class="fa fa-chevron-right" aria-hidden="true"></i>
                  </button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
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
      news: [],
      daily: {},
      email: "",
      author: "",
    };
  },
  created: function() {
    axios
      .get("http://127.0.0.1:5000/api/v1/daily-new")
      .then((response) => {
        this.daily = response.data[0];
        console.log(response.data);
      })
      .catch((error) => this.errors.push(error));

    axios
      .get("http://127.0.0.1:5000/api/v1/best-author")
      .then((response) => {
        this.author = response.data[0];
        console.log(response.data, "best");
      })
      .catch((error) => this.errors.push(error));
    axios
      .get("http://127.0.0.1:5000/api/v1/news")
      .then((response) => {
        this.news = response.data;
        console.log(response.data);
      })
      .catch((error) => this.errors.push(error));
  },
  methods: {},
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
