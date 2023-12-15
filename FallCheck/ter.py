from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

if __name__ == '__main__':
    data = r"D:\FallCheck\ultralytics\cfg\datasets\da.yaml"
    # 训练模型
    model.train(data=data, epochs=100)  # 训练模型，训练100个周期
    # 评估模型性能
    metrics = model.val()  # 在验证集上评估模型性能
    # 对图像进行预测
    results = model(r"C:\Users\Administrator\Desktop\people(120).jpg")
    # 导出模型为ONNX格式
    path = model.export(format="onnx")  # 导出模型为ONNX格式
