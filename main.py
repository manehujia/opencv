import cv2
import numpy as np

# 读取图像并进行错误处理
image_path = 'path_to_image.jpeg'
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"未找到指定路径的图像文件：{image_path}。请检查路径。")

try:
    # 将BGR图像转换为HSV图像
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 设置黑色的HSV阈值范围
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    # 创建掩码并应用掩码
    mask = cv2.inRange(hsv, lower_black, upper_black)#创建一个二值化的掩码，将黑色区域设置为1，其他区域设置为0
    result = cv2.bitwise_and(image, image, mask=mask)#将原图像与掩码进行位运算，得到黑色区域变黑色，其他区域保持原色

    # 查找并绘制轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:  # 仅在存在轮廓时绘制
        cv2.drawContours(image, contours, -1, (0, 255, 0), 1)

    # 显示结果
    cv2.imshow('Original Image', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
finally:
    cv2.destroyAllWindows()  # 确保窗口总是被关闭
