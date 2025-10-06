# 代码生成时间: 2025-10-07 00:00:38
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, measure, morphology
import SimpleITK as sitk

"""
医学影像分析程序
该程序包含以下功能：
1. 读取DICOM影像文件
2. 图像平滑处理
3. 图像二值化处理
4. 图像去噪
5. 图像特征提取
6. 可视化结果
"""

class MedicalImageAnalysis:
    def __init__(self, image_path):
        """初始化函数"""
        self.image_path = image_path
        self.image = None
        self.filtered_image = None
        self.thresholded_image = None
        self.features = None

    def read_image(self):
        """读取DICOM影像文件"""
        try:
            self.image = sitk.ReadImage(self.image_path)
            self.image_array = sitk.GetArrayFromImage(self.image)
        except Exception as e:
            print(f"读取影像文件失败：{e}")
            raise

    def smooth_image(self, sigma=1):
        """图像平滑处理
        使用高斯滤波器进行图像平滑
        :param sigma: 高斯滤波器的标准差
        """
        self.filtered_image = filters.gaussian(self.image_array, sigma=sigma)

    def threshold_image(self, threshold=0.5):
        """图像二值化处理
        使用Otsu方法进行图像二值化
        :param threshold: 阈值
        """
        self.thresholded_image = filters.threshold_otsu(self.filtered_image)
        self.thresholded_image = self.filtered_image > self.thresholded_image

    def denoise_image(self):
        """图像去噪
        使用非局部均值去噪
        """
        self.filtered_image = filters.nl_means_denoising(self.image_array, patch_size=5, patch_distance=3, h=0.01)

    def extract_features(self):
        """图像特征提取
        提取图像的形态学特征
        """
        labeled_image = measure.label(self.thresholded_image)
        self.features = measure.regionprops(labeled_image)

    def visualize_results(self):
        """可视化结果
        显示原始图像、平滑图像、二值化图像和特征提取结果
        """
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        axes[0, 0].imshow(self.image_array, cmap='gray')
        axes[0, 0].set_title('Original Image')
        axes[0, 1].imshow(self.filtered_image, cmap='gray')
        axes[0, 1].set_title('Smoothed Image')
        axes[1, 0].imshow(self.thresholded_image, cmap='gray')
        axes[1, 0].set_title('Thresholded Image')
        for feature in self.features:
            axes[1, 1].plot(feature.centroid[0], feature.centroid[1], 'r.')
        axes[1, 1].set_title('Feature Extraction Results')
        plt.show()

# 示例用法
if __name__ == '__main__':
    image_path = 'path_to_your_dicom_image.dcm'
    mia = MedicalImageAnalysis(image_path)
    mia.read_image()
    mia.smooth_image(sigma=1)
    mia.threshold_image(threshold=0.5)
    mia.denoise_image()
    mia.extract_features()
    mia.visualize_results()
