import Mock from 'mockjs';


let HrDatas = [];
for (let i = 1; i <= 12; i++) {
  HrDatas.push(Mock.mock({ // 根据数据模板生成模拟数据。
    bgUrl: "/static/img/woman.jpg",
    "viedeoUrl|1": ["http://vjs.zencdn.net/v/oceans.mp4", ""],   //hr没有视频时为空字符串
    details: {
      name: Mock.Random.name(),
      "sex|1": ["女","男"],
      joinYear: Mock.mock('@date("yyyy")'),
      id: Mock.Random.guid(),  // 随机id
      text: "优小招共享简历模式帮我轻松搞定工作",
      "downloadNum|1-5000000": 1,
      "shareNum|1-5000": 1,
      "convertNum|1-100": 1,
      "giftValue|50-200.2": 1
    }
  }));
}
export {
  HrDatas
};