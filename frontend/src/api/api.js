import axios from 'axios';
import qs from 'qs';


// 当api过多时，也可以把这些api放进store的actions中
export const getHrDatas = params => {
  return axios.get(`/hr/list`, {
    params: params
  });
};

export const getGiftDatas = params => {
  return axios.get(`/gift/list`, {
    params: params
  });
};

export const fetchRegister = params => {
  return axios.post(`/register`, qs.stringify(params)).then(res => res.data);
};

export const fetchLogin = params => {
  return axios.post(`/login`, qs.stringify(params)).then(res => res.data);
};

export const fetchLogout = params => {
  return axios.post(`/logout`, qs.stringify(params)).then(res => res.data);
};