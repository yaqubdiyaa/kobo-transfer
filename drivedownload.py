#1Uu2h0jxIJQLUCk6EZZ4xUu0WTaz64X-X

#so this currently works
#if you take entire 

#you would need to write your own code to make sure the output was in correct format
#but problem is how tf are you going to know if its an image... or a jpg or smth else
#you dont have that info rip




import gdown

url = "https://drive.google.com/drive/u/1/folders/149lRc_R6YBqqUCQEMuN_vmz36wqp5r1BiZolmcxGqDO4J5the7h_g_8xZ8Jvuz_50ugrnhcR"
#gdown.download_folder(url, quiet=True, use_cookies=False)

gdown.download(url="https://drive.google.com/file/d/1JDbqP7NKNz3seHwWhc9on8tYJAXavVjr", quiet=False, fuzzy=True)
#gdown.download(url = "https://drive.google.com/open?id=1Qn70Hda3npuSnGlwGindhggmWx2CNlbN", )
#url = 'https://drive.google.com/uc?id=1he1gkdCI0Kzi9KGrzgXkTwlt8Go5Hcfg'
#output = '20150428_collected_images.jpg'
#gdown.download(url, output, quiet=False)
