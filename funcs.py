import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def compile_data(data, sample="s1234"):
  # preprocess dataframe
  s1_t1 = data[["Sample 1 (320nm)", "Unnamed: 1", "Unnamed: 2"]].to_numpy().astype(float)
  s1_t2 = data[["Sample 1 (320nm)", "Unnamed: 1", "Unnamed: 3"]].to_numpy().astype(float)
  s1_t3 = data[["Sample 1 (320nm)", "Unnamed: 1", "Unnamed: 4"]].to_numpy().astype(float)
  s2_t1 = data[["Sample 2 (320nm)", "Unnamed: 7", "Unnamed: 8"]].to_numpy().astype(float)
  s2_t2 = data[["Sample 2 (320nm)", "Unnamed: 7", "Unnamed: 9"]].to_numpy().astype(float)
  s2_t3 = data[["Sample 2 (320nm)", "Unnamed: 7", "Unnamed: 10"]].to_numpy().astype(float)
  s3_t1 = data[["Sample 3 (320nm)", "Unnamed: 13", "Unnamed: 14"]].to_numpy().astype(float)
  s3_t2 = data[["Sample 3 (320nm)", "Unnamed: 13", "Unnamed: 15"]].to_numpy().astype(float)
  s3_t3 = data[["Sample 3 (320nm)", "Unnamed: 13", "Unnamed: 16"]].to_numpy().astype(float)
  s4_t1 = data[["Sample 4 (130nm)", "Unnamed: 20", "Unnamed: 21"]].to_numpy().astype(float)
  s4_t2 = data[["Sample 4 (130nm)", "Unnamed: 20", "Unnamed: 22"]].to_numpy().astype(float)
  s5_t1 = data[["Sample 5 (220nm)", "Unnamed: 25", "Unnamed: 26"]].to_numpy().astype(float)
  s5_t2 = data[["Sample 5 (220nm)", "Unnamed: 25", "Unnamed: 27"]].to_numpy().astype(float)
  s5_t3 = data[["Sample 5 (220nm)", "Unnamed: 25", "Unnamed: 28"]].to_numpy().astype(float)
  
  if sample=="s12345":
    temp = np.concatenate((s1_t1[:,0],s1_t2[:,0],s1_t3[:,0],s2_t1[:,0],s2_t2[:,0],s2_t3[:,0],s3_t1[:,0], s3_t2[:,0], s3_t3[:,0],s4_t1[:,0], s4_t2[:,0], s5_t1[:,0], s5_t2[:,0], s5_t3[:,0]))
    hum = np.concatenate((s1_t1[:,1],s1_t2[:,1],s1_t3[:,1],s2_t1[:,1],s2_t2[:,1],s2_t3[:,1],s3_t1[:,1], s3_t2[:,1], s3_t3[:,1],s4_t1[:,1], s4_t2[:,1], s5_t1[:,1], s5_t2[:,1], s5_t3[:,1]))
    thick = np.concatenate((s1_t1[:,2],s1_t2[:,2],s1_t3[:,2],s2_t1[:,2],s2_t2[:,2],s2_t3[:,2],s3_t1[:,2], s3_t2[:,2], s3_t3[:,2],s4_t1[:,2], s4_t2[:,2], s5_t1[:,2], s5_t2[:,2], s5_t3[:,2]))
    
  if sample=="s1234":
    # Samples 1,2,3,4
    temp = np.concatenate((s1_t1[:,0],s1_t2[:,0],s1_t3[:,0],s2_t1[:,0],s2_t2[:,0],s2_t3[:,0],s3_t1[:,0], s3_t2[:,0], s3_t3[:,0],s4_t1[:,0], s4_t2[:,0]))
    hum = np.concatenate((s1_t1[:,1],s1_t2[:,1],s1_t3[:,1],s2_t1[:,1],s2_t2[:,1],s2_t3[:,1],s3_t1[:,1], s3_t2[:,1], s3_t3[:,1],s4_t1[:,1], s4_t2[:,1]))
    thick = np.concatenate((s1_t1[:,2],s1_t2[:,2],s1_t3[:,2],s2_t1[:,2],s2_t2[:,2],s2_t3[:,2],s3_t1[:,2], s3_t2[:,2], s3_t3[:,2],s4_t1[:,2], s4_t2[:,2]))
    
  if sample=="s123":
    # Samples 1,2,3
    temp = np.concatenate((s1_t1[:,0],s1_t2[:,0],s1_t3[:,0],s2_t1[:,0],s2_t2[:,0],s2_t3[:,0],s3_t1[:,0], s3_t2[:,0], s3_t3[:,0]))
    hum = np.concatenate((s1_t1[:,1],s1_t2[:,1],s1_t3[:,1],s2_t1[:,1],s2_t2[:,1],s2_t3[:,1],s3_t1[:,1], s3_t2[:,1], s3_t3[:,1]))
    thick = np.concatenate((s1_t1[:,2],s1_t2[:,2],s1_t3[:,2],s2_t1[:,2],s2_t2[:,2],s2_t3[:,2],s3_t1[:,2], s3_t2[:,2], s3_t3[:,2]))
  
  if sample=="s1235":
    temp = np.concatenate((s1_t1[:,0],s1_t2[:,0],s1_t3[:,0],s2_t1[:,0],s2_t2[:,0],s2_t3[:,0],s3_t1[:,0], s3_t2[:,0], s3_t3[:,0], s5_t1[:,0], s5_t2[:,0], s5_t3[:,0]))
    hum = np.concatenate((s1_t1[:,1],s1_t2[:,1],s1_t3[:,1],s2_t1[:,1],s2_t2[:,1],s2_t3[:,1],s3_t1[:,1], s3_t2[:,1], s3_t3[:,1], s5_t1[:,1], s5_t2[:,1], s5_t3[:,1]))
    thick = np.concatenate((s1_t1[:,2],s1_t2[:,2],s1_t3[:,2],s2_t1[:,2],s2_t2[:,2],s2_t3[:,2],s3_t1[:,2], s3_t2[:,2], s3_t3[:,2], s5_t1[:,2], s5_t2[:,2], s5_t3[:,2]))
  
  if sample=="s4":
    # Sample 4
    temp = np.concatenate((s4_t1[:,0], s4_t2[:,0]))
    hum = np.concatenate((s4_t1[:,1], s4_t2[:,1]))
    thick = np.concatenate((s4_t1[:,2], s4_t2[:,2]))
    
  if sample=="s5":
    # Sample 5
    temp = np.concatenate((s5_t1[:,0], s5_t2[:,0], s5_t3[:,0]))
    hum = np.concatenate((s5_t1[:,1], s5_t2[:,1], s5_t3[:,1]))
    thick = np.concatenate((s5_t1[:,2], s5_t2[:,2], s5_t3[:,2]))
  
  s1_size = s1_t1.shape[0]+s1_t2.shape[0]+s1_t3.shape[0]
  s2_size = s2_t1.shape[0]+s2_t2.shape[0]+s2_t3.shape[0]
  s3_size = s3_t1.shape[0]+s3_t2.shape[0]+s3_t3.shape[0]
  s4_size = s4_t1.shape[0]+s4_t2.shape[0]
  s5_size = s5_t1.shape[0]+s5_t2.shape[0]+s5_t3.shape[0]
  
  return temp, hum, thick, (s1_size,s2_size,s3_size,s4_size,s5_size)



