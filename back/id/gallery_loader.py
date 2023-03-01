# encoding: utf-8
"""
@author:  feifei97
"""
import glob
import torch
import os.path as osp
import os
from PIL import Image, ImageFile
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as T

ImageFile.LOAD_TRUNCATED_IMAGES = True

def read_image(img_path):
    """Keep reading image until succeed.
    This can avoid IOError incurred by heavy IO process."""
    got_img = False
    while not got_img:
        try:
            img = Image.open(img_path).convert('RGB')
            got_img = True
        except IOError:
            print("IOError incurred when reading '{}'. Will redo. Don't worry. Just chill.".format(img_path))
            pass
    return img

class ImageDataset(Dataset):
    def __init__(self, root='', transform=None):
        super(ImageDataset, self).__init__()
        self.transform = transform
        self.gallery_dir = root
        self.gallery, self.num_gallery_pids, self.num_gallery_imgs = self._process_dir(self.gallery_dir)
        
    def _process_dir(self, dir_path):
        all_label = os.listdir(dir_path)
        dataset = []
        cnt = 0
        for cur_label in all_label:
            img_paths = glob.glob(osp.join(dir_path, cur_label, '*.jpg'))
            for img_path in img_paths:
                    dataset.append((img_path, int(cur_label)))
                    cnt += 1
        return dataset, len(all_label), cnt
    
    def __len__(self):
        return len(self.gallery)

    def __getitem__(self, index):
        img_path, pid = self.gallery[index]
        img = read_image(img_path)
        if self.transform is not None:
            img = self.transform(img)
        return img, pid, img_path


def print_dataset_statistics(dataset):
    print("Gallery statistics:")
    print("  ----------------------------------------")
    print("gallery_pids: " + str(dataset.num_gallery_pids))
    print("gallery_imgs: " + str(dataset.num_gallery_imgs))
    print("  ----------------------------------------")

def val_collate_fn(batch):
    imgs, pids, img_paths = zip(*batch)
    return torch.stack(imgs, dim=0), pids, img_paths

def make_dataloader(data_root):
    gallery_transforms = T.Compose([
        T.Resize((448,448)),
        T.ToTensor(),
        T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    gallary_dataset = ImageDataset(root=data_root, transform=gallery_transforms)
    print_dataset_statistics(gallary_dataset)
    gallery_loader = DataLoader(
        gallary_dataset, batch_size=8, shuffle=False, num_workers=0, collate_fn=val_collate_fn
    )
    return gallery_loader

