import cv2
import numpy as np
from scipy.spatial.distance import pdist, squareform
def plot_lines_between_nodes(warped_points, bird_image, d_thresh):
    p = np.array(warped_points)
    dist_condensed = pdist(p)#计算距离
    dist = squareform(dist_condensed)#压缩距离矩阵，按照下三角
    # Close enough: 10 feet mark
    dd = np.where(dist < d_thresh)#返回索引
    close_p = []
    color_10 = (80, 172, 110)
    lineThickness = 2
    for i ,j in zip(dd[0],dd[1]):
            if(i>j):
                cv2.line(
                    bird_image,
                    (p[i][0], p[i][1]),
                    (p[j][0], p[j][1]),
                    color_10,
                    lineThickness,
                )
    # for i in range(int(np.ceil(len(dd[0]) / 2))):#np.ceil向上取证
    #     if dd[0][i] != dd[1][i]:
    #         point1 = dd[0][i]
    #         point2 = dd[1][i]
    #
    #         close_p.append([point1, point2])
    #
    #         cv2.line(
    #             bird_image,
    #             (p[point1][0], p[point1][1]),
    #             (p[point2][0], p[point2][1]),
    #             color_10,
    #             lineThickness,
    #         )

    # Really close: 6 feet mark
    dd = np.where(dist < d_thresh)
    danger_p = []
    color_6 = (52, 92, 227)
    for i ,j in zip(dd[0],dd[1]):
            if(i>j):
                cv2.line(
                    bird_image,
                    (p[i][0], p[i][1]),
                    (p[j][0], p[j][1]),
                    color_6,
                    lineThickness,
                )
    # for i in range(int(np.ceil(len(dd[0]) / 2))):
    #     if dd[0][i] != dd[1][i]:
    #         point1 = dd[0][i]
    #         point2 = dd[1][i]
    #
    #         danger_p.append([point1, point2])
    #         cv2.line(
    #             bird_image,
    #             (p[point1][0], p[point1][1]),
    #             (p[point2][0], p[point2][1]),
    #             color_6,
    #             lineThickness,
    #         )
    # Display Birdeye view
    # cv2.imshow("Bird Eye View", bird_image)
    # cv2.waitKey(1)
