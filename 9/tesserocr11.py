from PIL import Image,ImageEnhance
import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr

# image = Image.open('g5fp.jpg')
# #print(image)
# imgry = image.convert('L')  # 图像加强，二值化
# #print(imgry)
# img_black_white = imgry.point(lambda x: 0 if x > 200 else 255)
# sharpness = ImageEnhance.Contrast(img_black_white)  # 对比度增强
# sharp_img = sharpness.enhance(2.0)
# print(tesserocr.image_to_text(sharp_img))

# print(tesserocr.file_to_text('https://xin.baidu.com/check/getCapImg?t=1560935653342'))


# def judge(pixl):
#     THRESHOLD = 80
#     if pixl>THRESHOLD:
#         return 1
#     else:
#         return 0
# def depoint(img):
#     """传入二值化后的图片进行降噪"""
#     pixdata = img.load()
#     w,h = img.size
#     for y in range(1,h-1):
#         for x in range(1,w-1):
#             count = 0
#             if judge(pixdata[x,y-1]):#上
#                 count = count + 1
#             if judge(pixdata[x,y+1]):#下
#                 count = count + 1
#             if judge(pixdata[x-1,y]):#左
#                 count = count + 1
#             if judge(pixdata[x+1,y]):#右
#                 count = count + 1
#             if judge(pixdata[x-1,y-1]):#左上
#                 count = count + 1
#             if judge(pixdata[x-1,y+1]):#左下
#                 count = count + 1
#             if judge(pixdata[x+1,y-1]):#右上
#                 count = count + 1
#             if judge(pixdata[x+1,y+1]):#右下
#                 count = count + 1
#             if count > 4:
#                 pixdata[x,y] = 255
#     return img
# def heibaihua(img):
#     # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
#     Img = img.convert('L')
#     # 黑白化处理，自定义灰度界限，大于这个值为黑色，小于这个值为白色
#     threshold = 200
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     # 图片二值化
#     photo = Img.point(table, '1')
#     photo.save("baocun.jpg")
#     return photo
# img= Image.open("CheckCode.png")  # 这里就相当于将图片数字化。
# img = heibaihua(img)
# img = depoint(img)
# img.show()
# ans=tesserocr.image_to_text(img)
# print(1111111111,ans)



image=Image.open('g5fp.jpg')
image=image.convert("L")
threshold=136
table=[]
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()
print(tesserocr.image_to_text(image))