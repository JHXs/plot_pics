# -*- coding: utf-8 -*-
# 画出RNN、LSTM、GRU、TCN、patchtst和ST-PatchTST在PM2.5和SO2预测中的RMSE和MAE随预测时间步长变化的图表

import matplotlib.pyplot as plt
import numpy as np

# 数据定义
models = ['RNN', 'LSTM', 'GRU', 'TCN', 'patchtst', 'ST-PatchTST']
time_steps = ['+1h', '+4h', '+12h', '+24h']
x = np.arange(len(time_steps))

# PM2.5 数据
pm25_rmse = {
    'RNN': [8.949, 12.864, 19.031, 22.477],
    'LSTM': [9.846, 14.135, 21.642, 23.137],
    'GRU': [10.053, 14.423, 20.101, 23.976],
    'TCN': [8.607, 12.214, 17.483, 20.988],
    'patchtst': [0.419, 0.561, 0.720, 1.253],
    'ST-PatchTST': [0.415, 0.550, 0.717, 0.996]
}

pm25_mae = {
    'RNN': [6.434, 8.798, 13.752, 16.870],
    'LSTM': [7.191, 9.921, 15.207, 17.371],
    'GRU': [7.273, 10.193, 14.338, 16.942],
    'TCN': [6.402, 8.866, 13.384, 16.138],
    'patchtst': [0.307, 0.395, 0.507, 0.946],
    'ST-PatchTST': [0.302, 0.386, 0.504, 0.736]
}

# SO2 数据
so2_rmse = {
    'RNN': [4.597, 6.167, 8.072, 8.668],
    'LSTM': [4.802, 6.342, 8.205, 8.766],
    'GRU': [4.613, 6.217, 8.017, 8.760],
    'TCN': [4.424, 6.094, 7.766, 8.980],
    'patchtst': [0.323, 0.459, 0.585, 0.727],
    'ST-PatchTST': [0.313, 0.459, 0.575, 0.680]
}

so2_mae = {
    'RNN': [2.809, 3.821, 5.225, 5.745],
    'LSTM': [2.910, 3.946, 5.462, 5.815],
    'GRU': [2.843, 3.866, 5.210, 5.923],
    'TCN': [2.733, 3.912, 5.001, 6.044],
    'patchtst': [0.192, 0.288, 0.391, 0.512],
    'ST-PatchTST': [0.184, 0.288, 0.384, 0.469]
}

# 创建图表
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 颜色映射
colors = {
    'RNN': '#FF6B6B',
    'LSTM': '#4ECDC4',
    'GRU': '#45B7D1',
    'TCN': '#FFA07A',
    'patchtst': '#96CEB4',
    'ST-PatchTST': '#9B59B6'
}

markers = ['o', 's', '^', 'D', 'v', 'p']

# PM2.5 RMSE
ax = axes[0, 0]
for i, model in enumerate(models):
    ax.plot(x, pm25_rmse[model], marker=markers[i], color=colors[model],
            label=model, linewidth=2, markersize=8)
ax.set_xlabel('Forecast Time Step', fontsize=12)
ax.set_ylabel('RMSE', fontsize=12)
ax.set_title('PM2.5 - RMSE vs Forecast Time Step', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(time_steps)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# PM2.5 MAE
ax = axes[0, 1]
for i, model in enumerate(models):
    ax.plot(x, pm25_mae[model], marker=markers[i], color=colors[model],
            label=model, linewidth=2, markersize=8)
ax.set_xlabel('Forecast Time Step', fontsize=12)
ax.set_ylabel('MAE', fontsize=12)
ax.set_title('PM2.5 - MAE vs Forecast Time Step', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(time_steps)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# SO2 RMSE
ax = axes[1, 0]
for i, model in enumerate(models):
    ax.plot(x, so2_rmse[model], marker=markers[i], color=colors[model],
            label=model, linewidth=2, markersize=8)
ax.set_xlabel('Forecast Time Step', fontsize=12)
ax.set_ylabel('RMSE', fontsize=12)
ax.set_title('SO2 - RMSE vs Forecast Time Step', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(time_steps)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# SO2 MAE
ax = axes[1, 1]
for i, model in enumerate(models):
    ax.plot(x, so2_mae[model], marker=markers[i], color=colors[model],
            label=model, linewidth=2, markersize=8)
ax.set_xlabel('Forecast Time Step', fontsize=12)
ax.set_ylabel('MAE', fontsize=12)
ax.set_title('SO2 - MAE vs Forecast Time Step', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(time_steps)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
print('图表已保存为 model_comparison.png')
plt.show()
