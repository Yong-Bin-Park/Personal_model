import cv2
import os
import numpy as np

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None
    
name = ['블랙핑크 제니','신세경','스테파니 리','캣 데닝스','한예슬','아이즈원 김민주','레드벨벳 예리',
     '세븐틴 버논','bts 뷔','김유정','현아','김효진','이효리','이민정','선미','청하','여자친구 은하','트와이스 미나','김옥빈','김혜수','문근영','선우선','앤 헤서웨이','강동원']

path ="D:/project/Personal_Model/crop/"
for j in range(len(name)):
    os.mkdir("D:/project/Personal_Model/skin/"+name[j])
    path2 = path+name[j]+"/"
    os.chdir(path2)
    files = os.listdir(path2)
    jpg_img = [] #숫자
    jpg = []  #이름
    for file in files:
        if '.jpg' in file: 
            f = imread(file)
            jpg_img.append(f)
            jpg.append(file)
    for i in range(len(jpg_img)):
        # face_img = cv2.imread("cropped2.jpg")
        face_img_ycrcb = cv2.cvtColor(jpg_img[i], cv2.COLOR_BGR2YCrCb)

        #YCbCr Color Space내에서 사람의 피부는 (0,133,77) ~ (255,173,127) 영역 내에 존재
        lower = np.array([0,133,77], dtype = np.uint8)
        upper = np.array([255,173,127], dtype = np.uint8)
        #inRange함수는 특정 이미지 데이터의 상/하한선을 정해놓고 
        # 그 안에 들어오는 pixel들은 1 나머지는 0으로 만드는 함수
        skin_msk = cv2.inRange(face_img_ycrcb, lower, upper)

        skin = cv2.bitwise_and(jpg_img[i], jpg_img[i], mask = skin_msk)
        imwrite("D:/project/Personal_Model/skin/"+name[j]+"/"+name[j]+str(i)+".jpg",skin)


# import cv2
# import numpy as np

# face_img = cv2.imread("cropped2.jpg")
# face_img_ycrcb = cv2.cvtColor(face_img, cv2.COLOR_BGR2YCrCb)

# #YCbCr Color Space내에서 사람의 피부는 (0,133,77) ~ (255,173,127) 영역 내에 존재
# lower = np.array([0,133,77], dtype = np.uint8)
# upper = np.array([255,173,127], dtype = np.uint8)
# #inRange함수는 특정 이미지 데이터의 상/하한선을 정해놓고 
# # 그 안에 들어오는 pixel들은 1 나머지는 0으로 만드는 함수
# skin_msk = cv2.inRange(face_img_ycrcb, lower, upper)
# #필터 씌우기
# skin = cv2.bitwise_and(face_img, face_img, mask = skin_msk)
# cv2.imwrite("skin2.jpg",skin)