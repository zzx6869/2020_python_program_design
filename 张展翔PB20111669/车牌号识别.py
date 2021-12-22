from aip import AipOcr

APP_ID = '24505499'
API_KEY = 'cFqOt6iGa1AeEMSFLvnXvueB'
SECRET_KEY = 'LvUx3XQSgDC37Y2DIMbpxVph642fOVGm'
# 创建客户端对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 建立连接的超时时间，单位为毫秒
client.setConnectionTimeoutInMillis(5000)
# 通过打开的连接传输数据的超时时间，单位为毫秒
client.setSocketTimeoutInMillis(5000)


# 读取图片

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('pic.jpg')
res = client.licensePlate(image)
print('车牌号码：' + res['words_result']['number'])
print('车牌颜色：' + res['words_result']['color'])
