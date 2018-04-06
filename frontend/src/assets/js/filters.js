export const createBgStyle =  (val) => {
  if (!val) return '';
  return `background-image: url(${val})`;
}