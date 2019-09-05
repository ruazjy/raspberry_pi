import SimpleITK as sitk


# 目的是测试在经过窗宽窗位调整之后将图像保存为nii,
# 查看nii图像是否符合预期效果
# input_path = r'F:\pycharm_file\zjy_raspberry_pi\learn_window_wise\test_dicom\.....'
# output_path = r'F:\pycharm_file\zjy_raspberry_pi\learn_window_wise\output.nii.gz'
# image = sitk.ReadImage(input_path)
# image_np = sitk.GetArrayFromImage(image)
# print(image_np.shape)
# sitk.WriteImage(image, output_path)

input_path = r'F:\pycharm_file\zjy_raspberry_pi\learn_window_wise\test_dicom'
image_reader = sitk.ImageSeriesReader()
image_reader.MetaDataDictionaryArrayUpdateOn()
image_reader.LoadPrivateTagsOn()
dicom_file_path = image_reader.GetGDCMSeriesFileNames(input_path)
image_reader.SetFileNames(dicom_file_path)
image = image_reader.Execute()


print(dicom_file_path)
# 我需要知道这个slice_number是从1开始还是从0开始
if image_reader.HasMetaDataKey(0, '0010|0010'):
    name = image_reader.GetMetaData(0, '0010|0010')
print(name)

window_center_key = '0028|1050'
window_width_key = '0028|1051'
# rescale 重新调节
# intercept 截距
rescale_intercept_key = '0028|1052'
# slope 斜率
rescale_slope_key = '0028|1053'

window_center = image_reader.GetMetaData(0, window_center_key)
window_width = image_reader.GetMetaData(0, window_width_key)

# 如果文件头不存在，默认为0 一个if/else搞定
rescale_intercept = image_reader.GetMetaData(0, rescale_intercept_key)

# 如果文件头不存在，默认为1
rescale_slope = image_reader.GetMetaData(0, rescale_slope_key)

# print(window_center)
# print(window_width)
# print(rescale_intercept)
# print(rescale_slope)

std_window_center = (float(window_center) - float(rescale_intercept)) / float(rescale_slope)
std_window_width = float(window_width) / float(rescale_slope)

std_window_ceil = std_window_center + std_window_width//2
std_window_floor = std_window_center - std_window_width//2

# print(std_window_center)
# print(std_window_width)

image_np = sitk.GetArrayFromImage(image)
std_image_np = (image_np - float(rescale_intercept)) / float(rescale_slope)
std_image_np[std_image_np > std_window_ceil] = std_window_ceil
std_image_np[std_image_np < std_window_floor] = std_window_floor

std_image = sitk.GetImageFromArray(std_image_np)


output_path = r'F:\pycharm_file\zjy_raspberry_pi\learn_window_wise\output.nii.gz'
sitk.WriteImage(std_image, output_path)

print(std_image_np.min(), std_window_center - std_window_width//2)
print(std_image_np.max(), std_window_center + std_window_width//2)


# 现在框架内部的窗宽窗位去除掉了归一化处理，仅保留ceil floor之间的信息
# 该脚本内的处理方式同样如此


