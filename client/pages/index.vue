<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card class="logo py-4 d-flex justify-center">
        <NuxtLogo />
        <VuetifyLogo />
      </v-card>
      <v-card>
        <v-card-title class="headline">
          緯度{{ lat }}と経度{{ lng }}
        </v-card-title>
        <v-card-text>
          {{ logs }}
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" nuxt to="/inspire"> Continue </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  setup() {},
  data() {
    return {
      lat: null,
      lng: null,
      accu: null,
      logs: []
    }
  },
  mounted() {
    console.log('here')
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
        // エラー処理（今回は特に何もしない）
      },
      {
        enableHighAccuracy: true // 高精度で測定するオプション
      }
    )
  }
}
</script>
