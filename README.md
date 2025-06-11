<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- [![Forks][forks-shield]][forks-url] -->
<!-- [![Stargazers][stars-shield]][stars-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/HappyPotatoHead/Signature-Verification-Model">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Signature Verification Model</h3>

  <p align="center">
    Because my eyes hurt
    <br />
    <a href="https://github.com/HappyPotatoHead/Signature-Verification-Model"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HappyPotatoHead/Signature-Verification-Model">View Demo</a>
    &middot;
    <a href="https://github.com/HappyPotatoHead/Signature-Verification-Model/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project aimed to develop a model to automate the verification of handwritten signatures. The challenge was to accurately compare scanned or captured signatures against known samples, even with variations in style and quality. By utilising a model, the process of verifying valid signatures can be significantly shorter and less tedious.

<p align="right"><a href="#readme-top">Back To Top</a></p>



### Built With

* [![Python][Python]][Python-url]
* [![PyTorch][PyTorch]][PyTorch-url]
* [![NumPy][NumPy]][NumPy]
* [![Matplotlib][Matplotlib]][Matplotlib-url]

<p align="right"><a href="#readme-top">Back To Top</a></p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Install the libraries listed in `requirements.txt`. The version of PyTorch used can be found in the [notebook](https://github.com/HappyPotatoHead/Signature-Verification-Model/blob/main/resnet_model.ipynb)

```sh
pip install -r requirements.txt
```

### Installation

Just clone the repository and you are good to go!

```sh
git clone https://github.com/HappyPotatoHead/Signature-Verification-Model.git
```

Change git remote url to avoid accidental pushes to base project
```sh
git remote set-url origin HappyPotatoHead/Signature-Verification-Model
git remote -v # confirm the changes
```

<p align="right"><a href="#readme-top">Back To Top</a></p>



<!-- USAGE EXAMPLES -->
## Usage

> Using the notebook is rather straightforward - I have arranged and ordered the cells in a logical order, so I will mainly cover the parts that you can *play around with* and what you should look out for. 
>
>Check out [The Garden](https://happypotatohead.github.io/project-garden/AI--and--Deep-Learning/Offline-Signature-Verification) to learn more!

I have provided a [sample model](https://drive.google.com/drive/folders/19Xu-Hgjdd62Sjq2RQoIWAeZ0aMTHTERz?usp=drive_link). If you would like to skip fine-tuning, you can run the configuration dictionaries and the classes and start executing from **Model Evaluation** onwards. Have fun!

To access the signature images: [Click me!](https://drive.google.com/drive/folders/1YbAjjXCEQwvv7jknDRO2xIKsmtC-Quyj?usp=drive_link)

### Image preprocessing

The *processing_images* folder contains the file necessary to fetch, load, and process the signature images; however, a naming function has yet to be implemented. 

For the fine-tuning of model to work, the images' names should be as follows:
 
*\<original/forgeries>\_\<signer's id>\_\<image's index>*

### Model

####  Configurable Code

Modify the **Configurations** section to control the fine-tuning of the model.

![Notebook Setup and Configurations](images/configurations.png)

`build_feature_extraction_model()` and `build_batch_triplet_loss` are used to define the model and the triplet loss function. 

![Model builder](images/model_builder.png) ![alt text](images/loss_function_builder.png)

Proceed to **Define Transforms** section to define transformers. 

![Transformers' definition](images/define_transformers.png)

#### K-Fold Cross Validation

By default, my definition of k-fold cross validation does not make checkpoints. 

![K-Fold does not make checkpoints by default](images/k_fold_no_checkpoint.png)

#### Evaluation

To evaluate the model on a dataset, the dataset has to be an instance of `TestingSignatureDataset` due to the difference in design between `TrainingSignatureDataset` and `TestingSignatureDataset`. So, you cannot reuse the training dataset instantiated with `TrainingSignatureDataset`. 


<p align="right"><a href="#readme-top">Back To Top</a></p>



<!-- ROADMAP -->
## Roadmap

- [] Hyperparameter tuning automation with Ray Tune
 
See the [open issues](https://github.com/HappyPotatoHead/Signature-Verification-Model/issues) for a full list of proposed features (and known issues).

<p align="right"><a href="#readme-top">Back To Top</a></p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right"><a href="#readme-top">Back To Top</a></p>

### Top contributors:

<a href="https://github.com/HappyPotatoHead/Signature-Verification-Model/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HappyPotatoHead/Signature-Verification-Model" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right"><a href="#readme-top">Back To Top</a></p>



<!-- CONTACT -->
## Contact

Jimmy Ding - jimmydingjk@gmail.com

Project Link: [Signature-Verification-Model](https://github.com/HappyPotatoHead/Signature-Verification-Model)

<p align="right"><a href="#readme-top">Back To Top</a></p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/HappyPotatoHead/Signature-Verification-Model.svg?style=for-the-badge
[contributors-url]: https://github.com/HappyPotatoHead/Signature-Verification-Model/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/HappyPotatoHead/Signature-Verification-Model.svg?style=for-the-badge
[forks-url]: https://github.com/HappyPotatoHead/Signature-Verification-Model/network/members

[stars-shield]: https://img.shields.io/github/stars/HappyPotatoHead/Signature-Verification-Model.svg?style=for-the-badge
[stars-url]: https://github.com/HappyPotatoHead/Signature-Verification-Model/stargazers

[issues-shield]: https://img.shields.io/github/issues/HappyPotatoHead/Signature-Verification-Model.svg?style=for-the-badge
[issues-url]: https://github.com/HappyPotatoHead/Signature-Verification-Model/issues


[license-shield]: https://img.shields.io/github/license/HappyPotatoHead/Signature-Verification-Model.svg?style=for-the-badge
[license-url]: https://github.com/HappyPotatoHead/Signature-Verification-Model/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jimmy-ding

[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[Python-url]: https://www.python.org/

[Matplotlib]: https://custom-icon-badges.demolab.com/badge/Matplotlib-71D291?logo=matplotlib&logoColor=fff
[Matplotlib-url]: https://matplotlib.org/

[NumPy]: https://img.shields.io/badge/NumPy-4DABCF?logo=numpy&logoColor=fff
[NumPy-url]: https://numpy.org/

[PyTorch]: https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white
[PyTorch-url]: https://docs.pytorch.org/docs/stable/index.html

[Scikit-learn]: https://img.shields.io/badge/-scikit--learn-%23F7931E?logo=scikit-learn&logoColor=white
[Scikit-learn]: https://scikit-learn.org/stable/
