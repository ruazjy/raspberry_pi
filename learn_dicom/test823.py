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
        temp.append(coordinate_element * spacing_element)
    four_apex_list_after.append(temp)

print(four_apex_list_after)

# 绝对坐标系中的值
# 先用列表进行计算，不过感觉需要使用np优化

# 对比绝对坐标系，图像的坐标系的平移距离
move_vector = xy_coordinate
four_apex_list_last = []
for apex_coordinate in four_apex_list_after:
    temp = []
    for i, j in zip(apex_coordinate, xy_coordinate):
        temp.append(i + j)
    four_apex_list_last.append(temp)
print(four_apex_list_last)


# 把上述功能简化成一个函数，输入图片的路径，自动输出四个端点上绝对坐标系的值
def coordinate_transform(input_path):
    """
    输入单张dicom的路径，输出该dicom图像四个端点在绝对坐标系下的端点
    :param input_path:
    :return:
    """
    # series_uid = '0020|000e'
    # series_desc = '0008|103e'
    image_position = '0020|0032'
    # image_orientation = '0020|0037'暂时忽略角度
    pixel_spacing = '0028|0030'
    # slice_thickness = '0018|0050'
    rows = '0028|0010'
    columns = '0028|0011'
    reader = sitk.ImageFileReader()
    # 经过检验，该方法与文件名后缀无关，都能提取到头信息
    reader.SetFileName(input_path)
    reader.LoadPrivateTagsOn()
    reader.ReadImageInformation()
    position = reader.GetMetaData(image_position)
    # orientation = reader.GetMetaData(image_orientation)
    spacing = reader.GetMetaData(pixel_spacing)
    # thickness = reader.GetMetaData(slice_thickness)
    w = reader.GetMetaData(rows)
    h = reader.GetMetaData(columns)

    xy_coordinate = []
    xy_coordinate.append(float(position.split('\\')[0]))
    xy_coordinate.append(float(position.split('\\')[1]))

    pixel_spacing_list = [float(x) for x in spacing.split('\\')]
    # todo:修改坐标映射关系
    # four_apex_list_before = [[0, 0], [int(w), 0], [0, -int(h)], [int(w), -int(h)]]
    # 在这种坐标状态下，该坐标系的y轴方向是向下的
    # 这样的坐标
    four_apex_list_before = [[0, 0], [int(w), 0], [0, int(h)], [int(w), int(h)]]
    four_apex_list_after = []
    # four_apex_list_mm
    for i in range(len(four_apex_list_before)):
        temp = []
        for coordinate_element, spacing_element in zip(four_apex_list_before[i], pixel_spacing_list):
            temp.append(coordinate_element * spacing_element)
        four_apex_list_after.append(temp)

    # move_vector = xy_coordinate
    four_apex_list_last = []
    for apex_coordinate in four_apex_list_after:
        temp = []
        # for i, j in zip(apex_coordinate, xy_coordinate):
        #     temp.append(i + j)
        for i in range(2):
            # if i == 0:
            temp.append(apex_coordinate[i] + xy_coordinate[i])
            # elif i == 1:
            #     temp.append(apex_coordinate[i] + xy_coordinate[i])
        four_apex_list_last.append(temp)
    return four_apex_list_last


if __name__ == '__main__':
    image_input_dir_path = r'C:\Users\zzz\Desktop\dicom_for_test\single_layer'
    # # adc_input_path = os.path.join(image_input_dir_path, 'adc', 'IMG-0002-00001.dcm')
    # adc_input_path = os.path.join(image_input_dir_path, 'adc_img', 'IMG-0002-00001.img')
    # t2_input_path = os.path.join(image_input_dir_path, 't2', 'IMG-0004-00001.dcm')
    adc_input_path = os.path.join(image_input_dir_path, 'adc', 'IMG-0002-00001.dcm')
    t2_input_path = os.path.join(image_input_dir_path, 't2', 'IMG-0004-00001.dcm')
    adc_coordinate = coordinate_transform(adc_input_path)
    t2_coordinate = coordinate_transform(t2_input_path)

    print('adc:', adc_coordinate)
    print('t2:', t2_coordinate)

# 一个插值方法的选择
# 选取四个点来标定对照区域，切割后进行缩放，即可作为adc的label进行使用
# 但是要明确插值方法，选取一个合适的插值至关重要
# 可能需要框架进行配合调整，读取图像的某些特定键值对

# 由该函数得出的结论与实际不符，所以坐标的相对位置概念需要进行修正
# todo:一个是从series中提取到初始图层的position
# todo:缩放的对应，根据产生打的坐标生成一个图像截取和缩放的比例
# todo:实验opencv图像缩放后的效果


# todo:周报
