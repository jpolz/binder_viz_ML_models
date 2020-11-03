import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA, KernelPCA

def plot_kpca_results(X, y):
    
    kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
    X_kpca = kpca.fit_transform(X)
    X_back = kpca.inverse_transform(X_kpca)
    pca = PCA()
    X_pca = pca.fit_transform(X)
    
    plt.figure(figsize=(10,10))
    plt.subplot(2, 2, 1, aspect='equal')
    plt.title("Original space")
    reds = y == 0
    blues = y == 1

    plt.scatter(X[reds, 0], X[reds, 1], c="red",
                s=1)
    plt.scatter(X[blues, 0], X[blues, 1], c="blue",
                s=1)
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")

    X1, X2 = np.meshgrid(np.linspace(-1.5, 1.5, 50), np.linspace(-1.5, 1.5, 50))
    X_grid = np.array([np.ravel(X1), np.ravel(X2)]).T
    # projection on the first principal component (in the phi space)
    Z_grid = kpca.transform(X_grid)[:, 0].reshape(X1.shape)
    plt.contour(X1, X2, Z_grid, colors='grey', linewidths=1, origin='lower')

    plt.subplot(2, 2, 2, aspect='equal')
    plt.scatter(X_pca[reds, 0], X_pca[reds, 1], c="red",
                s=1)
    plt.scatter(X_pca[blues, 0], X_pca[blues, 1], c="blue",
                s=1)
    plt.title("Projection by PCA")
    plt.xlabel("1st principal component")
    plt.ylabel("2nd component")

    plt.subplot(2, 2, 3, aspect='equal')
    plt.scatter(X_kpca[reds, 0], X_kpca[reds, 1], c="red",
                s=1)
    plt.scatter(X_kpca[blues, 0], X_kpca[blues, 1], c="blue",
                s=1)
    plt.title("Projection by KPCA")
    plt.xlabel(r"1st principal component in space induced by $\phi$")
    plt.ylabel("2nd component")

    plt.subplot(2, 2, 4, aspect='equal')
    plt.scatter(X_back[reds, 0], X_back[reds, 1], c="red",
                s=1)
    plt.scatter(X_back[blues, 0], X_back[blues, 1], c="blue",
                s=1)
    plt.title("Original space after inverse transform")
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")

    plt.tight_layout()
    plt.show()