def make_graph(X,Y,Z,temp,hum,thick,sizes,z_offset,sample="s1234"):
  #define how many datapoints for each sample or combined samples
  s1 = sizes[0]
  s12 = sizes[0]+sizes[1]
  s123 = sizes[0]+sizes[1]+sizes[2]
  s1234 = sizes[0]+sizes[1]+sizes[2]+sizes[3]
  s12345 = sizes[0]+sizes[1]+sizes[2]+sizes[3]+sizes[4]
  
  if sample=="s12345":
    fig = go.Figure(data=[
      go.Surface(x=X, y=Y, z=Z, opacity=0.7, colorscale="YlOrRd", cmin=np.amin(thick)-z_offset[0], cmax=np.amax(thick)+z_offset[0],
                 colorbar = {"len":0.75, "thickness": 40, "x": 0.88, "y":0.4, "tickfont":{"size":40}}),
      go.Scatter3d(x=temp[:s1], y=hum[:s1], z=thick[:s1], mode="markers", marker={"symbol": "cross","color":"black", "size": 10}),
      go.Scatter3d(x=temp[s1:s12], y=hum[s1:s12], z=thick[s1:s12], mode="markers", marker={"symbol": "cross", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s12:s123], y=hum[s12:s123], z=thick[s12:s123], mode="markers", marker={"symbol": "cross", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s123:s1234], y=hum[s123:s1234], z=thick[s123:s1234], mode="markers", marker={"symbol": "circle-open", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s1234:], y=hum[s1234:], z=thick[s1234:], mode="markers", marker={"symbol": "diamond-open", "color":"black", "size": 7})
    ])
  if sample=="s1234":
    fig = go.Figure(data=[
      go.Surface(x=X, y=Y, z=Z, opacity=0.7, colorscale="YlOrRd",cmin=np.amin(thick)-z_offset[0], cmax=np.amax(thick)+z_offset[0],
                 colorbar = {"len":0.75, "thickness": 70, "x": 0.88, "y":0.4, "tickfont":{"size":40}}),
      go.Scatter3d(x=temp[:s1], y=hum[:s1], z=thick[:s1], mode="markers", marker={"symbol": "cross","color":"black", "size": 10}),
      go.Scatter3d(x=temp[s1:s12], y=hum[s1:s12], z=thick[s1:s12], mode="markers", marker={"symbol": "cross", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s12:s123], y=hum[s12:s123], z=thick[s12:s123], mode="markers", marker={"symbol": "cross", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s123:], y=hum[s123:], z=thick[s123:], mode="markers", marker={"symbol": "circle-open", "color":"black", "size": 10}),
    ])
  if sample=="s123":
    fig = go.Figure(data=[
      go.Surface(x=X, y=Y, z=Z, opacity=0.7, colorscale="YlOrRd", cmin=np.amin(thick)-z_offset[0], cmax=np.amax(thick)+z_offset[0],
             colorbar = {"len":0.75, "thickness": 70, "x": 0.88, "y":0.4, "tickfont":{"size":40}}),
      go.Scatter3d(x=temp[:s1], y=hum[:s1], z=thick[:s1], mode="markers", marker={"symbol": "cross","color":"black", "size": 10}),
      go.Scatter3d(x=temp[s1:s12], y=hum[s1:s12], z=thick[s1:s12], mode="markers", marker={"symbol": "circle-open", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s12:], y=hum[s12:], z=thick[s12:], mode="markers", marker={"symbol": "diamond-open", "color":"black", "size": 7})
    ])
  if sample=="s1235":
    fig = go.Figure(data=[
      go.Surface(x=X, y=Y, z=Z, opacity=0.7, colorscale="YlOrRd", cmin=np.amin(thick)-z_offset[0], cmax=np.amax(thick)+z_offset[0],
                 colorbar = {"len":0.75, "thickness": 70, "x": 0.88, "y":0.4, "tickfont":{"size":40}}),
      go.Scatter3d(x=temp[:s1], y=hum[:s1], z=thick[:s1], mode="markers", marker={"symbol": "cross","color":"black", "size": 10}),
      go.Scatter3d(x=temp[s1:s12], y=hum[s1:s12], z=thick[s1:s12], mode="markers", marker={"symbol": "cross", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s12:s123], y=hum[s12:s123], z=thick[s12:s123], mode="markers", marker={"symbol": "cross", "color":"black", "size": 10}),
      go.Scatter3d(x=temp[s1234:], y=hum[s1234:], z=thick[s1234:], mode="markers", marker={"symbol": "diamond-open", "color":"black", "size": 7})
    ])
  if sample=="s4":
    fig = go.Figure(data=[
      go.Surface(x=X, y=Y, z=Z, opacity=0.7, colorscale="YlOrRd",cmin=np.amin(thick)-z_offset[0], cmax=np.amax(thick)+z_offset[0],
                 colorbar = {"len":0.75, "thickness": 70, "x": 0.88, "y":0.4, "tickfont":{"size":40}}),
      go.Scatter3d(x=temp, y=hum, z=thick, mode="markers", marker={"symbol": "circle", "color":"black", "size": 10})
    ])
  if sample=="s5":
    fig = go.Figure(data=[
      go.Surface(x=X, y=Y, z=Z, opacity=0.7, colorscale="YlOrRd", cmin=np.amin(thick)-z_offset[0], cmax=np.amax(thick)+z_offset[0],
                 colorbar = {"len":0.75, "thickness": 70, "x": 0.88, "y":0.4, "tickfont":{"size":40}}),
      go.Scatter3d(x=temp, y=hum, z=thick, mode="markers", marker={"symbol": "circle", "color":"black", "size": 10})
    ])
  return fig

