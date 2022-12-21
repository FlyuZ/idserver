import torch
import numpy as np
import os


def euclidean_distance(qf, gf):
    m = qf.shape[0]
    n = gf.shape[0]
    dist_mat = torch.pow(qf, 2).sum(dim=1, keepdim=True).expand(m, n) + \
               torch.pow(gf, 2).sum(dim=1, keepdim=True).expand(n, m).t()
    dist_mat.addmm_(qf, gf.t(),  beta=1, alpha=-2)
    return dist_mat.cpu().numpy()


def compute(query_feat, gallery_feats):
    print("The feature is normalized")
    gallery_feats = torch.nn.functional.normalize(gallery_feats, dim=1, p=2)
    query_feat = torch.nn.functional.normalize(query_feat, dim=1, p=2)
    print('=> Computing DistMat with euclidean_distance')
    distmat = euclidean_distance(query_feat, gallery_feats)
    distmat = np.squeeze(distmat)
    indices = np.argsort(distmat)
    return indices
