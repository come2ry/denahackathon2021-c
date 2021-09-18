<template>
  <div style="height: 100vh">
    <client-only>
      <l-map :zoom="13" :center="[lat, lng]">
        <l-tile-layer
          url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
        ></l-tile-layer>
        <l-marker :lat-lng="[lat, lng]"></l-marker>
      </l-map>
    </client-only>
  </div>
</template>

<script>
export default {
  data() {
    return {
      lat: null,
      lng: null,
      accu: null,
      logs: []
    }
  },
  watch: {
    logs(newLogs) {
      if (newLogs == null) return
      this.$L
        .polyline(newLogs, {
          color: 'green',
          weight: 2,
          fill: true,
          fillColor: 'green',
          opacity: 0.5
        })
        .addTo(this.$L.myMap.mapObject)
    }
  },
  mounted() {
    console.log(this.$L)

    // GPS センサの値が変化したら何らか実行する geolocation.watchPosition メソッド
    navigator.geolocation.watchPosition(
      (position) => {
        const lat = position.coords.latitude // 緯度を取得
        const lng = position.coords.longitude // 経度を取得
        // const accu = position.coords.accuracy // 緯度・経度の精度を取得
        this.lat = lat
        this.lng = lng
        this.logs.push({ lat, lng })
      },
      (error) => {
        console.log(error)
      },
      {
        enableHighAccuracy: true // 高精度で測定するオプション
      }
    )
  }
}
</script>
