import { get } from 'lodash'


export const getSlugByIndex = (window, index) => {
  const pathname = get(window, ['location', 'pathname'])
  const pathArr = pathname.split('/')
  return pathArr[index]
}