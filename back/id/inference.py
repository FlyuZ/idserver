import os
import torchvision.transforms as T
import cv2
from PIL import Image
import torch
import numpy as np


os.environ["CUDA_VISIBLE_DEVICES"] = "1"
IMAGE_SIZE = 448
PATH = os.path.dirname(os.path.abspath("."))
WEIGHTS_PATH = os.path.join(PATH, "weights")
MODEL_PATH = os.path.join(WEIGHTS_PATH, "resnest26d_448_map751rank96_jit.pth")


device = torch.device("cuda")

def euclidean_distance(qf, gf):
    m = qf.shape[0]
    n = gf.shape[0]
    dist_mat = torch.pow(qf, 2).sum(dim=1, keepdim=True).expand(m, n) + \
               torch.pow(gf, 2).sum(dim=1, keepdim=True).expand(n, m).t()
    dist_mat.addmm_(qf, gf.t(),  beta=1, alpha=-2)
    return dist_mat.cpu().numpy()


def compute(query_feat, gallery_feats):
    gallery_feats = torch.nn.functional.normalize(gallery_feats, dim=1, p=2)
    query_feat = torch.nn.functional.normalize(query_feat, dim=1, p=2)
    print('=> Computing DistMat with euclidean_distance')
    distmat = euclidean_distance(query_feat, gallery_feats)
    distmat = np.squeeze(distmat)
    indices = np.argsort(distmat)
    return indices

def init_env():
    global model
    global gallery_feats
    global gallery_pids
    model = torch.jit.load(MODEL_PATH)
    gallery_feats = np.load(os.path.join(WEIGHTS_PATH, "feature_gallery.npy"))
    gallery_pids = np.load(os.path.join(WEIGHTS_PATH, "labels_gallery.npy"))


def inference_single(probe_image_obj):
    probe_image = Image.open(probe_image_obj.stream)
    probe_image = cv2.cvtColor(np.asarray(probe_image), cv2.COLOR_RGB2BGR)
    image = cv2.resize(probe_image, (IMAGE_SIZE, IMAGE_SIZE), cv2.INTER_CUBIC)
    transform = T.Compose(
        [
            T.ToTensor(),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    image = transform(image).unsqueeze(dim=0)
    cuda_image = image.to(device)
    print("begin")
    with torch.no_grad():
        query_feat = model(cuda_image)
    indices = compute(query_feat.cpu(), torch.Tensor(gallery_feats))
    res_pids = gallery_pids[indices[:5]]
    print(res_pids)
    return res_pids
