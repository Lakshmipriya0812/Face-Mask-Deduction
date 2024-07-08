import torchvision
import numpy
import torch
import argparse
import cv2
import detect_utils
from PIL import Image

'''
parser.add_argument('-i', '--input', help='path to input image/video')
parser.add_argument('-m', '--min-size', dest='min_size', default=800, 
                    help='minimum input size for the FasterRCNN network')
'''
def predictuh():
    #path to image file
    a=""

    #minimum input size fot the model

    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True, 
                                                    min_size=800)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


    image = Image.open(a)
    model.eval().to(device)
    boxes, classes, labels = detect_utils.predict(image, model, device, 0.8)
    image = detect_utils.draw_boxes(boxes, classes, labels, image)
    cv2.imshow('Image', image)
    save_name = f"{args['input'].split('/')[-1].split('.')[0]}_{args['min_size']}"
    cv2.imwrite(f"outputs/{save_name}.jpg", image)
    cv2.waitKey(0)

