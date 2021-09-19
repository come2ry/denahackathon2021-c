<template>
  <div style="height: 90vh; z-index: -1">
    <l-map ref="myMap" :zoom="17" :center="[mapLat, mapLng]">
      <div class="text-center">
        <v-btn
          rounded
          color="primary"
          elevation="50"
          light
          x-large
          @click="buttonClick"
        >
          Let's Siege!
        </v-btn>
      </div>
      <l-tile-layer
        url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
      ></l-tile-layer>
      <l-marker
        v-if="icon !== null"
        ref="myMarker"
        name="あなた"
        :lat-lng="[lat, lng]"
        icon="icon"
      >
        <l-tooltip content="あなた"></l-tooltip>
      </l-marker>
      <l-circle-marker
        v-for="user of otherUsers"
        :key="user.id"
        :name="user.username"
        :lat-lng="[user.lat, user.lng]"
        :icon="icon"
        :color="circle.color"
      >
        <l-tooltip :content="user.username"></l-tooltip>
      </l-circle-marker>
    </l-map>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { LL, ULL } from '@/utils/baseType'
import { genRandomPath, randomScatter } from '~/utils/genRandomPath'
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

    const lat = 35.658319
    const lng = 139.702232
    const otherUsers = randomScatter({ lat, lng }, 30)
    // const icon = this.$L.icon({
    //   iconUrl: '/images/baseball-marker.png',
    //   iconSize: [32, 37],
    //   iconAnchor: [16, 37],
    // })
    return {
      mapLat: lat,
      mapLng: lng,
      lat,
      lng,
      logs: [] as LL[],
      loci: [] as LL[][],
      demo: true,
      k: 0,
      isFirst: true,
      randomPath: [] as LL[],
      otherUsers,
      id: 1,
      myUser: null as ULL | null,
      msg: '',
      icon: null as any,
      circle: {
        center: [47.41322, -1.0482],
        radius: 6,
        color: 'red',
      },
    }
  },
  watch: {
    logs(newLogs) {
      if (!newLogs) return
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
    loci(newLoci) {
      if (!newLoci) return
      for (const locus of newLoci) {
        this.$L
          .polyline(locus as LL[], {
            color: 'blue',
            weight: 4,
            // fill: true,
            // fillColor: 'green',
            opacity: 0.5,
          })
          .addTo((this.$refs.myMap as any).mapObject)
      }
    },
  },
  mounted() {
    // const myMap = this.$L.map('mapid')
    // console.log(myMap)
    this.randomPath = genRandomPath({ lat: 35.658318, lng: 139.702231 }, 100)

    // this.$L
    //   .polyline(randomPath, {
    //     color: 'green',
    //     weight: 2,
    //     fill: true,
    //     fillColor: 'green',
    //     opacity: 0.5
    //   })
    //   .addTo((this.$refs.myMap as any).mapObject)
    this.icon = this.$L.icon({
      iconUrl: '/images/baseball-marker.png',
      iconSize: [32, 37],
      iconAnchor: [16, 37],
    })
    let timer: NodeJS.Timer | null = null
    if (this.demo) {
      timer = setInterval(() => {
        if (this.k >= this.randomPath.length && timer != null) {
          clearInterval(timer)
          return
        }
        this.logs.push(this.randomPath[this.k])

        this.lng = this.randomPath[this.k].lng
        this.lat = this.randomPath[this.k].lat
        this.k++
        if (this.k % 10 === 0) {
          const [loci, rest] = findLoci(this.logs)
          this.loci = loci
          this.logs = rest
        }
      }, 200)
    }
    // GPS センサの値が変化したら何らか実行する geolocation.watchPosition メソッド
    navigator.geolocation.watchPosition(
      (position) => {
        console.log('updated')
        if (timer != null) {
          clearInterval(timer)
        }
        const lat = position.coords.latitude // 緯度を取得
        const lng = position.coords.longitude // 経度を取得
        // const accu = position.coords.accuracy // 緯度・経度の精度を取得
        this.lat = lat
        this.lng = lng
        this.mapLat = lat
        this.mapLng = lng
        this.logs.push({ lat, lng })
        if (this.demo && this.isFirst) {
          this.isFirst = false
          this.randomPath = genRandomPath({ lat, lng }, 100)
          // const realTimer = setInterval(() => {
          //   if (this.k >= randomPath.length) {
          //     clearInterval(realTimer)
          //     return
          //   }
          //   this.logs.push(randomPath[this.k])

          //   this.lng = randomPath[this.k].lng
          //   this.lat = randomPath[this.k].lat
          //   this.k++
          //   if (this.k % 10 === 0) {
          //     const [loci, rest] = findLoci(this.logs)
          //     this.loci = loci
          //     this.logs = rest
          //   }
          // })
        }
        if (!this.demo) {
          this.fetchUsers()
        } else {
          this.otherUsers = randomScatter({ lat, lng }, 30)
        }
      },
      (error) => {
        console.log(error)
      },
      {
        enableHighAccuracy: true, // 高精度で測定するオプション
      }
    )
  },
  methods: {
    buttonClick() {
      this.msg = ''
    },
    async fetchUsers() {
      const len = 0.05
      const top = this.mapLat + len
      const bottom = this.mapLat - len
      const left = this.mapLng - len
      const right = this.mapLng + len
      const res = await this.$axios.$get(
        `http://localhost:8081/api/v1/geo?top=${top}&bottom=${bottom}&left=${left}&right=${right}`
      )
      console.log(res)
      this.otherUsers = res.users
        ?.filter((u: any) => u.id !== this.id)
        .map((u: any) => ({
          lat: u.latitude,
          lng: u.longitude,
          ...u,
        }))
      // console.log(this.otherUsers)
      const resUser = (await this.$axios.$post(
        'http://localhost:8081/api/v1/geo',
        {
          user_id: this.id,
          latitude: this.lat,
          longitude: this.lng,
        }
      )) as any
      console.log(resUser)
    },
  },
})
</script>
<style lang="scss" scoped>
button {
  z-index: 1400 !important;
  position: absolute;
  bottom: 1%;
  left: 50%;
  margin: 0;
  padding: 0;
}
.someExtraClass {
  background-color: aqua;
  padding: 10px;
  border: 1px solid #333;
  border-radius: 0 20px 20px 20px;
  box-shadow: 5px 3px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: auto !important;
  height: auto !important;
  margin: 0 !important;
}
</style>
