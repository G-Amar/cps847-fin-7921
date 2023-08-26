<script>

const API_URL = "https://api.openweathermap.org/data/2.5/weather?q=London,on,ca&units=metric&APPID=";
const API_KEY = "PLACEHOLDER"; //add you API key here

export default {
  data: () => ({
    data: null,
    myTS: null,
    condition: null,
    temperature: null
  }),

  created() {
    // fetch on init
    this.fetchData()
  },

  methods: {
    async fetchData() {
      const url = `${API_URL}${API_KEY}`
      this.data = await (await fetch(url)).json()
      this.myTS = this.data.dt;
      this.condition = this.data.weather[0].description;
      this.temperature = this.data.main.temp; //already in Celsius
    },
  }
}

</script>

<template>
  <div id="w-header">Prediction's timestamp: {{ myTS }}</div>
  <div id="w-condition">Condition: {{ condition }}</div>
  <div id="w-temperature">Temperature: {{ temperature }}</div>
</template>

<style>

</style>
