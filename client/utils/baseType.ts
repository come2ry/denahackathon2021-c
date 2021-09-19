import { Dayjs } from 'dayjs'

export type LL = {
  lat: number
  lng: number
}

export type DLL = LL & {
  date: Dayjs
}

export type ULL = LL & {
  id: number
  username: string
}

export type LocusDL = {
  // eslint-disable-next-line camelcase
  user_id: number
  username: string
  locus: {
    latitude: number
    longitude: number
  }[]
}

export class Locus {
  // eslint-disable-next-line camelcase
  user_id: number
  username: string
  locus: LL[]
  constructor(l: LocusDL) {
    this.user_id = l.user_id
    this.username = l.username
    this.locus = l.locus.map((e) => ({
      lat: e.latitude,
      lng: e.longitude
    }))
  }
}
