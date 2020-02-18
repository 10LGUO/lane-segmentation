import os
import pandas as pd
from sklearn.utils import shuffle

label_list = []
image_list = []

image_dir = "xxx"
label_dir = "yyy"

for s1 in os.listdir(image_dir):
    image_sub1 = os.path.join(image_dir, s1)
    image_sub2 = os.path.join(label_dir, 'Label_' + str.lower(s1), 'Label')
    for s2 in os.listdir(image_sub1):
        image_sub2 = os.path.join(image_sub1, s2)
        label_sub2 = os.path.join(label_sub2, s2)
        for s3 in os.listdir(image_sub2):
            image_sub3 = os.path.join(image_sub2, s3)
            label_sub3 = os.path.join(label_sub2, s3)
            for s4 in os.listdir(image_sub3):
                image_sub4 = os.path.join(image_sub3, s4)
                new_s4 = s4.replace('.jpg','_bin.jpg')
                label_sub4 = os.path.join(label_sub3, new_s4)
                if not os.path.exists(label_sub4): # avoid error caused by damaged data
                    print(label_sub4)
                label_list.append(label_sub4)
                image_list.append(image_sub4)

assert len(image_list) == len(label_list)
print("the length of imagelist {} and the length of labellist {}".format(len(image_list), len(label_list)))

total_len = len(image_list)
# both lists here only contain addresses of data and label
all = pd.DataFrame({'image':image_list, 'label':label_list})
# shuffle to make sure samples better represent the whole dataset
all_shuffle = shuffle(all)

#train : val : test  = 6:2:2
train_set = all_shuffle[:int(total_len*0.6)]
val_set = all_shuffle[int(total_len*0.6):int(total_len*0.8)]
test_set = all_shuffle[int(total_len*0.8):]

train_set.to_csv("../data_list/train.csv", index = False)
val_set.to_csv("../data_list/val.csv", index = False)
test_set.to_csv("../data_list/test.csv", index = False)
