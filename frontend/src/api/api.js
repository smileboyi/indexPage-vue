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