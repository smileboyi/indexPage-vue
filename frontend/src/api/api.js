import axios from 'axios';


export const getHrDatas = params => {
  return axios.get(`/hr/list`, {
    params: params
  });
};