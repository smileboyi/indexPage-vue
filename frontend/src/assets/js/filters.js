export const telNumberHide = tel => { 
  return tel.replace(/(\d{3})\d{4}(\d{4})/, '$1****$2');
}

export const numTurnSex = num => { 
  return num == 1 ? "男" : "女";
}