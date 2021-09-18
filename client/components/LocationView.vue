<template>
  <div>
    {{ locus }}
    {{ geo }}
  </div>
</template>
<script>
export default {
  name: 'LocationView',
  data() {
    return {
      geo: null,
      locus: null,
      loading: true,
      errored: false
    }
  },
  mounted() {
    this.$axios
      .$get('http://localhost:8081/api/v1/geo')
      .then((response) => (this.geo = response))
      .catch((error) => {
        // エラー処理
        console.log(error)
        this.errored = true
      })
    this.$axios
      .$get('http://localhost:8081/api/v1/locus')
      .then((response) => (this.locus = response))
      .catch((error) => {
        // エラー処理
        console.log(error)
        this.errored = true
      })
  }
}
</script>
