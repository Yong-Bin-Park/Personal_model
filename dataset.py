from ast import increment_lineno
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import torchvision
from torchvision import transforms


trans = transforms.Compose([transforms.Resize((100,100)),
                            transforms.ToTensor(),
                            transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
                            ])
trainset = torchvision.datasets.ImageFolder(root = "C:/Users/dydql/Personal_model/personal",
                                            transform = trans)

# print(trainset.__getitem__(18))

classes = trainset.classes
# print(classes)

trainloader = DataLoader(trainset,
                         batch_size = 16,
                         shuffle = False,
                         num_workers = 0)

dataiter = iter(trainloader)
images, labels = dataiter.next()
# print(labels)

#무작위로 샘플 추출
np.random.seed(1234)
index_list = np.arange(0, len(labels))
valid_index = np.random.choice(index_list, size = 16, replace = False)

#검증셋 추출
valid_images = images[valid_index]
valid_labels = labels[valid_index]

#학습셋에서 검증셋 제외
train_index = set(index_list) - set(valid_index)
images = images[list(train_index)]
labels = labels[list(train_index)]
