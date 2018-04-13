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

    let telUser = {};
    // 注册
    mock.onPost('/register').reply(config => {
      let {tel, code} = JSON.parse(config.data);
      telUser[tel] = "123456";
      console.log(telUser);
      if(tel in telUser){
        return new Promise((resolve, reject) => {
          setTimeout(() => {
            resolve([200, {
              info: "注册成功，初始密码为123456"
            }]);
          }, 200);
        });
      }else{
        return new Promise((resolve, reject) => {
          setTimeout(() => {
            resolve([200, {
              error: "手机号已被注册"
            }]);
          }, 200);
        });
      }
    });

    // 登录
    mock.onPost('/login').reply(config => {
      let {tel, password} = JSON.parse(config.data);
      if(tel in telUser){
        if(password != telUser[tel]){
          return new Promise((resolve, reject) => {
            setTimeout(() => {
              resolve([200, {
                error: "手机号或者密码有误！"
              }]);
            }, 200);
          });
        }else{
          return new Promise((resolve, reject) => {
            setTimeout(() => {
              resolve([200, {
                info: "欢迎回来"
              }]);
            }, 200);
          });
        }
      }else{
        return new Promise((resolve, reject) => {
          setTimeout(() => {
            resolve([200, {
              error: "此手机号还未注册，请先注册"
            }]);
          }, 200);
        });
      }
    });

  }
}