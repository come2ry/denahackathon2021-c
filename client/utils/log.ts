import dayjs from 'dayjs'
import { LL, DLL } from './baseType'
import { Err, Ok, Result } from './result'

export function updateLog(logs: DLL[]): DLL[] {
  return logs.filter((e) => e.date.isAfter(dayjs().subtract(15, 'minutes')))
}

export function findLoci(logs: LL[]): LL[][] {
  let _logs = [...logs]
  const loops = []
  while (true) {
    const locus = _findLocus(_logs)
    if (locus.isOk()) {
      const [loop, rest] = locus.v
      loops.push(loop)
      _logs = rest
    } else {
      break
    }
  }
  return loops
}

function _findLocus(logs: LL[]): Result<[LL[], LL[]], null> {
  for (let end = 2; end < logs.length - 1; end++) {
    // 隣り合う線分は除く
    for (let j = 0; j < end - 1; j++) {
      if (checkCross(end, j, logs)) {
        // end + 1 までで線分
        return new Ok([
          logs.slice(j, end + 2),
          logs.slice(0, j + 1).concat(logs.slice(end + 1))
        ])
      }
    }
  }
  return new Err(null)
}

export function checkCross(i: number, j: number, logs: LL[]): boolean {
  return (
    _checkCross(logs[i], logs[i + 1], logs[j], logs[j + 1]) &&
    _checkCross(logs[j], logs[j + 1], logs[i], logs[i + 1])
  )
}

function _checkCross(a: LL, b: LL, c: LL, d: LL): boolean {
  const s =
    (a.lng - b.lng) * (c.lat - a.lat) - (a.lat - b.lat) * (c.lng - a.lng)
  const t =
    (a.lng - b.lng) * (d.lat - a.lat) - (a.lat - b.lat) * (d.lng - a.lng)
  return s * t <= 0
}
