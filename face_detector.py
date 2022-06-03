import dlib
import cv2
import os

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

detector = dlib.get_frontal_face_detector() 
path ="D:/project/Personal_Model/downloads/"
name = ['소녀시대 윤아','송혜교','이다인','오마이걸 효정','여자아이들 우기','아이유','수지','레드벨벳 조이','원더걸스 유빈','소녀시대 제시카',
     '손예진','김연아','아이브 장원영','트와이스 다현','레드벨벳 아이린','소녀시대 티파니','우주소녀 설아','이영애','트와이스 채영','트와이스 나연',
     '김고은','김태리','전지현','손예진','태연','이성경','블랙핑크 제니','신세경','스테파니 리','캣 데닝스','한예슬','아이즈원 김민주','레드벨벳 예리',
     '세븐틴 버논','bts 뷔','김유정','현아','김효진','이효리','이민정','선미','청하','여자친구 은하','트와이스 미나','김옥빈','김혜수','문근영','선우선','앤 헤서웨이','강동원']
for j in range(len(name)):
    path2 = path+name[j]+"/"
    os.chdir(path2)
    files = os.listdir(path2)
    jpg_img = [] #숫자
    jpg = []  #이름
    for file in files:
        if '.jpg' in file: 
            f = cv2.imread(file)
            jpg_img.append(f)
            jpg.append(file)
    # img = cv2.imread("input2.jpg")

    for i in range(len(jpg_img)):
        faces = detector(jpg_img[i])
        print("{} faces are detected.".format(len(faces)))
        for face in faces:
            print("left, top, right, bottom : ",face.left(), face.top(), face.right(), face.bottom())
            cv2.rectangle(jpg_img[i],(face.left(), face.top()), (face.right(), face.bottom()), (0,0,255),2)
                
        win = dlib.image_window()
        win.set_image(jpg_img[i])
        win.add_overlay(faces)
            #얼굴인식한 output 저장
            # cv2.imwrite("output2.jpg",i)

            #얼굴 부분만 따로 저장
            
            # path = 'D:/project/Personal_Model/김고은_moder'
            # img_name = j
            # full_path = path + '/' +img_name
                
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)retval, buffer = cv2.imencode('.bmp', dst)
        #이미지 파일 저장
        #이미지 파일 처리 - 좌우 flip
            
        crop = jpg_img[i][face.top():face.bottom(),face.left():face.right()]
        imwrite("D:/project/Personal_Model/crop/"+name[j]+str(i)+".jpg",crop)

# import dlib
# import cv2


# detector = dlib.get_frontal_face_detector() 
# img = cv2.imread("input2.jpg")
# faces = detector(img)

# print("{} faces are detected.".format(len(faces)))
# for face in faces:
#     print("left, top, right, bottom : ",face.left(), face.top(), face.right(), face.bottom())
#     cv2.rectangle(img,(face.left(), face.top()), (face.right(), face.bottom()), (0,0,255),2)
    
# win = dlib.image_window()
# win.set_image(img)
# win.add_overlay(faces)
# #얼굴인식한 output 저장
# cv2.imwrite("output2.jpg",img)

# #얼굴 부분만 따로 저장
# crop = img[face.top():face.bottom(),face.left():face.right()]
# cv2.imwrite("cropped2.jpg",crop)