
export const checkPhone = tel => { 
  return /^1(3|4|5|7|8)\d{9}$/.test(tel);
}