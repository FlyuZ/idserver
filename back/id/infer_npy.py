
import os
from gallaryLoader import make_dataloader
import torch
import torch
import numpy as np

def getGalleryFeats(model, gallerydataset):
    feats = []
    pids = []
    imgpaths = []
    device = torch.device('cuda')
    for n_iter, (img, pid, imgpath) in enumerate(gallerydataset):
        with torch.no_grad():
            img = img.to(device)
            feat = model(img)
            feats.append(feat.cpu())
            pids.extend(np.asarray(pid))
            imgpaths.extend(np.asarray(imgpath))
    feats = torch.cat(feats, dim=0)
    return feats, pids, imgpaths

if __name__ == "__main__":
    print("load model")
    model_path = os.path.join("../weighs", "")
    model = torch.jit.load(model_path)
    gallerydataset = make_dataloader("./gallery")
    print("load gallery feature")
    gallery_feats, gallery_pids, gallery_paths = getGalleryFeats(model, gallerydataset)
    np.save('./weights/feature_gallery',gallery_feats.numpy())
    np.save('./weights/labels_gallery',gallery_pids)