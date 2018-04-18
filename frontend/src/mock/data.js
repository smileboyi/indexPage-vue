import Mock from 'mockjs';


let HrDatas = [];
for (let i = 1; i <= 12; i++) {
  HrDatas.push(Mock.mock({ // 根据数据模板生成模拟数据。
    pic_url: "./static/img/woman.jpg",
    "viedeo_src|1": ["http://vjs.zencdn.net/v/oceans.mp4", "https://cdn.theguardian.tv/webM/2015/07/20/150716YesMen_synd_768k_vp8.webm",""],   //hr没有视频时为空字符串
    details: {
      name: Mock.Random.name(),
      "sex|1": ["女","男"],
      join_year: Mock.mock('@date("yyyy")'),
      id: Mock.Random.guid(),  // 随机id
      text: "优小招共享简历模式帮我轻松搞定工作",
      "download_num|1-5000000": 1,
      "share_num|1-5000": 1,
      "convert_num|1-100": 1,
      "gift_value|50-200.2": 1
    }
  }));
}

let giftDatas = [{
  // 第一个是大奖
  id: Mock.Random.guid(),
  pic_url: "./static/img/red-car.jpg",
  title: "法拉利448",
  parameter: "法拉利法拉利法拉利，法拉利法拉利法拉利",
  market_price: "3689000",
  discount_price: "3000000"
}];
for (let i = 1; i <= 7; i++) {
  giftDatas.push(Mock.mock({ // 根据数据模板生成模拟数据。
    id: Mock.Random.guid(),
    pic_url: "https://picsum.photos/400/800/",
    title: "Apple MacBook Pro 15.4英寸笔记本电脑",
    parameter: "银色(Core i7 处理器/16GB内存/256GB",
    market_price: "36890",
    discount_price: "30000"
  }));
}


export {
  HrDatas,
  giftDatas
};