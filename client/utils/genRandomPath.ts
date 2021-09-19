import { LL } from './baseType'

function random(): number {
  return Math.random() - 0.5
}

export function genRandomPath(home: LL, length: number): LL[] {
  const path = [home]
  for (let i = 0; i < length; i++) {
    const last = path[path.length - 1]
    path.push({
      lat: last.lat + random() * 0.001,
      lng: last.lng + random() * 0.001
    })
  }
  return path
}
