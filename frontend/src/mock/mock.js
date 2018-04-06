import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import Mock from 'mockjs';

import { HrDatas } from './data';


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
            todos: HrDatas // 返回状态为200和hr数据
          }]);
        }, 200);
      });
    });

  }
}