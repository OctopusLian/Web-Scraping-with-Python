from PIL import Image
import subprocess
def cleanFile(filePath, newFilePath):
image = Image.open(filePath)
# 对图片进行阈值过滤，然后保存
image = image.point(lambda x: 0 if x<143 else 255)
image.save(newFilePath)
# 调用系统的tesseract命令对图片进行OCR识别
subprocess.call(["tesseract", newFilePath, "output"])
# 打开文件读取结果
outputFile = open("output.txt", 'r')
print(outputFile.read())
outputFile.close()
cleanFile("text_2.jpg", "text_2_clean.png")
