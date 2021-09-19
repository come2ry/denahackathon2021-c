import { checkCross, findLoci } from '~/utils/log'

test('checkCross', () => {
  const logs = [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [-1, 0]
  ].map((e) => ({
    lng: e[0],
    lat: e[1]
  }))
  expect(checkCross(3, 0, logs)).toBe(true)
})

test('findLoci', () => {
  const logs = [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [-1, 0]
  ].map((e) => ({
    lng: e[0],
    lat: e[1]
  }))
  expect(findLoci(logs)).toStrictEqual([[...logs]])
})

test('findTwoLoci', () => {
  const logs = [
    [-2, 1],
    [0, -1],
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [-0.5, 0],
    [-1, 0],
    [-2, 0]
  ].map((e) => ({
    lng: e[0],
    lat: e[1]
  }))
  expect(findLoci(logs)).toStrictEqual([
    [
      { lng: 0, lat: -1 },
      { lng: 0, lat: 0 },
      { lng: 0, lat: 1 },
      { lng: 1, lat: 1 },
      { lng: 1, lat: 0 },
      { lng: -0.5, lat: 0 }
    ],
    [
      { lng: -2, lat: 1 },
      { lng: 0, lat: -1 },
      { lng: -0.5, lat: 0 },
      { lng: -1, lat: 0 }
    ]
  ])
})
