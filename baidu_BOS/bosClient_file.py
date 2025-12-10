from baidubce.services.sts.sts_client import StsClient
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
import time
from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient

sts_ak = "7480489799e511f0bdd4af2eba797bea"
sts_sk = "bc91b447cad14e828bc666a1312586c9"
token = "ZjkyZmQ2YmQxZTQ3NDcyNjk0ZTg1ZjYyYjlkZjNjODB8AAAAAFcDAAA87rFmhZ70x8el5NmNpNyrFOHXM6EVqkoxyOt/V+J/b1N+TAybp0Sq1XYnQk1tfzsUdOdYaAY3EgCjReawTvoOUyhrUNuWBlZfff6gU54RZoi7uHBhR41kiTRy7BHFt1GdTcnA2dnYbqaYd9LTa0OHYJ1WoBeGCKOw9+SmFn+sKfgjT6soq5fA68EGlDgtaev6poBO4uf6AxTFgh0PB0T97NoGQUBIRwEscL41y/It0vWBwyYBNZUQ2yhW4WDrEMF69rOQiG73f9L1IL1AMl2KLW8SCNBN+9tmQVv+lgpnrhdNFVG8r1RMk5vYJaDaLGt3n26xlFVbUo99ac57yR/EHrD4LEzJCXD/BeqbYcRKHfX0pJT/1r34ul4NE3YKjixi7y2rbjfnaWdIpOwnrRlO2vA1VVvuUSfy6HnDxI3JEzTgtpPFsahj2L9ujFf7dAjjqaVp92U4/mWzsiBLDrQNSZh7cOQq4d/28jZD1NeD18nE4ZuoSOeSAZ6w7MyxlaeABM5ptiN2IQZwp9rqYGNw"
bos_host = "bj.bcebos.com"
bucket_name = "wenku-ai-flower"
# #配置BceClientConfiguration
config = BceClientConfiguration(credentials=BceCredentials(sts_ak, sts_sk), endpoint = bos_host, security_token=token)



bos_client = BosClient(config)

exists = bos_client.does_bucket_exist(bucket_name)
# 输出结果
if exists:
    print("Bucket exists")
else:
    print("Bucket not exists")

# # 上传、读取文件
try:
    res = bos_client.put_object_from_string(bucket_name, "1.txt", "11U")
except Exception as e:
    print(e)