\# IEMT302 - Simplest Machine Learning Demonstration



This repository contains the simplest implementation of Supervised Machine Learning using Python and `scikit-learn`.



\## How the Code Works



Traditional programming relies on hardcoded rules. Machine Learning supplies data (inputs and correct answers) and the model learns the rule on its own.



\### Key Concepts:

1\. \*\*Features (`X\_train`)\*\*: Inputs fed to the model `\[\[1.0], \[2.0], \[3.0], \[4.0], \[5.0]]`.

2\. \*\*Targets (`y\_train`)\*\*: Known outputs `\[2.0, 4.0, 6.0, 8.0, 10.0]`.

3\. \*\*Training (`model.fit()`)\*\*: Linear Regression finds $y = (w \\cdot x) + b$.

4\. \*\*Learned Parameters\*\*: Weight ($w = 2.0$), Bias ($b = 0.0$).

5\. \*\*Inference (`model.predict()`)\*\*: Unseen inputs (`6.0`, `10.0`, `25.0`) yield (`12.0`, `20.0`, `50.0`).



\---



\## How to Set Up and Run



\### Prerequisites

\- Python 3.8+ installed on your system.



\### Setup Steps

1\. Install Dependencies:

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

