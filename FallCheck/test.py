from ultralytics import YOLO
import cv2
import os, datetime, time

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
path_pt = r"best.pt"
model = YOLO(path_pt)
img_dir = r"people(68).jpg"
image_files = [os.path.join(img_dir, file) for file in os.listdir(img_dir) if
               file.endswith((".jpg", "png", "jpeg", "mp4"))]
for img_file in image_files:
    mat_img = cv2.imread(img_file)
    res = model(img_file, save=True, conf=0.4, iou=0.2, imgsz=640, device="cuda:0")  # use cuda
    res_coord = []
    outputs = res[0]
    boxes = res[0].boxes  # include xyxy xywh xywhn
    boxes = boxes.xyxy
    boxes = boxes.cpu()  # cuda data transfer cpu data
    boxes = boxes.tolist()
    count = 0
    for box in boxes:
        count += 1
        width = int(box[2]) - int(box[0])
        height = int(box[3]) - int(box[1])
        x_center = (int(box[2]) + int(box[0])) // 2
        y_center = (int(box[3]) + int(box[1])) // 2
        res_coord.append((x_center, y_center))
        img = cv2.circle(mat_img, (x_center, y_center), 5, (0, 0, 255), -1)
    date_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
    path = ".res/" + date_time + ".jpg"
    cv2.imwrite(path, img)
    res.coord.append(path)  # include box(center) and the result path of img
