import { Dayjs } from 'dayjs'

export type LL = {
  lat: number
  lng: number
}

export type DLL = LL & {
  date: Dayjs
}

export type ULL = LL & {
  username: string
}
