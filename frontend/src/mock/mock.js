import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import Mock from 'mockjs';

import { HrDatas, giftDatas } from './data';


 // 创建 MockAdapter 实例
let mock = new MockAdapter(axios);

export default {
  // Mock start
  start(){
    // 获取hr列表
    mock.onGet('/hr/list').reply(config => { //  config 指前台传过来的值
      return new Promise((resolve, reject) => {
        setTimeout(() => {   //模拟延迟
          resolve([200, {
            datas: HrDatas // 返回状态为200和hr数据
          }]);
        }, 200);
      });
    });

    // 获取gift列表
    mock.onGet('/gift/list').reply(config => {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          resolve([200, {
            datas: giftDatas
          }]);
        }, 200);
      });
    });
  }
}