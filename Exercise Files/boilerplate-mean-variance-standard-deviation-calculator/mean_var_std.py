#!/usr/bin/env python 
# created by Regina Citra Pesela (reginapasela@gmail.com)

import numpy as np

def calculate(list):
    
    # first, we should check if the list length is 9
    # if it's not 9 then raise ValueError and
    # return "List must contain nine numbers"
    
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')


    # generate 3 x 3 matrix from the list using numpy

    array_list = np.array(list).reshape([3,3])


    # calculate mean, variance, standard deviation, max, min and sum
    # by axis 1, axis 2 and flattened respectively

    list_mean = [
                 array_list.mean(axis = 0).tolist(),
                 array_list.mean(axis = 1).tolist(),
                 array_list.mean().tolist()
                ]

    list_variance = [
                     array_list.var(axis = 0).tolist(),
                     array_list.var(axis = 1).tolist(),
                     array_list.var().tolist()
                    ]

    list_sd = [
               array_list.std(axis = 0).tolist(),
               array_list.std(axis = 1).tolist(),
               array_list.std().tolist()
              ]

    list_max = [
                array_list.max(axis = 0).tolist(),
                array_list.max(axis = 1).tolist(),
                array_list.max().tolist()    
               ]

    list_min = [
                array_list.min(axis = 0).tolist(),
                array_list.min(axis = 1).tolist(),
                array_list.min().tolist()    
               ]

    list_sum = [
                array_list.sum(axis = 0).tolist(),
                array_list.sum(axis = 1).tolist(),
                array_list.sum().tolist()    
               ]


    # return calculations as dictionary that contains mean, 
    # variance, standard deviation, max, min, and sum respectively
    
    calculations = {
                    'mean' : list_mean,
                    'variance' : list_variance,
                    'standard deviation' : list_sd,
                    'max' : list_max,
                    'min' : list_min,
                    'sum' : list_sum
                   }


    return calculations