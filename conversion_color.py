import numpy as np
import cv2

def RGB2HSV(I):
    Ir = I[:,:,0].astype(np.float64) / 255
    Ig = I[:,:,1].astype(np.float64) / 255
    Ib = I[:,:,2].astype(np.float64) / 255
    m, n = Ir.shape[:2]

    Iv = np.zeros((m, n))
    Is = np.zeros((m, n))
    Ih = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            r = Ir[i, j]
            g = Ig[i, j]
            b = Ib[i, j]

            v = np.max([r, g, b])
            vm = v - np.min([r, g, b])
            if v == 0:
                s = 0
            else:
                s = vm / v
        
            if s == 0:
                h = 0
            elif v == r:
                h = 60 * (g - b) / vm if g >= b else 60 * (g - b) / vm + 360
            elif v == g:
                h = 60 * (b - r) / vm + 120
            elif v == b:
                h = 60 * (r - g) / vm + 240

            Iv[i, j] = v
            Is[i, j] = s
            Ih[i, j] = h

    Ihsv = np.zeros_like(I)
    Ihsv[:,:,0] = Ih
    Ihsv[:,:,1] = Is
    Ihsv[:,:,2] = Iv

    return Ihsv

def RGB2XYZ(I):
    Ir = I[:, :, 0].astype(float)
    Ig = I[:, :, 1].astype(float)
    Ib = I[:, :, 2].astype(float)
    m, n = Ir.shape

    k = np.array([[0.49, 0.31, 0.20],
                  [0.17697, 0.81240, 0.01063],
                  [0.00, 0.01, 0.99]])

    Ix = np.zeros((m, n), dtype=float)
    Iy = np.zeros((m, n), dtype=float)
    Iz = np.zeros((m, n), dtype=float)

    for i in range(m):
        for j in range(n):
            rgb = np.array([Ir[i, j], Ig[i, j], Ib[i, j]])
            xyz = (1/0.17697) * k
            xyz = np.dot(k, rgb)
            Ix[i, j] = xyz[0]
            Iy[i, j] = xyz[1]
            Iz[i, j] = xyz[2]

    Ixyz = np.zeros((m, n, 3), dtype=float)
    Ixyz[:, :, 0] = Ix
    Ixyz[:, :, 1] = Iy 
    Ixyz[:, :, 2] = Iz 
    return Ixyz
def RGB2CMY(I):
    Ir = I[:, :, 0].astype(float)
    Ig = I[:, :, 1].astype(float)
    Ib = I[:, :, 2].astype(float)
    a, b = Ir.shape

    Ic = np.zeros((a, b), dtype=float)
    Im = np.zeros((a, b), dtype=float)
    Iy = np.zeros((a, b), dtype=float)

    for i in range(a):
        for j in range(b):
            c = 1 - (Ir[i, j] / 255)
            m = 1 - (Ig[i, j] / 255)
            y = 1 - (Ib[i, j] / 255)

            Ic[i, j] = c
            Im[i, j] = m
            Iy[i, j] = y

    Icmy = np.zeros((a, b, 3), dtype=np.float64)
    Icmy[:, :, 0] = Ic
    Icmy[:, :, 1] = Im
    Icmy[:, :, 2] = Iy

    return Icmy
def RGB2YCBCR(I):
    # Konversi citra dari RGB ke YCrCb
    Ir = I[:,:,0]
    Ig = I[:,:,1]
    Ib = I[:,:,2]
    a,b = Ir.shape

    Iy = np.zeros((a, b), dtype=np.float64)
    Icb = np.zeros((a, b), dtype=np.float64)
    Icr = np.zeros((a, b), dtype=np.float64)

    k1 = [0, 128, 128]
    k2 = [
        [0.2999, 0.587, 0.114],
        [-0.169, -0.331, 0.500],
        [0.500, -0.419, -0.081]
    ]
    
    for i in range(a):
            for j in range(b):
                rgb = np.array([Ir[i, j], Ig[i, j], Ib[i, j]])
                ycbcr = k1 + np.dot(k2, rgb)
                Iy[i, j] = ycbcr[0]
                Icb[i, j] = ycbcr[1]
                Icr[i, j] = ycbcr[2]

    img_ycrcb = np.zeros((a,b,3))
    img_ycrcb[:, :, 0] = Iy
    img_ycrcb[:, :, 1] = Icb
    img_ycrcb[:, :, 2] = Icr
    return img_ycrcb
