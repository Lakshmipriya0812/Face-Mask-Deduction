import torchvision
import numpy
import torch
import argparse
import cv2
import detect_utils
from PIL import Image
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchsummary import summary


'''
parser.add_argument('-i', '--input', help='path to input image/video')
parser.add_argument('-m', '--min-size', dest='min_size', default=800, 
                    help='minimum input size for the FasterRCNN network')
'''



def get_model_instance_segmentation(num_classes):
    # load an instance segmentation model pre-trained pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

    return model




def detectuh(a="C:/Users/srisharaan/Desktop/face mask/two.jpeg"):
    model = get_model_instance_segmentation(4)
    params = [p for p in model.parameters() if p.requires_grad]
    #print(summary(model))
    optimizer = torch.optim.SGD(params, lr=0.005,
                                momentum=0.9, weight_decay=0.0005)


    checkpoint = torch.load("D:/face/model20.pt",map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']




    #model = TheModelClass(*args, **kwargs)
    #model.load_state_dict(torch.load("C:/Users/srisharaan/Desktop/face mask/model.pt",map_location=torch.device('cpu')))
    #model.eval()

    #path to image file
    

    #minimum input size fot the model

    #model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True, min_size=800)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


    image = Image.open(a)
    model.eval().to(device)
    boxes, classes, labels = detect_utils.predict(image, model, device, 0.8)
    image = detect_utils.draw_boxes(boxes, classes, labels, image)
    cv2.imshow('Image', image)
    #save_name = f"{args['input'].split('/')[-1].split('.')[0]}_{800}"
    cv2.imwrite(f"outputs/save_name.jpg", image)
    cv2.waitKey(0)

#detectuh()
