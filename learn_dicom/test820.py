import SimpleITK as sitk
import pandas as pd

# file_path = r'F:\dicom_for_test\A002082132\adc'
#
# # 这东西干啥用的
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
#
# reader = sitk.ImageSeriesReader()
# series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(file_path)
#
# nb_series = len(series_IDs)
# print(series_IDs)
# print(nb_series)
#
# series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(file_path, series_IDs[0])
# reader.SetFileNames(series_file_names)
# image3D = reader.Execute()

# date = sitk.GetArrayFromImage(image3D)
#
# print(image3D.GetSize())

# resample = sitk.ResampleImageFilter()
# resample.SetOutputDirection(image3D.GetDirection())
# resample.SetOutputOrigin(image3D.GetOrigin())
# newspacing = [1,1,1]
# resample.SetOutputSpacing(newspacing)
# newimage = resample.Execute(image3D)
# print('begin image to array')
# date1 = sitk.GetArrayFromImage(newimage)
# print(date1.shape)

a = [1,2]
b = [3,4]
temp = []
for a_element, b_element in zip(a,b):
    temp.append(a_element*b_element)
print(temp)


