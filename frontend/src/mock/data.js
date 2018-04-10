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

let giftDatas = [{
  // 第一个是大奖
  id: Mock.Random.guid(),
  imgSrc: "/static/img/red-car.jpg",
  title: "法拉利448",
  parameter: "法拉利法拉利法拉利，法拉利法拉利法拉利",
  marketPrice: "3689000",
  discountPrice: "3000000"
}];
for (let i = 1; i <= 7; i++) {
  giftDatas.push(Mock.mock({ // 根据数据模板生成模拟数据。
    id: Mock.Random.guid(),
    imgSrc: "/static/img/product.jpg",
    title: "Apple MacBook Pro 15.4英寸笔记本电脑",
    parameter: "银色(Core i7 处理器/16GB内存/256GB",
    marketPrice: "36890",
    discountPrice: "30000"
  }));
}


export {
  HrDatas,
  giftDatas
};