<template>
  <div style="height: 100vh; z-index: -1">
    <l-map ref="myMap" :zoom="17" :center="[mapLat, mapLng]">
      <l-tile-layer
        url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
      ></l-tile-layer>
      <l-marker ref="myMarker" name="あなた" :lat-lng="[lat, lng]">
        <l-tooltip content="あなた"></l-tooltip>
      </l-marker>
    </l-map>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { LL } from '@/utils/baseType'
import { genRandomPath } from '~/utils/genRandomPath'
import { findLoci } from '~/utils/log'

export default Vue.extend({
  data() {
    // const logs: LL[] = [
    //   [35.658318, 139.702231],
    //   [35.6583, 139.7021],
    //   [35.6582, 139.702],
    //   [35.6581, 139.7019]
    // ].map((e) => ({
    //   lat: e[0],
    //   lng: e[1]
    // }))
    return {
      mapLat: 35.658319,
      mapLng: 139.702232,
      lat: 35.658319,
      lng: 139.702232,
      logs: [] as LL[],
      demo: true,
      k: 0,
    }
  },
  watch: {
    logs(newLogs) {
      if (newLogs == null) return
      this.$L
        .polyline(newLogs as LL[], {
          color: 'green',
          weight: 2,
          // fill: true,
          // fillColor: 'green',
          opacity: 0.5,
        })
        .addTo((this.$refs.myMap as any).mapObject)
    },
  },
  mounted() {
    // const myMap = this.$L.map('mapid')
    // console.log(myMap)
    const randomPath = genRandomPath({ lat: 35.658318, lng: 139.702231 }, 100)
    console.log(findLoci(randomPath))

    // this.$L
    //   .polyline(randomPath, {
    //     color: 'green',
    //     weight: 2,
    //     fill: true,
    //     fillColor: 'green',
    //     opacity: 0.5
    //   })
    //   .addTo((this.$refs.myMap as any).mapObject)
    if (this.demo) {
      const timer = setInterval(() => {
        if (this.k >= randomPath.length) {
          clearInterval(timer)
        }
        this.logs = randomPath.slice(0, this.k + 1)

        this.lng = randomPath[this.k].lng
        this.lat = randomPath[this.k].lat
        this.k++
      }, 200)
    }
    // GPS センサの値が変化したら何らか実行する geolocation.watchPosition メソッド
    navigator.geolocation.watchPosition(
      (position) => {
        const lat = position.coords.latitude // 緯度を取得
        const lng = position.coords.longitude // 経度を取得
        // const accu = position.coords.accuracy // 緯度・経度の精度を取得
        this.lat = lat
        this.lng = lng
        this.mapLat = lat
        this.mapLng = lng
        this.logs.push({ lat, lng })
      },
      (error) => {
        console.log(error)
      },
      {
        enableHighAccuracy: true, // 高精度で測定するオプション
      }
    )
  },
})
</script>
