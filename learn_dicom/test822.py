import SimpleITK as sitk
import numpy as np
import os

image_input_dir_path = r'C:\Users\zzz\Desktop\dicom_for_test\single_layer'
# adc_input_path = os.path.join(image_input_dir_path, 'adc', 'IMG-0002-00001.dcm')
adc_input_path = os.path.join(image_input_dir_path, 'adc_img', 'IMG-0002-00001.img')
t2_input_path = os.path.join(image_input_dir_path, 't2', 'IMG-0004-00001.dcm')

# adc_image = sitk.ReadImage(adc_input_path)
# t2_image = sitk.ReadImage(t2_input_path)
#
# adc_image_np = sitk.GetArrayFromImage(adc_image)
# t2_image_np = sitk.GetArrayFromImage(t2_image)
#
# print(adc_image_np.shape)
# print(t2_image_np.shape)

adc_reader = sitk.ImageSeriesReader()
# t2_reader = sitk.ImageSeriesReader()

series_uid = '0020|000e'
series_desc = '0008|103e'
image_position = '0020|0032'
image_orientation = '0020|0037'
pixel_spacing = '0028|0030'
slice_thickness = '0018|0050'
rows = '0028|0010'
columns = '0028|0011'

reader = sitk.ImageFileReader()
# 经过检验，该方法与文件名后缀无关，都能提取到头信息
reader.SetFileName(adc_input_path)
reader.LoadPrivateTagsOn()
reader.ReadImageInformation()
image_desc = reader.GetMetaData(series_desc)
position = reader.GetMetaData(image_position)
orientation = reader.GetMetaData(image_orientation)
spacing = reader.GetMetaData(pixel_spacing)
thickness = reader.GetMetaData(slice_thickness)
w = reader.GetMetaData(rows)
h = reader.GetMetaData(columns)

print(image_desc)
print(position)
print(orientation)
print(spacing)
print(thickness)
print(w)
print(type(w))
print(h)

# 存储xy毫米坐标
xy_coordinate = []
xy_coordinate.append(float(position.split('\\')[0]))
xy_coordinate.append(float(position.split('\\')[1]))
print(xy_coordinate)

# 存储每个像素毫米单位
# pixel_spacing_list = []
# pixel_spacing_list.append(float(spacing.split('\\')[0]))
# pixel_spacing_list.append(float(spacing.split('\\')[1]))
pixel_spacing_list = [float(x) for x in spacing.split('\\')]
print(pixel_spacing_list)

# 忽略旋转角度问题， 将像素点四个角的坐标转化为绝对坐标系下的坐标
# 先计算出该图像的四个顶点
w_len = int(w) * pixel_spacing_list[0]
h_len = int(w) * pixel_spacing_list[1]

# four_apex_list = []
# four_apex_list.append(xy_coordinate)
# four_apex_list.append([xy_coordinate[0] + w_len, xy_coordinate[1]])
# four_apex_list.append([xy_coordinate[0] + w_len, xy_coordinate[1] - h_len])
# four_apex_list.append([xy_coordinate[0], xy_coordinate[1] - h_len])
# print(four_apex_list)

four_apex_list_before = [[0, 0], [256, 0], [0, -256], [256, -256]]
four_apex_list_after = []
# four_apex_list_mm
for i in range(len(four_apex_list_before)):
    temp = []
    for coordinate_element, spacing_element in zip(four_apex_list_before[i], pixel_spacing_list):
        temp.append(coordinate_element*spacing_element)
        four_apex_list_after.append(temp)

print(four_apex_list_after)

# 绝对坐标系中的值
# 先用列表进行计算，不过感觉需要使用np优化

