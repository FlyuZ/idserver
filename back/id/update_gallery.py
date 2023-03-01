
import os 
import json
import os
from gallary_loader import make_dataloader
import torch
import numpy as np

PATH = os.path.dirname(os.path.abspath("."))
GALLERY_PATH = os.path.join(PATH, "gallery")
GALLERY_JSON_PATH = os.path.join(PATH, "galleryid.json")
WEIGHTS_PATH = os.path.join(PATH, "weights")
MODEL_PATH = os.path.join(WEIGHTS_PATH, "resnest26d_448_map751rank96_jit.pth")


def update_gallery_info():
    gallerydir = os.listdir(GALLERY_PATH)
    idinfodict = []
    galleryinfodict = []
    for galleryid in gallerydir:
        curidlist =  os.listdir(os.path.join(GALLERY_PATH, galleryid))
        #  后续可通过建议数据库 实现 羊圈和ID的对应关系
        galleryinfodict.append({'gallery': galleryid, 'name': '环庆养殖场'})
        for curid in curidlist:
            curid = curid.split('.')[0]
            curiddict = {'gallery': galleryid, 'id' : curid, 'info': ' '}
            idinfodict.append(curiddict)
    gallery_json = json.dumps(idinfodict)

    with open(GALLERY_JSON_PATH, 'w') as f:
        json.dump(gallery_json, f)
    
    # 返回给前端的数据
    return idinfodict, galleryinfodict

def load_gallery():
    with open(GALLERY_JSON_PATH, 'r') as f:
        gallery_json = json.load(f)
    gallerydict = json.loads(gallery_json)
    return gallerydict

def get_gallery_feats(model, gallerydataset):
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

def update_gallery_feature():
    model = torch.jit.load(MODEL_PATH)
    gallerydataset = make_dataloader(GALLERY_PATH)
    print("load gallery feature")
    gallery_feats, gallery_pids, gallery_paths = get_gallery_feats(model, gallerydataset)
    np.save(os.path.join(WEIGHTS_PATH, 'feature_gallery'), gallery_feats.numpy())
    np.save(os.path.join(WEIGHTS_PATH, 'labels_gallery'), gallery_pids)


# if __name__ == "__main__":
#     update_gallery()
#     # load_gallery()