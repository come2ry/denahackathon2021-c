<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card class="logo py-4 d-flex justify-center">
        <LocationView />
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
          <v-btn color="primary" nuxt to="/map"> Continue </v-btn>
        </v-card-actions>
      </v-card>
      <table>
        <tr>
          <th>順位</th>
          <th>ユーザー</th>
          <th>ひとこと</th>
          <th>住所</th>
        </tr>
        <tr>
          <td>
            <v-avater size="18px">
              <img width="50%" alt="Avatar" src="@/assets/ranking/1.jpg" />
            </v-avater>
          </td>
          <td class="icon">鳥</td>
          <td>空を飛ぶのがすきです！</td>
          <td>東京</td>
        </tr>
        <tr>
          <td>
            <v-avater size="18px">
              <img width="50%" alt="Avatar" src="@/assets/ranking/2.jpg" />
            </v-avater>
          </td>
          <td class="icon">クジラ</td>
          <td>潮を吹くのがすきです！</td>
          <td>北海道</td>
        </tr>
        <tr>
          <td>
            <v-avater size="18px">
              <img width="50%" alt="Avatar" src="@/assets/ranking/3.jpg" />
            </v-avater>
          </td>
          <td class="icon">カニ</td>
          <td>反復横飛び鍛えてます</td>
          <td>川</td>
        </tr>
      </table>
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
      logs: [],
    }
  },
  mounted() {
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
        enableHighAccuracy: true, // 高精度で測定するオプション
      }
    )
  },
}
</script>

<style lang="scss" scoped>
table {
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  tr {
    border-bottom: solid 1px #eee;
    cursor: pointer;
    &:hover {
      background-color: #d4f0fd;
    }
  }
  th,
  td {
    text-align: center;
    width: 25%;
    padding: 15px 0;
  }
  td.icon {
    background-size: 35px;
    background-position: left 5px center;
    background-repeat: no-repeat;
    padding-left: 30px;
  }
}
</style>
