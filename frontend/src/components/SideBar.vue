<template>
  <nav
    class="md:left sidebar md: md:fixed md:top md:bottom  md:flex-row  md:overflow-hidden  bg-white flex flex-wrap items-center justify-between absolute md:w-64 z-10 py-4 px-6"
  >
    <div
      class="md:flex-col md:items-stretch md:min-h-full md:flex-no-wrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"
    >
      <!-- Toggler -->
      <button
        class="cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent"
        type="button"
        v-on:click="toggleCollapseShow('bg-white m-2 py-3 px-6')"
      >
        <i class="fas fa-bars"></i>
      </button>
      <!-- Brand -->
      <!-- <a
        class="md:block text-left md:pb-2 text-gray-700 mr-0 inline-block whitespace-no-wrap text-sm uppercase font-bold p-4 px-0"
        href="javascript:void(0)"
      >
        Tailwind Starter Kit
      </a> -->
      <!-- User -->
      <ul
        class="md: items-center flex flex-wrap list-none ml-20 relative align-middle"
      >
        <li class="inline-block relative">
          <user-dropdown-component></user-dropdown-component>
        </li>
      </ul>
      <!-- Collapse -->
      <div
        class="md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded"
        v-bind:class="collapseShow"
      >
        <!-- Form -->
        <form class="mt-6 mb-4 md:hidden">
          <div class="mb-3 pt-0">
            <input
              type="text"
              placeholder="Search"
              class="px-3 py-2 h-12 border border-solid  border-gray-600 placeholder-gray-400 text-gray-700 bg-white rounded text-base leading-snug shadow-none outline-none focus:outline-none w-full font-normal"
            />
          </div>
        </form>
        <!-- Navigation -->
        <ul class="md:flex-col md:min-w-full flex flex-col list-none">
          <li class="items-center">
            <router-link :to="{ name: 'Sports' }">
              <a
                class="text-pink-500 hover:text-pink-600 text-xs uppercase py-3 font-bold block"
                ><i class="fas fa-newspaper opacity-75 mr-2 text-sm"></i>
                Sports</a
              >
            </router-link>
          </li>
          <li class="items-center">
            <router-link :to="{ name: 'Health' }">
              <a
                class="text-pink-500 hover:text-pink-600 text-xs uppercase py-3 font-bold block"
                ><i class="fas fa-newspaper opacity-75 mr-2 text-sm"></i>
                Halth</a
              >
            </router-link>
          </li>
          <li class="items-center">
            <router-link :to="{ name: 'International' }">
              <a
                class="text-pink-500 hover:text-pink-600 text-xs uppercase py-3 font-bold block"
                ><i class="fas fa-newspaper opacity-75 mr-2 text-sm"></i>
                World</a
              >
            </router-link>
          </li>
        </ul>

        <!-- subcriber -->
        <div
          class="w-full py-4 bg-blue-600 rounded-lg lg:w-12/12 xl:w-12/12 px-4 my-40"
        >
          <form
            class="md:flex  flex-row flex-wrap items-left lg:ml-auto mr-3"
            v-on:submit.prevent="saveemail"
          >
            <h6 class="text-md font-bold leading-normal mt-0 mb-2 text-white">
              Subscriber to Newsletter
            </h6>
            <div class="flex">
              <input
                type="email"
                v-model="email"
                placeholder="Enter email"
                class="px-1 py-2 bg-gray-200 placeholder-gray-500 text-gray-700 relative rounded text-sm shadow outline-none focus:outline-none focus:shadow-outline w-full pl-4"
              />
              <button
                class="bg-blue-500 text-white text-xs active:bg-blue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none "
                type="submit"
                style="position:relative; left:0.2rem; "
              >
                <i class="fa fa-paper-plane" aria-hidden="true"></i>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
import UserDropdownComponent from "./UserDrop";
import axios from "axios";

export default {
  data() {
    let d = new Date();

    return {
      collapseShow: "hidden",
      email: "",
      date: d.getFullYear(),
    };
  },
  methods: {
    toggleCollapseShow: function(classes) {
      this.collapseShow = classes;
    },
    saveemail() {
      if (this.email) {
        axios
          .post("http://127.0.0.1:5000/api/v1/add-subs", {
            email: this.email,
          })
          .then((response) => {
            console.log(response.data);
            this.email = "";
          })
          .catch((error) => this.errors.push(error));
      } else {
        console.log("no email");
      }
    },
  },
  components: {
    UserDropdownComponent,
  },
};
</script>

<style>
.sidebar {
  height: 80%;
}
</style>
