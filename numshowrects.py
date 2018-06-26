import cv2
im=cv2.imread("flawdetection.PNG")

# 讀取圖檔
#im = cv2.imread('image.jpg')

# 建立 Selective Search 分割器
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

# 設定要進行分割的圖形
ss.setBaseImage(im)

# 使用快速模式（精準度較差）
ss.switchToSelectiveSearchFast()

# 使用精準模式（速度較慢）
# ss.switchToSelectiveSearchQuality()

# 執行 Selective Search 分割
rects = ss.process()

print('候選區域總數量： {}'.format(len(rects)))

# 要顯示的候選區域數量
numShowRects = 100

# 每次增加或減少顯示的候選區域數量
increment = 50

while True:
  # 複製一份原始影像
  imOut = im.copy()

  # 以迴圈處理每一個候選區域
  for i, rect in enumerate(rects):
      # 以方框標示候選區域
      if (i < numShowRects):
          x, y, w, h = rect
          cv2.rectangle(imOut, (x, y), (x+w, y+h), (0, 255, 0), 1, cv2.LINE_AA)
      else:
          break

  # 顯示結果
  cv2.imshow("Output", imOut)

  # 讀取使用者所按下的鍵
  k = cv2.waitKey(0) & 0xFF

  # 若按下 m 鍵，則增加 numShowRects
  if k == 109:
      numShowRects += increment
  # 若按下 l 鍵，則減少 numShowRects
  elif k == 108 and numShowRects > increment:
      numShowRects -= increment
  # 若按下 q 鍵，則離開
  elif k == 113:
      break

# 關閉圖形顯示視窗
cv2.destroyAllWindows()
