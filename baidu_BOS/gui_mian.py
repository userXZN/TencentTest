import tkinter as tk
import sys
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.services.bos.bos_client import BosClient

root = tk.Tk()
root.title("BOS简易上传检测")
#root['height'] = 1000
#root['width'] = 800
root.geometry("1000x500")

var1 = tk.StringVar()
label1 = tk.Label(root, text="ak")
label1.grid(row=0)
entry1 = tk.Entry(width=100)
entry1.grid(row=0,column=1,sticky="W")

var2 = tk.StringVar()
label2 = tk.Label(root, text="sk")
label2.grid(row=1)
entry2 = tk.Entry(width=100)
entry2.grid(row=1,column=1,sticky="W")

var3 = tk.StringVar()
label3 = tk.Label(root, text="token")
label3.grid(row=2)
entry3 = tk.Entry(width=100)
entry3.grid(row=2,column=1,sticky="W")

var4 = tk.StringVar()
label4 = tk.Label(root, text="bos_host")
label4.grid(row=3,sticky="W")
entry4 = tk.Entry(width=100)
entry4.grid(row=3,column=1,sticky="W")

var5 = tk.StringVar()
label5 = tk.Label(root, text="bucket_name")
label5.grid(row=4,sticky="W")
entry5 = tk.Entry(width=100)
entry5.grid(row=4,column=1,sticky="W")

var6 = tk.StringVar()
label6 = tk.Label(root, text="输出:")
label6.grid(row=6,sticky="W")

label7 = tk.Label(root,text='')
label7.grid(row=7,column=1,sticky="W")

label8 = tk.Label(root,text='')
label8.grid(row=8,column=1,sticky="N")

def clickFun():

    sts_ak = entry1.get()
    sts_sk = entry2.get()
    token = entry3.get()
    bos_host = entry4.get()
    bucket_name = entry5.get()

    # #配置BceClientConfiguration

    config = BceClientConfiguration(credentials=BceCredentials(sts_ak, sts_sk), endpoint=bos_host, security_token=token)

    bos_client = BosClient(config)

    # # 上传、读取文件
    try:
        exists = bos_client.does_bucket_exist(bucket_name)
        # 输出结果
        if exists:
            label7['text'] = "Bucket exists"
        else:
            label7['text'] = "Bucket not exists"
        res = bos_client.put_object_from_string(bucket_name, "1.txt", "11U")
    except Exception as e:
        label8['text'] = str(e).splitlines ()[-1]

    else:
        result = res.__dict__
        if result['metadata']:
            label8['text'] = str(result['metadata']).replace(',',',\n')


button1 = tk.Button(root, text="Aute", width=10, height=2, command=clickFun)
button1.grid(row=5,column=1)
root.mainloop()