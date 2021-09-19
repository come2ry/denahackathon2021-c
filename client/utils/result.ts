// npm ライブラリ neverthrowを参考に。必要であれば package を入れる

export class Ok<T, E> {
  // eslint-disable-next-line no-useless-constructor
  constructor(readonly v: T) {}
  readonly type = 'Ok' as const
  isOk(): this is Ok<T, E> {
    return true
  }

  isErr(): this is Err<T, E> {
    return false
  }
}

export class Err<T, E> {
  // eslint-disable-next-line no-useless-constructor
  constructor(readonly v: E) {}
  readonly type = 'Err' as const
  isOk(): this is Ok<T, E> {
    return false
  }

  isErr(): this is Err<T, E> {
    return true
  }
}
export type Result<T, E> = Ok<T, E> | Err<T, E>
