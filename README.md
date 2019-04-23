# Reliable-and-Interpretable-AI-HS18
Assignments, projects and cheatsheet for the ETH Zurich Reliable and Interpretable Artificial Intelligence class autumn 2018.

The class covered the following topics:
- Adverserial Examples
- Fast Gradient Sign Method (FGSM)
- Projected Gradient Descent (PGD)
- Training Neural Networks with Logic
- Certify AI with Abstract Domains
- Visualization of Neural Networks
- Probabilistic Programming

[Class site](https://www.sri.inf.ethz.ch/teaching/riai2018)

[Course catalogue](http://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?semkez=2018W&ansicht=KATALOGDATEN&lerneinheitId=123752&lang=en)

## Project
Teamwork project as part of the class. The goal of the project is to design a precise and scalable automated verifier for proving the robustness of fully connected feedforward neural networks with rectified linear activations (ReLU) against adversarial attacks. More information can be found [here](./project).

## Cheatsheet
I summarized some of the most importants topics in a [cheatsheet](./cheatsheet).

## Assignments

### Install Instructions
Assignment directories contain `pip` requirement files to install python package dependencies:
```
virtualenv -p python3.6 .env
. .env/bin/activate
pip install requirements.txt
```

### Assignment 3
Simple FGSM and PGD examples for MNIST dataset.

[notebook](./assignments/ex3/task.ipynb).

### Assignment 4
Defend and train neural network against PGD attacks for MNIST dataset.

[notebook](./assignments/ex4/task.ipynb).

### Assignment 5
Train neural network with logical constrains for MNIST dataset.

[notebook](./assignments/ex6/ex6.ipynb).

### Assignment 6
Abstract representation of neural network in the interval domain.

[notebook](./assignments/ex6/ex6.ipynb).

### Assignment 7
Abstract representation of neural network in the zonotop domain.

[notebook](./assignments/ex7/notebook.ipynb).

### Assignment 8
Probabilisitc programming.
