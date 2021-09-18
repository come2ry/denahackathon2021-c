<template>
  <div id="mapid" style="height: 100vh">
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

<script lang="ts">
import Vue from 'vue'

type LL = {
  lat: number
  lng: number
}
export default Vue.extend({
  data() {
    const logs: LL[] = [
      [35.658318, 139.702231],
      [35.6583, 139.702232],
      [35.6582, 139.702232],
      [35.6581, 139.702235]
    ].map((e) => ({
      lat: e[0],
      lng: e[1]
    }))
    return {
      lat: 35.658319,
      lng: 139.702232,
      logs
    } as {
      lat: number
      lng: number
      logs: LL[]
    }
  },
  watch: {
    logs(newLogs) {
      if (newLogs == null) return
      const myMap = this.$L.map('mapid')
      this.$L
        .polyline(newLogs as LL[], {
          color: 'green',
          weight: 2,
          fill: true,
          fillColor: 'green',
          opacity: 0.5
        })
        .addTo(myMap)
    }
  },
  mounted() {
    // GPS センサの値が変化したら何らか実行する geolocation.watchPosition メソッド
    navigator.geolocation.watchPosition(
      (position) => {
        const myMap = this.$L.map('mapid')
        console.log(myMap)
        this.$L
          .polyline(this.logs as LL[], {
            color: 'green',
            weight: 2,
            fill: true,
            fillColor: 'green',
            opacity: 0.5
          })
          .addTo(myMap)
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
})
</script>
