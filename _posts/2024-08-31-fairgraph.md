---
layout: post
title:  "Reproducibility Study Of Learning Fair Graph Representations Via Automated Data Augmentations"
date:   2024-08-31 23:59:59 +00:00
image: /images/publications/fairgraph.png
categories: research
author: "Thijmen Nijdam"
authors: <strong>Thijmen Nijdam</strong>, Juell Sprott, Taiki Papandreou-Lazos, Jurgen de Heus
venue: "Transactions on Machine Learning Research"
note: <u>Also:</u> Presented at NeurIPS 2024 as a poster as part of the Machine Learning Reprodicibilty Challenge (MLRC)
paper: https://openreview.net/forum?id=4WiqHopXQX
code: https://github.com/juellsprott/graphair-reproducibility
poster: docs/poster_fairgraph.pdf
# video: 
slides: docs/slides_fairgraph.pdf
---

In this study, we assessed the reproducibility of the paper "Learning Fair Graph Representations Via Automated Data Augmentations". We were able to partially reproduce one of the claims made by the original authors and fully reproduce the other two. Beyond verifying the original work, we extended the framework to assess its usability for another downstream task, specifically link prediction. We found that it significantly outperforms baselines on one fairness metric, while performing comparably on the other.
