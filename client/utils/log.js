import dayjs from 'dayjs'

export function updateLog(logs) {
  return logs.filter((e) => e.date.isAfter(dayjs().subtract(15, 'minutes')))
}

export function findLoci(logs) {
  let _logs = [...logs]
  const loops = []
  while (true) {
    const [exist, loop, rest] = _findLocus(_logs)
    if (exist) {
      loops.push(loop)
      _logs = rest
    } else {
      break
    }
  }
  return loops
}

function _findLocus(logs) {
  for (let end = 2; end < logs.length - 1; end++) {
    // 隣り合う線分は除く
    for (let j = 0; j < end - 1; j++) {
      if (checkCross(end, j, logs)) {
        // end + 1 までで線分
        return [
          true,
          logs.slice(j, end + 2),
          logs.slice(0, j + 1).concat(logs.slice(end + 1))
        ]
      }
    }
  }
  return [false, null, null]
}

export function checkCross(i, j, logs) {
  return (
    _checkCross(logs[i], logs[i + 1], logs[j], logs[j + 1]) &&
    _checkCross(logs[j], logs[j + 1], logs[i], logs[i + 1])
  )
}

function _checkCross(a, b, c, d) {
  const s =
    (a.lon - b.lon) * (c.lat - a.lat) - (a.lat - b.lat) * (c.lon - a.lon)
  const t =
    (a.lon - b.lon) * (d.lat - a.lat) - (a.lat - b.lat) * (d.lon - a.lon)
  return s * t <= 0
}
