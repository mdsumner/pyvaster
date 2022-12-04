import math

def hello():
    return (u'hellooooo world')


def x_res(dimension, extent):
  dx = extent[1] - extent[0]
  res = dx / dimension[0]
  return res


def y_res(dimension, extent):
  dy = extent[3] - extent[2]
  res = dy / dimension[1]
  return res


def n_col(dimension, extent): 
  return dimension[0]

def n_row(dimension, extent): 
  return dimension[1]

def x_min(dimension, extent):
  return extent[0]

def x_max(dimension, extent):
  return extent[1]

def y_min(dimension, extent):
  return extent[2]

def y_max(dimension, extent):
  return extent[3]



def cell_from_xy(dimension, extent, xx, yy):
  nn = len(xx)
  ncols = n_col(dimension, extent)
  nrows = n_row(dimension, extent)
  xmin = x_min(dimension, extent)
  xmax = x_max(dimension, extent)
  ymin = y_min(dimension, extent)
  ymax = y_max(dimension, extent)
  yres_inv = nrows / (ymax - ymin)
  xres_inv = ncols / (xmax - xmin)
  
  cell = []
  ##row = ifelse(yy == ymin, nrows - 1, row)
  for i in range(nn):
    row = math.floor((ymax  - yy[i]) * yres_inv)
    col = math.floor((xx[i] - xmin) * xres_inv)
    if xx == xmax:
      col = ncols - 1
    else: 
      col = col
    if yy == ymin:
      row = nrows - 1
    else:
     row = row


    if row < 0 or row >= nrows or col < 0 or col >= ncols: 
      cell.append( -1) ## missing value?
    else:
      cell.append(row * ncols + col + 1)
    return cell
 ## col = floor((xx - xmin) * xres_inv)
  ## as for rows above. Go right, except for last column
  ##col <- ifelse (xx == xmax, ncols-1, col)

#  ifelse (row < 0 | row >= nrows | col < 0 | col >= ncols, NA_real_, row * ncols + col + 1)
