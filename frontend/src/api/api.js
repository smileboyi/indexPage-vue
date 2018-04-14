import axios from 'axios';


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
  return axios.post(`/register`, params).then(res => res.data);
};

export const fetchLogin = params => {
  return axios.post(`/login`, params).then(res => res.data);
};

export const fetchLogout = params => {
  return axios.post(`/logout`, params).then(res => res.data);
};