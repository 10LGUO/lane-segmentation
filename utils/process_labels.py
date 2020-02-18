import numpy as np
import colorsys

def encoder(orginal_mask):
    encoded_mask = np.zeros(original_mask.shape[0], original_mask.shape[1])
    id_train = {0:[0, 249, 255, 213, 206, 207, 211, 208,216,215,218, 219,232, 202, 231,230,228,229,233,212,223],
                1:[200, 204, 209], 2: [201,203], 3:[217], 4:[210], 5:[214],
                6:[220,221,222,224,225,226], 7:[205,227,250]}

    for i in range(8):
        for item in id_train[i]:
            encoded_mask[original_mask == item] = i  # numpy matrix operation

    return encoded_mask

def decoder(encoded_mask):
    decoded_mask = np.zeros(encoded_mask.shape[0], encoded_mask.shape[1], dtype='unit8')
    original_id = {0:0, 1:204, 2:203, 3:217, 4:210, 5:214, 6:224, 7:227}
    for i in range(8):
        decoded_mask[encoded_mask == i] = original_id[i]

    return decoded_mask

def color_decoder(encoded_mask):
    decoded_color_mask = np.zeros((3, encoded_mask.shape[0], encoded_mask.shape[1]), dtype='unit8')
    original_color_id = [{0:0, 1:70, 2:0, 3:153, 4:128, 5:190, 6:0, 7:255},
                        {0:0, 1:130, 2:0, 3:153, 4:64, 5:153, 6:0, 7:128},{0:0, 1:180, 2:142, 3:153, 4:128, 5:153, 6:230, 7:0}]
    for i in range(3):
        for j in range(8):
            decoded_color_mask[i][encoded_mask == j] = original_id[i][j]

    return decoded_color_mask
