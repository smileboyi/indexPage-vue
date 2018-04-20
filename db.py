import pymysql  
import random
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def createGiftDatas():
  global conn,cur
  datas=[]
  price_range = ['1wup','8kup','6kup','4kup','3kup','2kup','1kup','1kdown'] 
  
  # 构造数据
  for pr in price_range:  
    # 构造普通礼品
    for i in range(12):  
      data=(
        "https://picsum.photos/400/800/","Apple MacBook Pro 15.4英寸笔记本电脑","银色(Core i7 处理器/16GB内存/256GB",
        random.randint(3000, 5000),random.randint(1, 3000),0,pr,
      )  
      datas.append(data)
    
    # 构造大礼
    data=(
      "/static/img/red-car.jpg","Apple MacBook Pro 15.4英寸笔记本电脑","银色(Core i7 处理器/16GB内存/256GB",
      random.randint(3000, 5000),random.randint(1, 3000),1,pr,
    )
    datas.append(data)

  # 插入数据
  try:  
    cur.executemany("insert into indexpage_gift(pic_url,title,parameter,market_price,discount_price,is_range_great,price_range)" +
      "values(%s,%s,%s,%s,%s,%s,%s)",datas)  
    conn.commit()
    print("礼品数据已构造完毕")
  except Exception as err:  
    print(err)  


def createHrDatas():
  global conn,cur,now
  datas=[]
  
  for i in range(20):  
    data=(
      "/static/img/woman.jpg","http://vjs.zencdn.net/v/oceans.mp4",
      "优小招",1,now,"优小招共享简历模式帮我轻松搞定工作",
      random.randint(10, 1000),random.randint(10, 1000),random.randint(10, 1000),"653.36"
    )  
    datas.append(data)

  try:  
    cur.executemany("insert into indexpage_hr(pic_url,viedeo_src,name,sex,join_datetime,text,download_num,share_num,convert_num,gift_value)" +
      "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",datas)  
    conn.commit()
    print("hr数据已构造完毕")
  except Exception as err:  
    print(err)  


def createAccountDatas():
  global conn,cur,now
  datas=[(
    "优小招","18888888888","$wuFYQznAsLyxZiLi9zdIZ04afLicNVrfFSAb56K2g6s=",now
  ),]

  try:  
    cur.executemany("insert into indexpage_account(nickname,account_tel,password,add_time)" +
      "values(%s,%s,%s,%s)",datas)  
    conn.commit()
    print("用户数据已构造完毕")
  except Exception as err:  
    print(err)  



if __name__ == "__main__":
  # 连接数据库
  conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='webapp', charset='utf8')
  cur=conn.cursor()
  # 生成数据
  createHrDatas()
  createGiftDatas()
  createAccountDatas()
  # 关闭
  cur.close()
  conn.close()
  