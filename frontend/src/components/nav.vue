<template>
  <!-- Navbar -->
  <nav
    class="absolute top-0 left-0 w-full z-10 bg-transparent md:flex-row md:flex-no-wrap md:justify-start flex items-center p-4"
  >
    <div
      class="w-full mx-autp items-center flex justify-between md:flex-no-wrap flex-wrap md:px-10 px-4"
    >
      <!-- Brand -->
      <div class="flex items-center flex-shrink-0  mr-6">
        <img
          :src="require(`../assets/img${saludoImg}`)"
          style="width:3rem; height:3rem; top:-0.5rem; position: relative"
        />
        <p
          style="margin-left:1rem; size:1.5rem; padding-bottom:0px"
          class="font-bold text-xl tracking-tight"
        >
          {{ saludoTexto }}
        </p>
      </div>
      <!-- Form -->
      <form
        class="md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-3"
      >
        <div class=" flex">
          <span
            class="z-10 h-full leading-snug font-normal absolute text-center text-gray-400 absolute bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3"
            ><i class="fas fa-search"></i
          ></span>
          <input
            type="text"
            placeholder="Search for articles"
            class="px-3 py-3 bg-gray-200 placeholder-gray-500 text-gray-700 relative rounded text-md shadow outline-none focus:outline-none focus:shadow-outline w-full pl-10"
          />
          <button
            class="bg-blue-500 text-white text-md active:bg-blue-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1"
            type="button"
            style="position:relative; left:0.2rem; top:0.2rem"
          >
            <i class="fa fa-search" aria-hidden="true"></i>
          </button>
        </div>
      </form>
    </div>
  </nav>

  <!-- End Navbar -->
</template>
<script>
export default {
  components: {},
  data() {
    return {
      saludoTexto: "",
      saludoImg: "",
    };
  },
  methods: {
    saludo() {
      let fecha = new Date();
      let hora = fecha.getHours();
      console.log(fecha, hora);
      if (hora >= 0 && hora < 12) {
        this.saludoTexto = "Good Mornig";
        this.saludoImg = "/manana.png";
      }

      if (hora >= 12 && hora < 18) {
        this.saludoTexto = "Good Afternoon";
        this.saludoImg = "/tarde.png";
      }

      if (hora >= 18 && hora < 24) {
        this.saludoTexto = "Good Evening";
        this.saludoImg = "/tarde.png";
      }
      console.log(this.saludoTexto, this.saludoImg);
    },
  },
  created() {
    this.saludo();
  },
};
</script>
