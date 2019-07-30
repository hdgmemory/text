# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:22:41 2019

@author: guanguan
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm


def winsorize_median(tmp):
    if isinstance(tmp, pd.Series):               #isinstance（object,classinfo）判断一个对象是否是一个已知的类型
        mc = sm.stats.stattools.medcouple(tmp)   #medcouple（）用于识别非对称分布的异常值,向右倾斜的分布是正的，对于向左倾斜的分布是负的，对称分布是零
        data = sorted(tmp)                       #sorted() 函数对所有可迭代的对象进行 排序操作，返回一个新的 list
        q1 = np.percentile(data, 25)             #计算一个多维数组的任意百分比分位数的数值，25%分位数
        q3 = np.percentile(data, 75)
        iqr = q3-q1
        if mc >= 0:                              #mc表示样本偏度，当样本数据分布右偏时，提升正常数据区间上限的数值；样本数据左偏时，则会降低正常数据区间下限的数值。
            l = q1-1.5*np.exp(-3.5*mc)*iqr
            u = q3+1.5*np.exp(4*mc)*iqr
        else:
            l = q1-1.5*np.exp(-4*mc)*iqr
            u = q3+1.5*np.exp(3.5*mc)*iqr
        pd_clu = tmp.index
        tmp = tmp.tolist()
        for index in range(len(tmp)):
            if tmp[index] < l:
                tmp[index] = l
            if tmp[index] > u:
                tmp[index] = u
#         tmp[tmp<l]=l
#         tmp[tmp>u]=u
    return pd.Series(tmp,index = pd_clu)

#################################################
# def winsorize_median(tmp):
#     if isinstance(tmp, pd.Series):               #isinstance（object,classinfo）判断一个对象是否是一个已知的类型
#         mc = sm.stats.stattools.medcouple(tmp)   #medcouple（）用于识别非对称分布的异常值,向右倾斜的分布是正的，对于向左倾斜的分布是负的，对称分布是零
#         data = sorted(tmp)                       #sorted() 函数对所有可迭代的对象进行 排序操作，返回一个新的 list
#         q1 = np.percentile(data, 25)             #计算一个多维数组的任意百分比分位数的数值，25%分位数
#         q3 = np.percentile(data, 75)
#         iqr = q3-q1
#         if mc >= 0:                              #mc表示样本偏度，当样本数据分布右偏时，提升正常数据区间上限的数值；样本数据左偏时，则会降低正常数据区间下限的数值。
#             l = q1-1.5*np.exp(-3.5*mc)*iqr
#             u = q3+1.5*np.exp(4*mc)*iqr
#         else:
#             l = q1-1.5*np.exp(-4*mc)*iqr
#             u = q3+1.5*np.exp(3.5*mc)*iqr
#         tmp[tmp<l]=l
#         tmp[tmp>u]=u
#         print tmp
#     return tmp
#######################################

# 函数封装问题（标准化：z-score使得平均值为0，标准差为1）
#标准化：将去极值处理后的因子暴露度序列减去其现在的均值、除以其标准差，得到一个新的近似服从N(0,1)分布的序列，
#这样做可以让不同因子的暴露度之间具有可比性
def standardize_zscore(tmp):
    if isinstance(tmp, pd.Series):
        mu = tmp.mean()
        sigma = tmp.std()
        tmp = (tmp - mu)/sigma
    return tmp



data = pd.read_csv('data_final_1228.csv')
data.set_index('secID',inplace=True, drop=False)

fac = ['NetAssetGrowRate', 'NetProfitGrowRate', 'OperatingProfitGrowRate', 'LCAP', 'REVS20', 'ROA', 'Volatility', 'MACD', 'ATR14', 'EMV6', 'DEA', 'DIFF', 'high_low_2w', 'relative_strength_12w', 'mfd_buyamt_d','S_QFA_ROE',  'S_FA_OCFTOOR']
for f in fac:
    data[f] = standardize_zscore(winsorize_median(data[f]))
data.to_csv('G:\\byy\\yinzi\\filter_factor\\all_data\\uqer\\data_final_1228_formal.csv')