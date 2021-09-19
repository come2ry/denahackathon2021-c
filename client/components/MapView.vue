<template>
  <div style="height: 90vh; z-index: -1">
    <l-map ref="myMap" :zoom="17" :center="[mapLat, mapLng]">
      <div class="text-center btn">
        <v-btn
          rounded
          color="primary"
          elevation="50"
          light
          x-large
          @click="surround"
        >
          囲う！
        </v-btn>
        <v-switch v-model="demo" label="デモ"></v-switch>
      </div>
      <l-tile-layer
        url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
      ></l-tile-layer>
      <l-marker ref="myMarker" name="あなた" :lat-lng="[lat, lng]">
        <l-tooltip content="あなた"></l-tooltip>
      </l-marker>
      <l-marker
        v-for="user of otherUsers"
        :key="user.id"
        :name="user.username"
        :lat-lng="[user.lat, user.lng]"
      >
        <l-tooltip :content="user.username"></l-tooltip>
      </l-marker>
    </l-map>
    <v-switch v-model="demo" label="デモ"></v-switch>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { LL, Locus, ULL } from '@/utils/baseType'
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
    return {
      mapLat: lat,
      mapLng: lng,
      lat,
      lng,
      logs: [] as LL[],
      loci: [] as LL[][],
      k: 0,
      isFirst: true,
      randomPath: [] as LL[],
      otherUsers,
      id: 1,
      myUser: null as ULL | null,
      demo: false,
      surroundedUsers: [] as LL[],
      surroundedLocus: null as Locus | null
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
          opacity: 0.5
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
            opacity: 0.5
          })
          .addTo((this.$refs.myMap as any).mapObject)
      }
    },
    demo(newDemo) {
      if (newDemo) {
        this.demoStart()
      }
    }
  },
  mounted() {
    this.demoStart()
  },
  methods: {
    async surround() {
      const [loci, rest] = findLoci(this.logs)
      this.loci = loci
      this.logs = rest
      for (const locus of loci) {
        try {
          const res = await this.$axios.$post(
            `${this.$config.baseURL}/api/v1/locus`,
            {
              user_id: this.id,
              locus: locus.map((e) => ({
                latitude: e.lat,
                longitude: e.lng
              }))
            }
          )
          console.log(res)
          this.surroundedUsers.concat(res.users)
        } catch (e) {
          console.log(e)
        }
      }
    },
    async fetchUsers() {
      const len = 0.05
      const top = this.mapLat + len
      const bottom = this.mapLat - len
      const left = this.mapLng - len
      const right = this.mapLng + len
      const res = await this.$axios.$get(
        `${this.$config.baseURL}/api/v1/geo?top=${top}&bottom=${bottom}&left=${left}&right=${right}`
      )
      console.log(res)
      this.otherUsers = res.users
        ?.filter((u: any) => u.id !== this.id)
        .map((u: any) => ({
          lat: u.latitude,
          lng: u.longitude,
          ...u
        }))
      // console.log(this.otherUsers)
      const resUser = (await this.$axios.$post(
        `${this.$config.baseURL}/api/v1/geo`,
        {
          user_id: this.id,
          latitude: this.lat,
          longitude: this.lng
        }
      )) as any
      console.log(resUser)
      if (resUser.locus_id != null) {
        const resLocus = (await this.$axios.get(
          `${this.$config.baseURL}/api/v1/locus/${resUser.locus_id}`
        )) as any
        console.log(resLocus)
        this.surroundedLocus = new Locus(resLocus)
      }
    },
    demoStart() {
      this.k = 0
      // const myMap = this.$L.map('mapid')
      // console.log(myMap)
      this.randomPath = genRandomPath({ lat: this.lat, lng: this.lng }, 100)

      // this.$L
      //   .polyline(randomPath, {
      //     color: 'green',
      //     weight: 2,
      //     fill: true,
      //     fillColor: 'green',
      //     opacity: 0.5
      //   })
      //   .addTo((this.$refs.myMap as any).mapObject)
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
          // if (this.k % 10 === 0) {
          //   const [loci, rest] = findLoci(this.logs)
          //   this.loci = loci
          //   this.logs = res (this.k % 10 === 0) {
          //   const [loci, rest] = findLoci(this.logs)
          //   this.loci = loci
          //   this.logs = rest
          // }t
          // }
        }, 200)
      }
      // GPS センサの値が変化したら何らか実行する geolocation.watchPosition メソッド
      navigator.geolocation.watchPosition(
        (position) => {
          console.log('updated')
          // if (timer != null) {
          //   clearInterval(timer)
          // }
          const lat = position.coords.latitude // 緯度を取得
          const lng = position.coords.longitude // 経度を取得
          // const accu = position.coords.accuracy // 緯度・経度の精度を取得
          this.lat = lat
          this.lng = lng
          this.mapLat = lat
          this.mapLng = lng
          this.logs.push({ lat, lng })
          // if (this.demo && this.isFirst) {
          //   this.isFirst = false
          //   this.randomPath = genRandomPath({ lat, lng }, 100)
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
          // }
          if (!this.demo) {
            this.fetchUsers()
          }
          this.otherUsers = randomScatter({ lat, lng }, 30)
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
})
</script>
<style lang="scss" scoped>
.btn {
  z-index: 1400 !important;
  position: absolute;
  bottom: 1%;
  left: 50%;
  margin: 0;
  padding: 0;
}
</style>