def fLab(q):
    if q > 0.008856:
        return pow(q, 1/3)
    else:
        return 7.787*q + 16/116
def fLab(q):
    if q > 0.008856:
        return pow(q, 1/3)
    else:
        return 7.787*q + 16/116
def RGB2LAB(I) :
    # konversi RGB ke XYZ
    Ixyz = RGB2XYZ(I)
    Ix = Ixyz[:,:,0] / 100
    Iy = Ixyz[:,:,1] / 100
    Iz = Ixyz[:,:,2] / 100
    [m,n] = Ix.shape

    # White Point d65
    xn = 0.95047
    yn = 1
    zn = 1.08883

    # konversi XYZ ke LAB
    IL = np.zeros((m,n))
    Ia = np.zeros((m,n))
    Ib = np.zeros((m,n))

    for i in range(m):
        for j in range(n):
            IL[i,j] = 116*fLab(Iy[i,j]/yn)-16
            Ia[i,j] = 500*(fLab(Ix[i,j]/xn)-fLab(Iy[i,j]/yn))
            Ib[i,j] = 200*(fLab(Iy[i,j]/yn)-fLab(Iz[i,j]/zn))

    ILab = np.zeros((m,n,3))
    ILab[:,:,0] = IL
    ILab[:,:,1] = Ia
    ILab[:,:,2] = Ib

    return ILab
def XYZ2RGB(I):
    Ix = I[:, :, 0]
    Iy = I[:, :, 1]
    Iz = I[:, :, 2]
    a, b = Ix.shape

    Ir = np.zeros((a, b), dtype=float)
    Ig = np.zeros((a, b), dtype=float)
    Ib = np.zeros((a, b), dtype=float)

    k = np.array(
        [[0.41847, -0.15866, -0.082835],
        [-0.091169, 0.25243, 0.015708],
        [0.00092090, 0.0025498, 0.17860]])
    for i in range(a):
        for j in range(b):
            xyz = [Ix[i, j], Iy[i, j], Iz[i, j]]
            rgb = np.dot(k, np.float64(xyz))
            Ir[i, j] = np.uint8(rgb[0])
            Ig[i, j] = np.uint8(rgb[1])
            Ib[i, j] = np.uint8(rgb[2])

    Irgb = np.zeros((a, b, 3), dtype=np.uint8)
    Irgb[:, :, 0] = Ir
    Irgb[:, :, 1] = Ig
    Irgb[:, :, 2] = Ib
    return Irgb
def XYZ2HSV(xyz):
    xyz = np.array(xyz, dtype=np.float32)
    rgb = XYZ2RGB(np.float32([[xyz]]))
    hsv = RGB2HSV(rgb)
    return hsv
def XYZ2CMY(xyz):
    xyz = np.array(xyz, dtype=np.float32)
    rgb = XYZ2RGB(np.float32([[xyz]]))
    cmy = RGB2CMY(rgb)
    return cmy
def XYZ2LAB(Ixyz):
    Ix = Ixyz[:,:,0] / 100
    Iy = Ixyz[:,:,1] / 100
    Iz = Ixyz[:,:,2] / 100
    [m,n] = Ix.shape

    # White Point d65
    xn = 0.95047
    yn = 1
    zn = 1.08883

    # konversi XYZ ke LAB
    IL = np.zeros((m,n))
    Ia = np.zeros((m,n))
    Ib = np.zeros((m,n))

    for i in range(m):
        for j in range(n):
            IL[i,j] = 116*fLab(Iy[i,j]/yn)-16
            Ia[i,j] = 500*(fLab(Ix[i,j]/xn)-fLab(Iy[i,j]/yn))
            Ib[i,j] = 200*(fLab(Iy[i,j]/yn)-fLab(Iz[i,j]/zn))

    ILab = np.zeros((m,n,3))
    ILab[:,:,0] = IL
    ILab[:,:,1] = Ia
    ILab[:,:,2] = Ib
    return ILab
