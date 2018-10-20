

# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode,put_data
import qiniu.config

#需要填写你的 Access Key 和 Secret Key

access_key = '5G9JKa5er7h_Isl3uYus_qBLdgbCbbF-DJ6MLb-n'
secret_key = 'Xz3qJv2IVPYupPExlMEdMvdnD_I4j-Y8dvFLIoDh'

#初始化Auth状态
q = Auth(access_key, secret_key)

#初始化BucketManager


#你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'duanwo'
#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间


#上传到七牛后保存的文件名
key = 'media/python_test2.jpeg'

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
localfile = 'python_test.jpeg'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
