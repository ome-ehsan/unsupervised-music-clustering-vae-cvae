# Music Genre Clustering and Generation with Multimodal VAEs

This repository contains a comparative analysis of Variational Autoencoder (VAE) architectures for unsupervised music representation learning and generation. The project investigates the transition from unimodal handcrafted features to conditional multimodal deep learning, evaluating the trade-offs between geometric clustering separability and semantic generative fidelity.

## Project Overview

The goal of this project is to learn latent representations of musical tracks that capture semantic attributes such as genre. We implement and compare three distinct architectures:

1.  **Basic VAE:** A Multi-Layer Perceptron (MLP) model using 40-dimensional MFCC features.
2.  **Enhanced Multimodal VAE:** A fusion model combining Convolutional Neural Networks (CNN) for Mel-spectrograms and linear layers for text (lyrics) embeddings.
3.  **Conditional VAE (CVAE):** A structured prediction model conditioned on genre labels to enable controlled audio generation.

## Dataset

This project utilizes a subset of the Free Music Archive (FMA) dataset.

* **Metadata and Lyrics:** Obtained from the [FMA GitHub Repository](https://github.com/mdeff/fma).
* **Audio Files:** The processed `.wav` audio samples used for training are available here: [Google Drive Link](https://drive.google.com/drive/folders/1dB1Qd88Zmt3QpaNaQ9E-EVPooRrAx5n7?usp=sharing).

## Results Summary

* **Clustering:** Linear baselines (PCA + K-Means) achieved higher Silhouette scores due to the creation of convex projections. However, the VAE architectures demonstrated higher Adjusted Rand Index (ARI) scores, indicating better alignment with ground-truth genre labels despite complex manifold geometry.
* **Generation:** The Conditional VAE successfully reconstructs high-fidelity Mel-spectrograms and allows for genre-conditioned sampling, validating the effectiveness of the multimodal fusion approach.

## References

* **MFCCs:** Davis, S., & Mermelstein, P. (1980). Comparison of parametric representations for monosyllabic word recognition.
* **VAE:** Kingma, D. P., & Welling, M. (2013). Auto-encoding variational bayes.
* **CVAE:** Sohn, K., Lee, H., & Yan, X. (2015). Learning structured output representation using deep conditional generative models.
