<template>
  <div>
    <a
      class="text-gray-600 block"
      v-on:click="toggleDropdown($event)"
      ref="btnDropdownRef"
    >
      <div class="items-left flex-end">
        <span
          class="w-12 h-12 text-sm text-white bg-gray-300 inline-flex items-center justify-center rounded-full"
        >
          <img
            alt="..."
            src="../assets/img/profile.jpg"
            class="w-full rounded-full align-middle border-none shadow-lg"
          />
        </span>
      </div>
    </a>
    <div class="items-left text-lg leading-normal font-semibold  flex-end my-4">
      {{ this.date }}
    </div>
    <div class="items-left flex-end my-1">
      {{ this.time }}
    </div>
    <div
      ref="popoverDropdownRef"
      class="bg-white text-base z-50 float-left py-2 list-none text-left rounded ml-10 shadow-lg mt-1"
      v-bind:class="{
        hidden: !dropdownPopoverShow,
        block: dropdownPopoverShow,
      }"
      style="min-width: 12rem"
    >
      <a
        href="/login"
        class="text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800"
      >
        Login
      </a>

      <div class="h-0 my-2 mx-4 border border-solid border-gray-200" />
    </div>
  </div>
</template>
<script>
import Popper from "popper.js";

export default {
  data() {
    let d = new Date();
    var months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    let saludo = d.getHours < 12 ? "pm" : "am";
    return {
      dropdownPopoverShow: false,
      date2: d.getTime(),
      date: months[d.getMonth()] + " " + d.getDay() + ", " + d.getFullYear(),
      time: d.getHours() + ":" + d.getMinutes() + saludo,
    };
  },
  methods: {
    toggleDropdown: function(event) {
      event.preventDefault();
      if (this.dropdownPopoverShow) {
        this.dropdownPopoverShow = false;
      } else {
        this.dropdownPopoverShow = true;
        new Popper(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
          placement: "bottom-end",
        });
      }
    },
  },
};
</script>
