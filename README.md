# DiFF-RF: forest of random partitioning trees for point-wise and collective anomaly detection
![](/fig/DiFF-RF.jpg)
This code is a simple implementation for the DiFF-RF algorithm described in this [draft paper](https://hal.archives-ouvertes.fr/hal-02882548v2/document), a semi-supervised approach for detecting point-wise or collective anomalies or outliers given a dataset of 'normal' instances. It implements a distance measure to a centroid and a frequency of visit mechanism at leaf level to build point-wise and collective anomaly scores. It solves a drawback identified in the Isolation Forest (IF) algorithm and outperforms in general IF and other state of the art methods in anomaly detection on a large set of diversified application datasets.


This code is derived from the one provided by Xiao Han as an implemention of the Isolation Forest algorithm available at [github.com/xhan0909](https://github.com/xhan0909)


## Requirements
It supports python3.5+

No extra requirement is needed apart numpy.

## Installation
    $ sudo python3  setup.py install

    (or $python3 setup.py install --user)


## Usage

A running example exploiting 'donnuts' data is given in file testDiFF_RF_Donnuts.py

The API documentation (html àr pdf) is described in the file documentation/DiFF-RF-API.(html/pdf)
(generated using $ pdoc3 DiFF_RF.py --html --force)

Typical usage (close to sklearn api) is as follows:

    # Creation of the data structure
    diff_rf = DiFF_TreeEnsemble(sample_size=sample_size, n_trees=ntrees)
    # fit the DiFF-RF with (normal) data: X_train, a nD numpy array whose dimensions should be (n_obs, n_features), n_jobs : the number of process
    diff_rf.fit(X_train, n_jobs=8)
    # Get the anomaly scores for test data X_test
    point_wise_scores, visiting_frequency_scores, collective_scores = diff_rf.anomaly_score(X_test,alpha=alpha0)

### Launching the test code (requires matplotlib and sklearn)
    $ python3 -i testDiFF_RF_Donuts.py

### creating an instance of the donut dataset (normal data) and the anomaly clusters (red and green clusters)
    >>> createDonutData(contamin=0)

### Creating and evaluating DiFF-RF
    >>> computeDiFF_RF(ntrees=512, sample_size=32)

### Some of the outputs are saved on disk
Data is saved in the *PKL* subdirectory
Figures are saved in the *FIG* subdirectory

    
Thanks to cite the above mentioned draft paper if you use this code.

    @article{marteau:hal-02882548,
        TITLE = {{Random Partitioning Forest for Point-Wise and Collective Anomaly Detection - Application to Network Intrusion Detection}},
        AUTHOR = {Marteau, Pierre-Fran{\c c}ois},
        URL = {https://hal.archives-ouvertes.fr/hal-02882548},
        JOURNAL = {{IEEE Transactions on Information Forensics and Security}},
        PUBLISHER = {{Institute of Electrical and Electronics Engineers}},
        PAGES = {1-16},
        YEAR = {2021},
        MONTH = Jan,
        DOI = {10.1109/TIFS.2021.3050605},
        KEYWORDS = {Machine Learning ; Semisupervised Learning ; NIDS ; Random Forest ; Anomaly Detection ; Random Partitioning Trees ; Semi- supervised Learning ; Intrusion Detection},
        PDF = {https://hal.archives-ouvertes.fr/hal-02882548v2/file/DiFF-RF-v3.pdf},
        HAL_ID = {hal-02882548},
        HAL_VERSION = {v2},
        }
