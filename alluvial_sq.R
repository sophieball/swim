library(scales)

dat <- read.csv("traffic_r.csv", header = TRUE, as.is = FALSE)

names <- matrix(NA, nrow = length(dat[,1]), ncol = length(dat)/2)
freqs <- matrix(NA, nrow = length(dat[,1]), ncol = length(dat)/2)

#sort each col-tuples
for (i in 1:(length(dat)/2)) {
  tmp <- data.frame("name" = dat[, (i - 1) * 2 + 1], "freq" = dat[, i * 2])
  tmp <- tmp[order(tmp[, "name"]), ]
  names[, i] = as.character(tmp[, 1])
  freqs[, i] = tmp[, 2]
}

names <- data.frame(names)
names[] <- lapply(names, as.character)
freqs <- data.frame(freqs)

#max number of unique items in a col
max_row_len = max(as.numeric(lapply(lapply(names, unique), length)))

#combine items in each col
com_names = matrix(NA, nrow = max_row_len, ncol = length(names))
com_freqs = matrix(NA, nrow = max_row_len, ncol = length(names))
for (i in 1:length(names)) {
  count = 1
  com_names[1, i] <- as.character(names[[1, i]])
  com_freqs[1, i] = freqs[[1, i]]
  for (j in 2:length(names[, i])) {
    if (as.character(names[[j, i]]) == com_names[count, i]) {
      com_freqs[count, i] = com_freqs[count, i] + freqs[[j, i]]
    }
    else {
      count = count + 1
      com_names[count, i] = as.character(names[[j, i]])
      com_freqs[count, i] = freqs[[j, i]]
    }
  }
}

#calculate blocks

#sort each col-tuples by freq
for (i in 1:(dim(com_names)[2])) {
  tmp <- data.frame("name" = com_names[, i], "freq" = com_freqs[, i])
  tmp <- tmp[order(tmp[, "freq"]), ]
  com_names[, i] = as.character(tmp[, 1])
  com_freqs[, i] = tmp[, 2]
}

block_margin = 0.01
y_coors = matrix(NA, nrow = dim(com_freqs)[1] + 1, ncol = dim(com_freqs)[2])
rel_freqs = matrix(NA, nrow = dim(com_freqs)[1], ncol = dim(com_freqs)[2])
y_coors[1, ] = 0
for (i in 1:(length(com_freqs))) {
  rel_freqs[, i] = com_freqs[, i] / sum(com_freqs[, i])
  y_coors[2, i] = rel_freqs[1, i]
  for (k in 2:(length(rel_freqs[, 1]))) {
    y_coors[k + 1, i] = sum(rel_freqs[1:k, i])
  }
}

# ys for all blocks to be drawn, taken margins into account
ys = matrix(NA, nrow = dim(y_coors)[1] - 1, ncol = dim(y_coors)[2] * 2)
for (i in 1:dim(y_coors)[2]) {
  for (k in 1:dim(y_coors)[1] - 1) {
    ys[k, i * 2 - 1] = y_coors[k, i]
    ys[k, i * 2] = y_coors[k + 1, i] - 2 * block_margin
  }
}

# (0, 0) is left bottom corner, so sorting freq from low to high will draw
# most freqs on top
plot.new()
col_width = 0.5
col_dist = 2
par(mar = c(1, 1, 1, 1))
plot(NULL, type = "n", xlim = c(0, dim(y_coors)[2] * col_dist - 1), ylim = c(0, 1), 
     xaxt = "n", yaxt = "n", xaxs = "i", yaxs = "i", xlab = '', ylab = '',
     frame = FALSE)
for (i in 1:dim(y_coors)[2]) {
  for (k in 1:(dim(y_coors)[1] - 1)) {
    rect((i - 1) * col_dist, ys[k, i * 2 - 1], (i - 1) * col_dist + col_width, ys[k, i * 2])
  }
}

#put text labels
for (i in 1:(dim(ys)[2]/2)) {
  for (k in 1:dim(ys)[1]) {
    text(x = (i - 1) * 2 + 0.25, 
         y = 0.5 * (ys[k, i * 2 - 1] + ys[k, i * 2]), 
         labels = com_names[k, i],
         cex = 0.8)
  }
}

#==========

#calculate curves
for (i in 1:(dim(dat)[2]/2 - 1)) {
  start = (i - 1) * col_dist + col_width + 0.01
  end = i * col_dist - 0.01
  curve_x = c(start, end, end, start)
  curve_y = matrix(NA, nrow = dim(dat)[1], ncol = 4)
  left_y_bot = ys[, i]
  right_y_bot = ys[, i + 2]
  dat_col = i * 2 - 1
  for (k in 1:dim(dat)[1]) {
    sorted_id = match(dat[[k, dat_col]], com_names[, i])
    curve_y[k, 1] = left_y_bot[sorted_id] #left_bot
    height = dat[k, dat_col + 1] / com_freqs[sorted_id, i] * (ys[sorted_id, i + 1] - ys[sorted_id, i])
    left_y_bot[sorted_id] = left_y_bot[sorted_id] + height
    curve_y[k, 4] = left_y_bot[sorted_id]
    
    #right
    if (i < dim(com_names)[2]) {
      sorted_id = match(dat[[k, dat_col + 2]], com_names[, i + 1])
      curve_y[k, 2] = right_y_bot[sorted_id]
      height = dat[k, dat_col + 3] / com_freqs[sorted_id, i + 1] * (ys[sorted_id, i + 3] - ys[sorted_id, i + 2])
      right_y_bot[sorted_id] = right_y_bot[sorted_id] + height
      curve_y[k, 3] = right_y_bot[sorted_id]
    }
    xspline(x = curve_x, y = curve_y[k, ], open = FALSE, col = alpha("green", 0.5), border = "green")
  }
}