def get_colors(color_path="/content/drive/MyDrive/nanofilm_data/data_files/bubble_pics"):
  c1c18c26 = plt.imread(f"{color_path}/c1c18c26.jpg")/255
  c1c18c26 = [np.mean(c1c18c26[:,:,0]),np.mean(c1c18c26[:,:,1]),np.mean(c1c18c26[:,:,2])]
  c2c10c27 = plt.imread(f"{color_path}/c2c10c27.jpg")/255
  c2c10c27 = [np.mean(c2c10c27[:,:,0]),np.mean(c2c10c27[:,:,1]),np.mean(c2c10c27[:,:,2])]
  c3c11c19c28 = plt.imread(f"{color_path}/c3c11c19c28.jpg")/255
  c3c11c19c28 = [np.mean(c3c11c19c28[:,:,0]),np.mean(c3c11c19c28[:,:,1]),np.mean(c3c11c19c28[:,:,2])]
  c4c12c20c29 = plt.imread(f"{color_path}/c4c12c20c29.jpg")/255
  c4c12c20c29 = [np.mean(c4c12c20c29[:,:,0]),np.mean(c4c12c20c29[:,:,1]),np.mean(c4c12c20c29[:,:,2])]
  c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32 = plt.imread(f"{color_path}/c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32.jpg")/255
  c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32 = [np.mean(c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32[:,:,0]),np.mean(c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32[:,:,1]),np.mean(c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32[:,:,2])]
  c9 = plt.imread(f"{color_path}/c9.jpg")/255
  c9 = [np.mean(c9[:,:,0]),np.mean(c9[:,:,1]),np.mean(c9[:,:,2])]
  c17 = plt.imread(f"{color_path}/c17.jpg")/255
  c17 = [np.mean(c17[:,:,0]),np.mean(c17[:,:,1]),np.mean(c17[:,:,2])]
  c25 = plt.imread(f"{color_path}/c25.jpg")/255
  c25 = [np.mean(c25[:,:,0]),np.mean(c25[:,:,1]),np.mean(c25[:,:,2])]
  colors = np.array([c1c18c26, c2c10c27, c3c11c19c28, c4c12c20c29, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, 
           c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c9, c2c10c27, c3c11c19c28, c4c12c20c29,
           c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32,
           c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c17, c1c18c26, c3c11c19c28, c4c12c20c29, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32,
           c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32,
           c25, c1c18c26, c2c10c27, c3c11c19c28, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, 
           c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32, c5c6c7c8c13c14c15c16c21c22c23c24c30c31c32])
  return colors
