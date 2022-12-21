import os
from inference_metrics import compute
import torch
import time
import torchvision.transforms as T
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import time
import torch
import numpy as np


os.environ['CUDA_VISIBLE_DEVICES'] = "0"
transform = T.Compose([T.ToTensor(),
                T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

device = torch.device('cuda')
image_size = 448
model_path = "../weighs"

def init_env(model_type):
    global model
    global gallery_feats
    global gallery_pids
    if(model_type == 'resnetst'):
        model_path = os.path.join("./weighs", "resnest26d_448_2048512_map751rank96_jit.pth")
        model = torch.jit.load(model_path)
    gallery_feats = np.load(os.path.join("./weighs", "feature_gallery"))
    gallery_pids = np.load(os.path.join("./weighs", "labels_gallery"))
    return True


def inference_single(probe_image_obj):
    probe_image = Image.open(probe_image_obj.stream)
    probe_image = cv2.cvtColor(np.asarray(probe_image),cv2.COLOR_RGB2BGR)
    image = cv2.resize(probe_image, (image_size,image_size), cv2.INTER_CUBIC)
    image = transform(image).unsqueeze(dim=0)
    cuda_image = image.to(device)
    with torch.no_grad():
        query_feat = model(cuda_image)
    indices = compute(query_feat.cpu(), gallery_feats, gallery_pids)
    res_pids = gallery_pids[indices[:5]]
    return res_pids